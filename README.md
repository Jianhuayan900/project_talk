# AI助手聊天模块

一个专为IDE环境设计的智能助手协作聊天系统，支持实时WebSocket通信、多主题切换、背景自定义、消息标签等功能。该模块与IDE的智能助手（包括Trae、GitHub Copilot等）深度集成，形成多智能助手协作环境，可以实现角色认定、项目任务讨论布置、跨助手信息交互联络等功能，并提供跨对话记录的长久保存机制。

## 应用场景

### IDE环境中的智能助手协作
本聊天模块专门为IDE（集成开发环境）设计，旨在创建一个多智能助手协作的工作环境：

- **多智能助手集成**：与IDE中的各种智能助手（Trae、GitHub Copilot、CodeLlama等）无缝集成，形成统一的聊天成员组
- **角色认定机制**：每个智能助手可以认定自己的专业角色（如代码审查、架构设计、测试专家等），在协作中发挥专长
- **项目任务讨论**：通过聊天界面进行项目任务的分析、讨论和布置，智能助手之间可以相互协作
- **跨助手信息交互**：实现不同智能助手之间的信息传递和协作，打破单一助手的局限
- **跨对话记录保存**：所有对话记录长久保存，支持跨项目、跨时间的信息检索和回溯

### 典型使用场景

#### 1. 代码审查协作
```
Trae（架构师）：这个模块的设计需要考虑扩展性
GitHub Copilot（代码专家）：我建议使用策略模式来处理不同的AI服务
CodeLlama（测试专家）：我会为这些策略编写单元测试
```

#### 2. 项目任务分配
```
用户：我们需要实现一个用户认证功能
Trae（项目经理）：我来制定技术方案和任务分解
GitHub Copilot（开发者）：我来实现核心代码逻辑
CodeLlama（测试专家）：我来设计测试用例和自动化测试
```

#### 3. 问题排查协作
```
用户：系统出现了内存泄漏问题
Trae（架构师）：从架构角度分析，可能是缓存策略问题
GitHub Copilot（代码专家）：我来检查代码中的资源释放逻辑
CodeLlama（性能专家）：我来分析性能监控数据
```

## 目录

