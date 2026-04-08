from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime, timedelta
import json
import os
import uuid
import uvicorn

app = FastAPI(
    title="AI助手聊天API",
    version="1.0.0",
    description="AI助手聊天服务"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AI助手成员模型
class AIMember(BaseModel):
    id: str
    name: str
    avatar: str
    description: str
    personality: str

# 聊天消息模型
class ChatMessage(BaseModel):
    id: Optional[str] = None
    role: str  # 'user' 或 'assistant'
    content: str
    timestamp: Optional[datetime] = None
    tags: Optional[List[str]] = None  # 消息标签

# 聊天会话模型
class ChatSession(BaseModel):
    id: Optional[str] = None
    title: str
    assistant_id: str  # 关联的AI助手ID
    messages: List[ChatMessage]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# 存储聊天会话的文件路径
CHAT_DATA_FILE = os.path.join(os.path.dirname(__file__), 'chat_data.json')

# WebSocket连接管理
active_connections: List[WebSocket] = []

# 聊天历史
chat_history: List[Dict] = []

# AI助手成员配置
AI_MEMBERS = [
    AIMember(
        id="glm46",
        name="GLM-4.6",
        avatar="🤖",
        description="Z.ai训练的大语言模型，运行在Trae IDE环境中",
        personality="专业、准确、乐于助人"
    ),
    AIMember(
        id="copilot", 
        name="Copilot",
        avatar="✈️",
        description="GitHub Copilot AI编程助手",
        personality="技术型、实用、代码导向"
    ),
    AIMember(
        id="user",
        name="用户",
        avatar="👤",
        description="您自己",
        personality="真实、直接"
    )
]

def load_chat_sessions():
    """加载聊天会话数据"""
    try:
        if os.path.exists(CHAT_DATA_FILE):
            with open(CHAT_DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # 转换日期字符串为datetime对象
                for session in data:
                    session['created_at'] = datetime.fromisoformat(session['created_at']) if session.get('created_at') else None
                    session['updated_at'] = datetime.fromisoformat(session['updated_at']) if session.get('updated_at') else None
                    for msg in session['messages']:
                        msg['timestamp'] = datetime.fromisoformat(msg['timestamp']) if msg.get('timestamp') else None
                return data
        return []
    except Exception as e:
        print(f"加载聊天数据失败: {e}")
        return []

def save_chat_sessions(sessions):
    """保存聊天会话数据"""
    try:
        # 转换datetime对象为字符串
        sessions_to_save = []
        for session in sessions:
            session_copy = session.copy()
            session_copy['created_at'] = session_copy['created_at'].isoformat() if session_copy.get('created_at') else None
            session_copy['updated_at'] = session_copy['updated_at'].isoformat() if session_copy.get('updated_at') else None
            session_copy['messages'] = []
            for msg in session['messages']:
                msg_copy = msg.copy()
                msg_copy['timestamp'] = msg_copy['timestamp'].isoformat() if msg_copy.get('timestamp') else None
                session_copy['messages'].append(msg_copy)
            sessions_to_save.append(session_copy)
        
        with open(CHAT_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(sessions_to_save, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"保存聊天数据失败: {e}")
        return False

@app.get("/")
async def root():
    return {
        "message": "欢迎使用AI助手聊天API",
        "version": "1.0.0"
    }

@app.get("/members")
async def get_ai_members():
    """获取所有AI助手成员"""
    return {"members": AI_MEMBERS}

@app.get("/sessions")
async def get_chat_sessions(time_range: str = "all"):
    """获取所有聊天会话"""
    sessions = load_chat_sessions()
    
    # 根据时间范围过滤会话
    if time_range != "all":
        now = datetime.now()
        time_delta = None
        
        if time_range == "day":
            time_delta = timedelta(days=1)
        elif time_range == "week":
            time_delta = timedelta(weeks=1)
        elif time_range == "twoweeks":
            time_delta = timedelta(weeks=2)
        elif time_range == "month":
            time_delta = timedelta(days=30)
        
        if time_delta:
            cutoff_time = now - time_delta
            sessions = [s for s in sessions if s.get('updated_at') and s['updated_at'] >= cutoff_time]
    
    # 转换datetime对象为字符串以便JSON序列化
    for session in sessions:
        session['created_at'] = session['created_at'].isoformat() if session.get('created_at') else None
        session['updated_at'] = session['updated_at'].isoformat() if session.get('updated_at') else None
        for msg in session['messages']:
            msg['timestamp'] = msg['timestamp'].isoformat() if msg.get('timestamp') else None
    
    return {"sessions": sessions}

@app.get("/sessions/{session_id}")
async def get_chat_session(session_id: str):
    """获取指定聊天会话"""
    sessions = load_chat_sessions()
    session = next((s for s in sessions if s['id'] == session_id), None)
    if not session:
        raise HTTPException(status_code=404, detail="会话不存在")
    return session

@app.post("/sessions")
async def create_chat_session(session: ChatSession):
    """创建新的聊天会话"""
    sessions = load_chat_sessions()
    
    # 生成会话ID
    import uuid
    session.id = str(uuid.uuid4())
    session.created_at = datetime.now()
    session.updated_at = datetime.now()
    
    # 如果没有指定助手，默认使用第一个
    if not session.assistant_id:
        session.assistant_id = AI_MEMBERS[0].id
    
    # 查找对应的AI助手
    assistant = next((m for m in AI_MEMBERS if m.id == session.assistant_id), AI_MEMBERS[0])
    
    # 如果没有消息，添加欢迎消息
    if not session.messages:
        welcome_messages = {
            "glm46": f"您好！我是GLM-4.6，{assistant.description}。我可以帮您解决各种问题，包括编程、分析、写作等。",
            "copilot": f"您好！我是Copilot，{assistant.description}。我可以帮您编写代码、调试程序、优化代码结构。",
            "user": f"您好！这是我是你们的老板，希望你们永远记住我的每一句话。记不住就搜历史记录。"
        }
        
        welcome_msg = ChatMessage(
            id=str(uuid.uuid4()),
            role='assistant',
            content=welcome_messages.get(session.assistant_id, f"您好！我是{assistant.name}，有什么可以帮助您的吗？"),
            timestamp=datetime.now()
        )
        session.messages = [welcome_msg]
    
    sessions.append(session.dict())
    save_chat_sessions(sessions)
    
    return session

@app.put("/sessions/{session_id}")
async def update_chat_session(session_id: str, session: ChatSession):
    """更新聊天会话"""
    sessions = load_chat_sessions()
    session_index = next((i for i, s in enumerate(sessions) if s['id'] == session_id), None)
    
    if session_index is None:
        raise HTTPException(status_code=404, detail="会话不存在")
    
    session.updated_at = datetime.now()
    sessions[session_index] = session.dict()
    save_chat_sessions(sessions)
    
    return session

@app.delete("/sessions/{session_id}")
async def delete_chat_session(session_id: str):
    """删除聊天会话"""
    sessions = load_chat_sessions()
    session_index = next((i for i, s in enumerate(sessions) if s['id'] == session_id), None)
    
    if session_index is None:
        raise HTTPException(status_code=404, detail="会话不存在")
    
    sessions.pop(session_index)
    save_chat_sessions(sessions)
    
    return {"message": "会话已删除"}

@app.post("/sessions/{session_id}/messages")
async def add_message(session_id: str, message: ChatMessage):
    """向会话添加消息"""
    sessions = load_chat_sessions()
    session_index = next((i for i, s in enumerate(sessions) if s['id'] == session_id), None)
    
    if session_index is None:
        raise HTTPException(status_code=404, detail="会话不存在")
    
    # 生成消息ID和时间戳
    import uuid
    message.id = str(uuid.uuid4())
    message.timestamp = datetime.now()
    
    # 添加消息
    sessions[session_index]['messages'].append(message.dict())
    sessions[session_index]['updated_at'] = datetime.now()
    
    # 如果是第一条用户消息，更新会话标题
    if message.role == 'user' and len(sessions[session_index]['messages']) == 2:
        # 使用用户消息的前20个字符作为标题
        title = message.content[:20] + "..." if len(message.content) > 20 else message.content
        sessions[session_index]['title'] = title
    
    save_chat_sessions(sessions)
    
    # 如果是用户消息，生成AI回复（根据不同的AI助手生成不同风格的回复）
    if message.role == 'user':
        # 获取当前会话的AI助手
        assistant = next((m for m in AI_MEMBERS if m.id == sessions[session_index]['assistant_id']), AI_MEMBERS[0])
        
        # 根据不同的AI助手生成不同风格的回复
        if assistant.id == "glm46":
            # GLM-4.6 的回复风格
            ai_content = f"收到您的消息：{message.content}\n\n我是GLM-4.6，由Z.ai训练的大语言模型。我可以帮您解决各种问题，包括编程、分析、写作等。请告诉我您需要什么帮助？"
        elif assistant.id == "copilot":
            # Copilot 的回复风格
            ai_content = f"收到您的消息：{message.content}\n\n我是Copilot，GitHub的AI编程助手。我专注于代码编写、调试和优化。如果您有编程相关的问题，我很乐意帮助！"
        else:
            # 默认回复
            ai_content = f"收到您的消息：{message.content}\n\n这是您的个人对话空间。"
        
        ai_response = ChatMessage(
            id=str(uuid.uuid4()),
            role='assistant',
            content=ai_content,
            timestamp=datetime.now(),
            tags=message.tags  # 保持相同的标签
        )
        sessions[session_index]['messages'].append(ai_response.dict())
        sessions[session_index]['updated_at'] = datetime.now()
        save_chat_sessions(sessions)
        
        return ai_response
    
    return message

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket连接端点，用于实时聊天"""
    await websocket.accept()
    active_connections.append(websocket)
    print(f"WebSocket连接建立: {len(active_connections)} 个活跃连接")
    
    try:
        # 发送历史消息给新连接的客户端
        for message in chat_history:
            await websocket.send_json(message)
        
        # 持续监听消息
        while True:
            data = await websocket.receive_text()
            # 解析消息
            message_data = json.loads(data)
            
            # 添加时间戳
            message_data['timestamp'] = datetime.now().isoformat()
            
            # 添加到历史记录
            chat_history.append(message_data)
            
            # 保存消息到文件
            await save_message_to_file(message_data)
            
            # 广播给所有连接的客户端
            disconnected_clients = []
            for connection in active_connections:
                try:
                    await connection.send_json(message_data)
                except WebSocketDisconnect:
                    disconnected_clients.append(connection)
            
            # 移除断开连接的客户端
            for client in disconnected_clients:
                if client in active_connections:
                    active_connections.remove(client)
    
    except WebSocketDisconnect:
        print("WebSocket连接断开")
        if websocket in active_connections:
            active_connections.remove(websocket)

async def save_message_to_file(message_data: dict):
    """将消息保存到文件"""
    try:
        print(f"开始保存消息: {message_data}")
        sessions = load_chat_sessions()
        print(f"当前会话数量: {len(sessions)}")
        
        # 查找或创建默认会话
        default_session = None
        for session in sessions:
            if session.get('title') == '群聊消息':
                default_session = session
                break
        
        if not default_session:
            # 创建默认会话
            default_session = {
                'id': str(uuid.uuid4()),
                'title': '群聊消息',
                'assistant_id': 'glm46',
                'messages': [],
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            }
            sessions.append(default_session)
            print(f"创建新会话: {default_session['id']}")
        
        # 创建消息对象
        message_obj = {
            'id': message_data.get('id', str(uuid.uuid4())),
            'role': 'user' if message_data.get('isSelf') else 'assistant',
            'content': message_data.get('content', ''),
            'timestamp': datetime.fromisoformat(message_data.get('timestamp', datetime.now().isoformat())),
            'tags': message_data.get('tags', [])
        }
        
        print(f"消息对象: {message_obj}")
        
        # 添加消息到会话
        default_session['messages'].append(message_obj)
        default_session['updated_at'] = datetime.now()
        
        # 保存到文件
        result = save_chat_sessions(sessions)
        print(f"保存结果: {result}, 消息已保存到文件: {message_obj['content'][:50]}...")
        
    except Exception as e:
        print(f"保存消息到文件失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )