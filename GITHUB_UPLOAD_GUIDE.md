# GitHub上传指南

本指南将帮助您将AI助手聊天系统上传到GitHub。

## 前置准备

### 1. 检查项目文件

确保以下文件都已创建：

```
project_talk/
├── LICENSE                          ✅ MIT许可证
├── .gitignore                       ✅ Git忽略配置
├── .dockerignore                    ✅ Docker忽略配置
├── README.md                        ✅ 项目文档
├── CONTRIBUTING.md                   ✅ 贡献指南
├── CODE_OF_CONDUCT.md                ✅ 行为准则
├── CHANGELOG.md                     ✅ 更新日志
├── SECURITY.md                      ✅ 安全政策
├── SETUP_GUIDE.md                   ✅ 配置指南
├── DOCKER_SETUP.md                   ✅ Docker设置（本文件）
├── requirements.txt                 ✅ Python依赖
├── Dockerfile                       ✅ Docker配置
├── docker-compose.yml                ✅ Docker Compose
├── start.bat                        ✅ Windows启动脚本
├── start_backend.bat                ✅ 后端启动脚本
├── start_frontend.bat               ✅ 前端启动脚本
├── start_project.bat                ✅ 项目启动脚本
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md           ✅ Bug报告模板
│   │   └── feature_request.md      ✅ 功能请求模板
│   └── PULL_REQUEST_TEMPLATE.md    ✅ Pull请求模板
├── backend/
│   ├── main.py                    ✅ 后端服务
│   └── chat_data.json             ✅ 聊天数据
└── frontend/
    └── index.html                ✅ 前端界面
```

### 2. 修改占位符（可选）

如果需要修改文档中的占位符，请参考 `SETUP_GUIDE.md`。

## 上传步骤

### 方法1：使用Git命令行（推荐）

#### 步骤1：初始化Git仓库

```bash
cd d:\Users\john\AppProject\WorkSpace\AIphaInsight\project_talk
git init
```

#### 步骤2：添加所有文件

```bash
git add .
```

#### 步骤3：查看待提交的文件

```bash
git status
```

#### 步骤4：提交更改

```bash
git commit -m "Initial commit: AI助手聊天系统

- 实现WebSocket实时通信
- 支持多智能助手协作
- 添加主题切换和背景自定义
- 集成IDE环境支持
- 完整的文档和配置"
```

#### 步骤5：创建GitHub仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - Repository name: `project_talk`
   - Description: `AI助手聊天模块 - 专为IDE设计的智能助手协作系统`
   - Public/Private: 选择Public（推荐开源）
   - 不要勾选"Initialize this repository with a README"
3. 点击"Create repository"

#### 步骤6：连接到GitHub仓库

```bash
git remote add origin https://github.com/Jianhuayan900/project_talk.git
```

**注意**：将 `Jianhuayan900` 替换为您的GitHub用户名。

#### 步骤7：推送到GitHub

```bash
git branch -M main
git push -u origin main
```

### 方法2：使用GitHub Desktop（图形界面）

#### 步骤1：安装GitHub Desktop

下载并安装：https://desktop.github.com/

#### 步骤2：克隆或创建仓库

1. 打开GitHub Desktop
2. 点击"File" → "Add Local Repository"
3. 选择项目文件夹：`d:\Users\john\AppProject\WorkSpace\AIphaInsight\project_talk`

#### 步骤3：提交更改

1. 在左侧面板查看所有更改
2. 在"Summary"中填写提交信息
3. 点击"Commit to main"

#### 步骤4：推送到GitHub

1. 点击"Publish repository"
2. 填写仓库信息：
   - Name: `project_talk`
   - Description: `AI助手聊天模块`
   - 选择"Keep this code private"或"Public"
3. 点击"Publish repository"

### 方法3：使用VSCode（推荐）

#### 步骤1：打开项目

1. 打开VSCode
2. File → Open Folder
3. 选择：`d:\Users\john\AppProject\WorkSpace\AIphaInsight\project_talk`

#### 步骤2：初始化Git