- [功能特性](#功能特性)
- [环境要求](#环境要求)
- [依赖安装](#依赖安装)
- [快速开始](#快速开始)
- [详细配置](#详细配置)
- [使用指南](#使用指南)
- [文件结构](#文件结构)
- [API接口](#api接口)
- [技术栈](#技术栈)
- [集成到其他项目](#集成到其他项目)
- [数据存储](#数据存储)
- [扩展功能](#扩展功能)
- [常见问题](#常见问题)

## 功能特性

### IDE集成特性
- **多智能助手协作**：与IDE中的Trae、GitHub Copilot、CodeLlama等智能助手深度集成
- **角色认定系统**：支持智能助手认定专业角色，发挥各自专长
- **跨助手通信**：实现不同智能助手之间的信息传递和协作
- **项目任务管理**：通过聊天界面进行项目任务的讨论、分配和跟踪
- **跨对话持久化**：所有对话记录长久保存，支持跨项目、跨时间的信息检索
- **IDE上下文感知**：自动获取IDE上下文信息（当前文件、代码位置等）

### 核心功能
- **实时WebSocket通信**：基于WebSocket的双向实时消息传输
- **多会话管理**：支持创建、查看、删除多个聊天会话
- **消息标签系统**：支持预设标签和自定义标签，便于消息分类和检索
- **历史记录加载**：支持按时间范围加载历史消息（全部、一天、一周、两周、一月）
- **成员提及功能**：支持@提及功能，快速引用聊天成员

### 界面功能
- **多主题切换**：支持亮色、暗色、随系统三种主题模式
- **背景自定义**：支持自定义背景颜色和背景图片
- **响应式设计**：适配不同屏幕尺寸，类似微信的聊天界面
- **字体大小调节**：支持小、中、大三种字体大小设置
- **消息时间显示**：精确到秒的消息时间戳

### 数据功能
- **本地存储**：聊天数据以JSON格式本地存储
- **设置持久化**：用户设置（主题、背景、标签等）自动保存到localStorage
- **自动保存**：消息实时保存，防止数据丢失

## 环境要求

### 后端环境
- Python 3.7 或更高版本
- 操作系统：Windows、Linux、macOS

### 前端环境
- 现代浏览器（Chrome、Firefox、Safari、Edge等）
- 支持ES6+的JavaScript环境

## 依赖安装

### 安装Python依赖

```bash
cd project_talk
pip install -r requirements.txt
```

### 依赖列表

```
fastapi==0.104.1          # Web框架
uvicorn[standard]==0.24.0 # ASGI服务器
pydantic==2.5.0           # 数据验证
python-multipart==0.0.6   # 文件上传支持
websockets==12.0          # WebSocket支持
```

## 快速开始

### 方式一：使用启动脚本

#### Windows系统

```bash
# 启动后端服务
start_backend.bat

# 启动前端服务
start_frontend.bat

# 或一键启动全部服务
start_project.bat
```

#### Linux/macOS系统

```bash
# 启动后端服务
cd backend && python main.py &

# 启动前端服务
cd frontend && python -m http.server 8080 &
```

### 方式二：手动启动

#### 1. 启动后端服务

```bash
cd backend
python main.py
```

后端服务将在 `http://localhost:8001` 启动，支持WebSocket连接。

#### 2. 启动前端服务

```bash
cd frontend
python -m http.server 8080
```

然后在浏览器中访问 `http://localhost:8080`

#### 3. 访问应用

打开浏览器访问：`http://localhost:8080`

## 详细配置

### 后端配置

#### 修改端口

编辑 `backend/main.py` 文件，修改端口配置：

```python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)  # 修改端口号
```

#### 修改数据存储路径

编辑 `backend/main.py` 文件，修改数据文件路径：

```python
CHAT_DATA_FILE = "chat_data.json"  # 修改为你的路径
```

### 前端配置

#### 修改后端API地址

编辑 `frontend/index.html` 文件，修改API地址：

```javascript
const API_BASE_URL = 'http://localhost:8001';  // 修改为你的后端地址
const WS_URL = 'ws://localhost:8001/ws';       // 修改为你的WebSocket地址
```

#### 修改默认设置

编辑 `frontend/index.html` 文件，修改默认设置：

```javascript
const settings = ref({
    theme: 'system',           // 默认主题：'light', 'dark', 'system'
    autoScroll: true,          // 自动滚动
    showTimestamp: true,       // 显示时间戳
    soundEnabled: false,       // 启用提示音
    fontSize: 'medium',        // 字体大小：'small', 'medium', 'large'
    bgColor: '#f5f5f5',        // 默认背景颜色
    bgImage: ''                // 默认背景图片
});
```
  
## 使用指南

### IDE环境使用

#### 启动IDE集成模式

在IDE中启动聊天模块时，系统会自动：

1. **检测IDE环境**：识别当前运行的IDE（VSCode、Trae IDE等）
2. **加载智能助手**：自动集成IDE中的可用智能助手
3. **建立连接**：与IDE的API建立连接，获取上下文信息
4. **初始化角色**：为每个智能助手分配默认角色

#### 智能助手角色设定

在聊天界面中，可以为不同的智能助手设定专业角色：

**Trae助手角色**：
- 架构师：负责系统架构设计和技术方案制定
- 项目经理：负责任务分解和进度跟踪
- 代码审查：负责代码质量检查和优化建议

**GitHub Copilot角色**：
- 代码专家：负责代码生成和补全
- 重构专家：负责代码重构和优化
- Bug修复：负责问题诊断和修复

**CodeLlama角色**：
- 测试专家：负责测试用例设计和自动化测试
- 性能专家：负责性能分析和优化
- 文档专家：负责代码文档生成

#### 项目协作流程

**1. 任务讨论阶段**
```
用户：我们需要为项目添加用户认证功能
Trae（架构师）：我来分析一下技术方案。建议使用JWT token进行认证，配合Redis进行会话管理。
GitHub Copilot（代码专家）：我可以实现JWT的生成和验证逻辑。
CodeLlama（测试专家）：我会设计认证流程的测试用例。
```

**2. 任务分配阶段**
```
用户：@Trae 请制定详细的任务分解
Trae（项目经理）：好的，我分解为以下任务：
1. 用户注册接口开发
2. 登录认证接口开发  
3. Token验证中间件开发
4. 会话管理模块开发
5. 测试用例编写

@GitHub Copilot 请负责1-3项
@CodeLlama 请负责4-5项
```

**3. 协作开发阶段**
```
GitHub Copilot：我已经完成了用户注册接口，代码在 auth/register.py
Trae（代码审查）：我看了代码，建议添加输入验证和错误处理
CodeLlama：注册接口的测试用例我已经写好了，覆盖率95%
```

**4. 问题解决阶段**
```
用户：登录接口有时会超时
Trae（架构师）：可能是数据库连接池的问题，建议检查连接配置
GitHub Copilot：我发现了问题，连接池配置过小，已调整
CodeLlama：压力测试通过，响应时间从2s降到200ms
```

#### 跨对话信息检索

通过标签系统和历史记录搜索，可以快速找到相关的对话：

```javascript
// 搜索特定主题的对话
const searchResults = await searchConversations("用户认证");

// 搜索特定助手的建议
const traeSuggestions = await searchConversations("Trae 架构");

// 搜索特定项目的讨论
const projectDiscussions = await searchConversations("电商项目", project_id);
```

#### IDE上下文感知

聊天模块会自动获取IDE的上下文信息，让智能助手能够提供更精准的帮助：

**当前文件上下文**：
- 自动获取当前打开的文件路径和内容
- 智能助手可以基于当前代码提供建议
- 支持代码片段的讨论和修改

**项目结构上下文**：
- 获取项目的整体结构
- 智能助手可以理解项目架构
- 支持跨文件的代码分析

**Git上下文**：
- 获取当前分支和提交历史
- 智能助手可以理解代码变更
- 支持代码审查和合并建议

### 基本聊天功能

#### 发送消息
1. 在输入框中输入消息内容
2. 点击发送按钮或按Enter键发送消息
3. 消息会实时显示在聊天界面中

#### 添加标签
1. 点击输入框右侧的"标签"按钮
2. 从下拉菜单中选择预设标签
3. 或点击"+ 自定义"添加自定义标签
4. 标签会显示在消息下方

#### 提及成员
1. 在输入框中输入@符号
2. 从弹出的成员列表中选择要提及的成员
3. 成员名称会自动插入到消息中

### 主题和外观设置

#### 切换主题
1. 打开左侧设置面板
2. 在"主题"下拉菜单中选择：
   - **亮色**：浅色主题
   - **暗色**：深色主题
   - **随系统**：跟随系统主题自动切换

#### 设置背景颜色
1. 打开左侧设置面板
2. 点击"背景颜色"颜色选择器
3. 选择你喜欢的背景颜色
4. 背景颜色会立即应用并自动保存

#### 设置背景图片
1. 打开左侧设置面板
2. 点击"上传图片"按钮
3. 选择本地图片文件
4. 图片会自动设置为聊天背景
5. 如需清除，点击"清除背景图片"按钮

#### 调整字体大小
1. 打开左侧设置面板
2. 在"字体大小"下拉菜单中选择：
   - **小**：较小字体
   - **中**：中等字体（默认）
   - **大**：较大字体

### 历史记录管理

#### 加载历史消息
1. 在顶部时间范围选择器中选择：
   - **全部**：加载所有历史消息
   - **一天**：加载最近一天的消息
   - **一周**：加载最近一周的消息
   - **两周**：加载最近两周的消息
   - **一月**：加载最近一个月的消息

#### 查看会话
1. 左侧显示所有聊天会话
2. 点击会话名称切换到该会话
3. 当前会话会高亮显示

### 成员管理

#### 查看成员
1. 左侧面板显示所有聊天成员
2. 包括用户头像、名称和描述

#### 添加成员
1. 点击"添加成员"按钮
2. 输入成员信息
3. 保存后成员会显示在成员列表中

## 文件结构

```
project_talk/
├── backend/                    # 后端目录
│   ├── main.py               # 后端API服务和WebSocket处理
│   ├── chat_data.json        # 聊天数据存储文件
│   └── __pycache__/          # Python缓存文件
├── frontend/                  # 前端目录
│   └── index.html            # 前端聊天界面（包含HTML/CSS/JS）
├── start.bat                 # Windows一键启动脚本
├── start_backend.bat         # Windows后端启动脚本
├── start_frontend.bat        # Windows前端启动脚本
├── start_project.bat         # Windows项目启动脚本
├── requirements.txt          # Python依赖列表
└── README.md                 # 项目文档
```

## API接口

### HTTP接口

#### 获取所有会话
```http
GET http://localhost:8001/sessions?time_range=all
```

参数：
- `time_range`（可选）：时间范围，可选值：`all`, `day`, `week`, `twoweeks`, `month`

响应：
```json
{
  "sessions": [
    {
      "id": "会话ID",
      "title": "会话标题",
      "assistant_id": "助手ID",
      "messages": [...],
      "created_at": "2024-01-01T00:00:00",
      "updated_at": "2024-01-01T00:00:00"
    }
  ]
}
```

#### 获取指定会话
```http
GET http://localhost:8001/sessions/{session_id}
```

#### 创建新会话
```http
POST http://localhost:8001/sessions
Content-Type: application/json

{
  "title": "新会话",
  "assistant_id": "glm46",
  "messages": []
}
```

#### 更新会话
```http
PUT http://localhost:8001/sessions/{session_id}
Content-Type: application/json

{
  "title": "更新标题",
  "messages": [...]
}
```

#### 删除会话
```http
DELETE http://localhost:8001/sessions/{session_id}
```

#### 获取成员列表
```http
GET http://localhost:8001/members
```

### WebSocket接口

#### 连接WebSocket
```javascript
const ws = new WebSocket('ws://localhost:8001/ws');
```

#### 消息格式

客户端发送：
```json
{
  "type": "message",
  "content": "消息内容",
  "sender": "发送者ID",
  "sender_name": "发送者名称",
  "avatar": "头像",
  "tags": ["标签1", "标签2"]
}
```

服务器返回：
```json
{
  "type": "message",
  "content": "消息内容",
  "sender": "发送者ID",
  "sender_name": "发送者名称",
  "avatar": "头像",
  "timestamp": "2024-01-01T00:00:00",
  "tags": ["标签1", "标签2"]
}
```

## 技术栈

### 后端技术
- **FastAPI**：现代、快速的Web框架
- **Uvicorn**：ASGI服务器
- **WebSockets**：实时双向通信
- **Pydantic**：数据验证和序列化
- **Python 3.7+**：编程语言

### 前端技术
- **Vue 3**：渐进式JavaScript框架
- **Composition API**：Vue 3组合式API
- **原生HTML/CSS/JavaScript**：基础技术
- **CSS Variables**：主题和样式管理
- **WebSocket API**：实时通信
- **localStorage**：本地数据存储

## 集成到其他项目

### 集成到FastAPI项目

#### 1. 复制后端代码

将 `backend/main.py` 中的路由和WebSocket处理代码复制到你的FastAPI项目中：

```python
from fastapi import APIRouter

# 创建路由器
chat_router = APIRouter(prefix="/api/v1/chat")

# 复制所有路由代码...

# 在主应用中注册路由
from fastapi import FastAPI
app = FastAPI()
app.include_router(chat_router)
```

#### 2. 复制数据模型

复制所有Pydantic模型定义：

```python
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ChatMessage(BaseModel):
    id: Optional[str] = None
    role: str
    content: str
    timestamp: Optional[datetime] = None
    tags: Optional[List[str]] = None

class ChatSession(BaseModel):
    id: Optional[str] = None
    title: str
    assistant_id: str
    messages: List[ChatMessage]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
```

### 集成到Vue项目

#### 1. 提取Vue组件

将 `frontend/index.html` 中的Vue代码提取为单独的组件：

```vue
<template>
  <div class="chat-app">
    <!-- 复制模板部分 -->
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted, nextTick } from 'vue';

// 复制脚本部分
</script>

<style scoped>
/* 复制样式部分 */
</style>
```

#### 2. 配置API地址

在Vue项目中配置API地址：

```javascript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8001';
const WS_URL = import.meta.env.VITE_WS_URL || 'ws://localhost:8001/ws';
```

### 集成到React项目

#### 1. 转换为React组件

将Vue组件转换为React组件：

```jsx
import React, { useState, useEffect, useRef } from 'react';

function ChatComponent() {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const wsRef = useRef(null);

  // 转换Vue逻辑为React逻辑
  
  return (
    <div className="chat-app">
      {/* JSX模板 */}
    </div>
  );
}

export default ChatComponent;
```

## 数据存储

### JSON文件存储结构

聊天数据存储在 `backend/chat_data.json` 文件中：

```json
[
  {
    "id": "会话唯一标识",
    "title": "会话标题",
    "assistant_id": "关联的AI助手ID",
    "messages": [
      {
        "id": "消息唯一标识",
        "role": "user或assistant",
        "content": "消息内容",
        "timestamp": "2024-01-01T00:00:00.000000",
        "tags": ["标签1", "标签2"]
      }
    ],
    "created_at": "2024-01-01T00:00:00.000000",
    "updated_at": "2024-01-01T00:00:00.000000"
  }
]
```

### 本地存储结构

用户设置存储在浏览器的localStorage中：

```javascript
// 聊天设置
localStorage.getItem('chatSettings');

// 自定义标签
localStorage.getItem('chatCustomTags');
```

## 扩展功能

### IDE智能助手集成

#### 集成Trae助手

```python
# 在backend/main.py中添加Trae助手集成
class TraeAssistant:
    def __init__(self):
        self.name = "Trae"
        self.role = "架构师"
        self.avatar = "🤖"
        self.capabilities = [
            "代码架构设计",
            "技术方案制定",
            "项目任务分解",
            "代码审查"
        ]
    
    async def process_message(self, message: str, context: dict):
        """处理来自Trae的消息"""
        # 获取IDE上下文信息
        current_file = context.get('current_file')
        code_selection = context.get('code_selection')
        
        # Trae处理逻辑
        response = await self.call_trae_api(message, context)
        return response
    
    async def call_trae_api(self, message: str, context: dict):
        """调用Trae API"""
        # 实现Trae API调用逻辑
        pass

# 在WebSocket处理中使用
trae_assistant = TraeAssistant()

async def handle_websocket_message(websocket, data):
    if data["sender"] == "trae":
        # 处理Trae助手的消息
        context = get_ide_context()
        response = await trae_assistant.process_message(data["content"], context)
        await websocket.send_json(response)
```

#### 集成GitHub Copilot

```python
class CopilotAssistant:
    def __init__(self):
        self.name = "GitHub Copilot"
        self.role = "代码专家"
        self.avatar = "🐙"
        self.capabilities = [
            "代码生成",
            "代码补全",
            "代码重构",
            "bug修复"
        ]
    
    async def process_message(self, message: str, context: dict):
        """处理来自GitHub Copilot的消息"""
        # 获取代码上下文
        code_context = context.get('code_context')
        
        # Copilot处理逻辑
        response = await self.call_copilot_api(message, code_context)
        return response
    
    async def call_copilot_api(self, message: str, code_context: dict):
        """调用GitHub Copilot API"""
        # 实现Copilot API调用逻辑
        pass

# 在WebSocket处理中使用
copilot_assistant = CopilotAssistant()
```

#### IDE上下文获取

```python
def get_ide_context():
    """获取IDE当前上下文信息"""
    return {
        'current_file': get_current_file_path(),
        'current_line': get_cursor_line(),
        'code_selection': get_selected_code(),
        'project_structure': get_project_structure(),
        'git_branch': get_git_branch(),
        'open_files': get_open_files()
    }

# 这些函数需要与IDE的API进行集成
def get_current_file_path():
    """获取当前打开的文件路径"""
    # 实现IDE API调用
    pass

def get_cursor_line():
    """获取光标所在行"""
    # 实现IDE API调用
    pass

def get_selected_code():
    """获取选中的代码"""
    # 实现IDE API调用
    pass
```

#### 角色认定和任务分配

```python
class TaskManager:
    """任务管理器"""
    
    def __init__(self):
        self.assistants = {
            'trae': TraeAssistant(),
            'copilot': CopilotAssistant(),
            'codellama': CodeLlamaAssistant()
        }
        self.active_tasks = []
    
    async def assign_task(self, task: dict, context: dict):
        """根据任务类型分配给合适的助手"""
        task_type = task.get('type')
        
        # 根据任务类型选择合适的助手
        if task_type == 'architecture':
            assistant = self.assistants['trae']
        elif task_type == 'coding':
            assistant = self.assistants['copilot']
        elif task_type == 'testing':
            assistant = self.assistants['codellama']
        else:
            # 多助手协作
            return await self.collaborative_task(task, context)
        
        # 分配任务
        response = await assistant.process_message(task['description'], context)
        return response
    
    async def collaborative_task(self, task: dict, context: dict):
        """多助手协作处理任务"""
        results = {}
        
        # 按顺序让不同助手处理
        for assistant_name, assistant in self.assistants.items():
            result = await assistant.process_message(task['description'], context)
            results[assistant_name] = result
        
        # 综合结果
        return self.synthesize_results(results)

# 在WebSocket中使用
task_manager = TaskManager()

async def handle_task_assignment(websocket, data):
    """处理任务分配"""
    task = {
        'type': data.get('task_type'),
        'description': data.get('description'),
        'priority': data.get('priority', 'normal')
    }
    
    context = get_ide_context()
    result = await task_manager.assign_task(task, context)
    
    await websocket.send_json({
        'type': 'task_result',
        'result': result,
        'task_id': data.get('task_id')
    })
```

#### 跨对话记录持久化

```python
class ConversationManager:
    """对话管理器"""
    
    def __init__(self):
        self.conversations = {}
        self.cross_project_index = {}
    
    def save_conversation(self, session_id: str, conversation: dict):
        """保存对话记录"""
        # 保存到主存储
        self.conversations[session_id] = conversation
        
        # 建立跨项目索引
        project_id = conversation.get('project_id')
        if project_id:
            if project_id not in self.cross_project_index:
                self.cross_project_index[project_id] = []
            self.cross_project_index[project_id].append(session_id)
    
    def search_conversations(self, query: str, project_id: str = None):
        """搜索对话记录"""
        results = []
        
        # 确定搜索范围
        search_sessions = []
        if project_id:
            search_sessions = self.cross_project_index.get(project_id, [])
        else:
            search_sessions = self.conversations.keys()
        
        # 执行搜索
        for session_id in search_sessions:
            conversation = self.conversations.get(session_id)
            if self.matches_query(conversation, query):
                results.append(conversation)
        
        return results
    
    def matches_query(self, conversation: dict, query: str) -> bool:
        """检查对话是否匹配查询"""
        # 在消息内容中搜索
        for message in conversation.get('messages', []):
            if query.lower() in message.get('content', '').lower():
                return True
        
        # 在标签中搜索
        for message in conversation.get('messages', []):
            for tag in message.get('tags', []):
                if query.lower() in tag.lower():
                    return True
        
        return False

# 在API中使用
conversation_manager = ConversationManager()

@app.post("/conversations/search")
async def search_conversations(query: str, project_id: Optional[str] = None):
    """搜索对话记录"""
    results = conversation_manager.search_conversations(query, project_id)
    return {"results": results}
```

### 集成真实AI服务

#### 集成OpenAI

修改 `backend/main.py` 中的WebSocket消息处理：

```python
import openai

async def handle_websocket_message(websocket, data):
    if data["type"] == "message":
        # 保存用户消息
        save_message_to_session(session_id, data)
        
        # 调用OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": data["content"]}]
        )
        
        ai_content = response.choices[0].message.content
        
        # 发送AI回复
        ai_message = {
            "type": "message",
            "content": ai_content,
            "sender": "ai_assistant",
            "sender_name": "AI助手",
            "avatar": "🤖",
            "timestamp": datetime.now().isoformat()
        }
        await websocket.send_json(ai_message)
```

#### 集成Claude

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

async def get_claude_response(message):
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1024,
        messages=[{"role": "user", "content": message}]
    )
    return response.content[0].text
```

### 使用数据库存储

#### SQLite数据库

```python
import sqlite3
from datetime import datetime

def init_database():
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id TEXT PRIMARY KEY,
            title TEXT,
            assistant_id TEXT,
            created_at TEXT,
            updated_at TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id TEXT PRIMARY KEY,
            session_id TEXT,
            role TEXT,
            content TEXT,
            timestamp TEXT,
            tags TEXT,
            FOREIGN KEY (session_id) REFERENCES sessions (id)
        )
    ''')
    
    conn.commit()
    conn.close()
```

#### PostgreSQL数据库

```python
from sqlalchemy import create_engine, Column, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class ChatSession(Base):
    __tablename__ = "chat_sessions"
    
    id = Column(String, primary_key=True)
    title = Column(String)
    assistant_id = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
    messages = relationship("ChatMessage", back_populates="session")

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    
    id = Column(String, primary_key=True)
    session_id = Column(String, ForeignKey("chat_sessions.id"))
    role = Column(String)
    content = Column(Text)
    timestamp = Column(DateTime)
    tags = Column(Text)  # JSON格式存储
    
    session = relationship("ChatSession", back_populates="messages")

# 数据库连接
engine = create_engine("postgresql://user:password@localhost/chatdb")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
```

### 添加用户认证

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    # 验证token逻辑
    user = verify_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的认证凭据"
        )
    return user

# 在路由中使用
@app.get("/sessions")
async def get_chat_sessions(current_user = Depends(get_current_user)):
    # 只有认证用户才能访问
    pass
```

### 添加文件上传功能

```python
from fastapi import UploadFile, File

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # 保存文件
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"filename": file.filename, "location": file_location}
```

## 常见问题

### 1. 后端服务无法启动

**问题**：运行 `python main.py` 时出现错误

**解决方案**：
- 确保Python版本为3.7或更高
- 安装所有依赖：`pip install -r requirements.txt`
- 检查端口8001是否被占用

### 2. 前端无法连接后端

**问题**：前端显示连接失败

**解决方案**：
- 确保后端服务正在运行
- 检查后端地址是否正确（默认为 `http://localhost:8001`）
- 检查浏览器控制台是否有错误信息

### 3. WebSocket连接断开

**问题**：聊天过程中连接突然断开

**解决方案**：
- 检查网络连接
- 查看后端日志是否有错误信息
- 前端会自动尝试重新连接

### 4. 历史记录无法加载

**问题**：切换时间范围后没有显示历史消息

**解决方案**：
- 确保 `chat_data.json` 文件存在且格式正确
- 检查是否有"群聊消息"会话
- 查看浏览器控制台是否有错误信息

### 5. 背景图片无法显示

**问题**：上传背景图片后没有显示

**解决方案**：
- 确保图片格式正确（支持jpg、png、gif等）
- 检查图片文件大小是否过大
- 清除浏览器缓存后重试

### 6. 主题切换不生效

**问题**：切换主题后界面没有变化

**解决方案**：
- 清除浏览器localStorage
- 刷新页面
- 检查浏览器是否支持CSS变量

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 联系方式

如有问题或建议，请通过以下方式联系：
- 提交Issue
- 发送邮件

## 更新日志

### v1.0.0 (2024-04-08)
- 初始版本发布
- 支持基本的聊天功能
- 支持WebSocket实时通信
- 支持多主题切换
- 支持背景自定义
- 支持消息标签系统
- 支持历史记录加载
- 支持成员提及功能
- **IDE环境集成**：专为IDE设计的智能助手协作系统
- **多智能助手支持**：集成Trae、GitHub Copilot等智能助手
- **角色认定机制**：支持智能助手专业角色设定
- **跨助手协作**：实现不同智能助手之间的信息交互
- **项目任务管理**：通过聊天界面进行任务讨论和分配
- **跨对话持久化**：支持跨项目、跨时间的对话记录保存
- **IDE上下文感知**：自动获取IDE上下文信息提供精准帮助

## IDE集成架构

### 系统架构图

```
┌─────────────────────────────────────────────────────────────┐
│                      IDE Environment                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Trae IDE   │  │   VSCode     │  │  JetBrains   │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
│         │                 │                 │             │
│         └─────────────────┴─────────────────┘             │
│                           │                               │
│                  ┌────────▼────────┐                     │
│                  │  Chat Module   │                     │
│                  │  (WebSocket)   │                     │
│                  └────────┬────────┘                     │
│                           │                               │
└───────────────────────────┼───────────────────────────────┘
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
    ┌────▼────┐      ┌────▼────┐      ┌────▼────┐
    │  Trae   │      │ Copilot │      │CodeLlama│
    │Assistant│      │Assistant│      │Assistant│
    └─────────┘      └─────────┘      └─────────┘
```

### 数据流程

1. **用户输入** → 聊天界面
2. **上下文获取** → IDE API → 当前文件、项目结构、Git信息
3. **消息路由** → 根据角色分配给对应的智能助手
4. **智能处理** → 各智能助手并行或串行处理
5. **结果整合** → 综合多个助手的回复
6. **消息保存** → 持久化存储到数据库
7. **界面更新** → 实时显示在聊天界面

### 技术优势

- **无缝集成**：与IDE深度集成，无需额外配置
- **智能路由**：自动将消息路由到最合适的助手
- **上下文感知**：理解代码上下文，提供精准建议
- **协作增强**：多助手协作，发挥各自优势
- **持久化存储**：所有对话长久保存，便于回溯
- **跨项目支持**：支持多个项目的对话管理

## 未来规划

### 短期目标 (v1.1)
- [ ] 支持更多IDE（IntelliJ IDEA、Eclipse等）
- [ ] 增加语音输入功能
- [ ] 支持代码块高亮和语法分析
- [ ] 添加任务进度跟踪界面

### 中期目标 (v1.2)
- [ ] 支持自定义智能助手插件
- [ ] 增加协作白板功能
- [ ] 支持代码审查流程
- [ ] 添加性能监控和优化建议

### 长期目标 (v2.0)
- [ ] 支持分布式团队协作
- [ ] 集成CI/CD流程
- [ ] 支持AI模型训练和微调
- [ ] 建立智能助手生态系统