1. 点击左侧源代码管理图标（或按Ctrl+Shift+G）
2. 点击"Initialize Repository"

#### 步骤3：提交更改

1. 在"Message"框中输入提交信息
2. 点击"Commit"按钮（或按Ctrl+Enter）

#### 步骤4：推送到GitHub

1. 点击状态栏的"Publish to GitHub"
2. 填写仓库信息
3. 点击"Publish"

## 上传后的配置

### 1. 设置仓库描述

1. 访问您的GitHub仓库
2. 点击"Settings"
3. 在"Description"中填写：
   ```
   AI助手聊天模块 - 专为IDE设计的智能助手协作系统
   支持WebSocket实时通信、多主题切换、背景自定义、消息标签等功能
   ```

### 2. 设置仓库主题

1. 在仓库页面点击"Settings"
2. 滚动到"GitHub Pages"部分
3. 选择主题（推荐"Minimal"或"Architect"）

### 3. 添加仓库标签

在仓库页面添加以下标签：
- `ai-assistant`
- `chat-system`
- `websocket`
- `vue3`
- `fastapi`
- `ide-integration`
- `python`
- `javascript`

### 4. 设置仓库图标（可选）

1. 准备一个正方形的图标（建议512x512像素）
2. 在仓库页面点击"Settings"
3. 滚动到"GitHub Pages"
4. 上传图标

### 5. 启用GitHub Issues

1. 在仓库页面点击"Settings"
2. 滚动到"Features"
3. 确保"Issues"已启用

### 6. 启用GitHub Actions（可选）

如果需要自动化测试和部署：

1. 创建 `.github/workflows/ci.yml`：
```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest
```

## 验证上传

### 检查清单

上传完成后，请验证：

- [ ] 仓库页面正常显示
- [ ] README.md内容正确显示
- [ ] 所有文件都已上传
- [ ] LICENSE文件显示正确
- [ ] Issues和Pull Requests模板正常工作
- [ ] 可以克隆仓库

### 测试克隆

```bash
# 在另一个目录测试克隆
cd d:\temp
git clone https://github.com/Jianhuayan900/project_talk.git
cd project_talk

# 测试运行
python -m http.server 8080
```

## Docker部署

### 使用Docker运行

```bash
# 构建并启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down

# 重新构建
docker-compose up -d --build
```

### 访问服务

- 前端：http://localhost:8080
- 后端：http://localhost:8001
- API文档：http://localhost:8001/docs

## 常见问题

### Q1: 推送时提示认证错误

**解决方案**：
```bash
# 使用个人访问令牌
# 1. 访问 https://github.com/settings/tokens
# 2. 生成新的Personal Access Token
# 3. 使用Token代替密码
git push -u origin main
# 用户名：GitHub用户名
# 密码：Personal Access Token
```

### Q2: 文件太大无法推送

**解决方案**：
```bash
# 增加Git缓冲区大小
git config http.postBuffer 524288000

# 或者使用Git LFS（大文件存储）
git lfs install
git lfs track "*.psd"
git add .gitattributes
```

### Q3: .gitignore不生效

**解决方案**：
```bash
# 清除Git缓存
git rm -r --cached .
git add .
git commit -m "Update .gitignore"
```

### Q4: 如何删除已上传的文件

**解决方案**：
```bash
# 删除文件但保留本地文件
git rm --cached filename

# 删除文件夹
git rm -r --cached foldername

# 提交并推送
git commit -m "Remove files"
git push
```

## 下一步

上传成功后，您可以：

1. **分享项目**：将仓库链接分享给他人
2. **邀请协作者**：在Settings → Collaborators中添加
3. **创建Release**：在Releases页面发布版本
4. **设置GitHub Pages**：部署项目文档
5. **集成CI/CD**：使用GitHub Actions自动化

## 资源链接

- [GitHub官方文档](https://docs.github.com/)
- [Git官方文档](https://git-scm.com/doc)
- [Docker官方文档](https://docs.docker.com/)
- [VSCode Git集成](https://code.visualstudio.com/docs/sourcecontrol/overview)

---

**恭喜！您的项目已成功上传到GitHub！** 🎉