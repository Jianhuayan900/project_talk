# 贡献指南

感谢您对AI助手聊天模块的关注！我们欢迎任何形式的贡献。

## 如何贡献

### 报告问题

如果您发现了bug或有功能建议：

1. 检查[Issues](https://github.com/Jianhuayan900/project_talk/issues)中是否已有类似问题
2. 如果没有，请创建新的Issue，包含：
   - 清晰的标题
   - 详细的问题描述
   - 复现步骤
   - 预期行为
   - 实际行为
   - 环境信息（操作系统、Python版本等）
   - 相关的日志或截图

### 提交代码

#### 开发流程

1. **Fork项目**
   ```bash
   # 在GitHub上点击Fork按钮
   ```

2. **克隆您的Fork**
   ```bash
   git clone https://github.com/Jianhuayan900/project_talk.git
   cd project_talk
   ```

3. **创建功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-bug-fix
   ```

4. **进行开发**
   - 遵循代码规范（见下方）
   - 添加必要的测试
   - 更新相关文档

5. **提交更改**
   ```bash
   git add .
   git commit -m "描述您的更改"
   ```

6. **推送到您的Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **创建Pull Request**
   - 在GitHub上创建PR
   - 填写PR模板
   - 等待代码审查

#### 代码规范

**Python代码规范**
- 遵循PEP 8规范
- 使用有意义的变量和函数名
- 添加必要的注释和文档字符串
- 函数长度不超过50行
- 类职责单一

**JavaScript代码规范**
- 使用ES6+语法
- 遵循Vue 3最佳实践
- 组件命名使用PascalCase
- 函数命名使用camelCase

**Git提交信息规范**
```
<type>(<scope>): <subject>

<body>

<footer>
```

类型（type）：
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建/工具相关

示例：
```
feat(auth): 添加JWT认证功能

实现了基于JWT的用户认证机制，包括：
- Token生成和验证
- Token刷新机制
- 会话管理

Closes #123
```

#### 测试要求

- 新功能必须包含单元测试
- 测试覆盖率不低于80%
- 所有测试必须通过
- 提交PR前运行完整测试套件

```bash
# 运行测试
pytest

# 查看覆盖率
pytest --cov=backend --cov-report=html
```

#### 文档要求

- 新功能需要更新README.md
- API变更需要更新API文档
- 重大变更需要更新CHANGELOG.md
- 代码中添加必要的注释

## Pull Request流程

### PR模板

创建PR时，请填写以下信息：

**描述**
- 简要描述此PR的目的
- 说明解决了什么问题或添加了什么功能

**更改类型**
- [ ] Bug修复
- [ ] 新功能
- [ ] 代码重构
- [ ] 文档更新
- [ ] 性能优化
- [ ] 其他

**测试**
- [ ] 添加了单元测试
- [ ] 所有测试通过
- [ ] 手动测试通过

**检查清单**
- [ ] 代码遵循项目规范
- [ ] 更新了相关文档
- [ ] 添加了必要的注释
- [ ] 没有引入新的警告

**相关Issue**
- 关联的Issue编号

### 代码审查

- 所有PR都需要至少一位维护者审查
- 审查者可能会要求修改
- 请及时响应审查意见
- 修改后更新PR

### 合并

- 审查通过后，维护者会合并PR
- 使用Squash and Merge方式
- 合并后删除功能分支

## 开发环境设置

### 1. 克隆项目
```bash
git clone https://github.com/Jianhuayan900/project_talk.git
cd project_talk
```

### 2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 安装开发依赖
```bash
pip install pytest pytest-cov black flake8
```

### 5. 运行项目
```bash
# 启动后端
cd backend
python main.py

# 启动前端
cd frontend
python -m http.server 8080
```

### 6. 运行测试
```bash
pytest
```

### 7. 代码格式化
```bash
# 格式化Python代码
black backend/

# 检查代码规范
flake8 backend/
```

## 社区准则

### 行为准则

- 尊重所有贡献者
- 接受建设性批评
- 专注于对社区最有利的事情
- 对不同观点保持开放态度

### 不可接受的行为

- 使用性化语言或图像
- 人身攻击或侮辱性评论
- 公开或私下骚扰
- 未经许可发布他人隐私信息
- 其他不专业或不恰当的行为

## 获取帮助

如果您在贡献过程中遇到问题：

1. 查看[文档](README.md)
2. 搜索[Issues](https://github.com/Jianhuayan900/project_talk/issues)
3. 创建新的Issue寻求帮助
4. 在讨论区提问

## 许可

通过贡献代码，您同意您的贡献将根据项目的MIT许可证进行许可。

## 致谢

感谢所有贡献者！

---

再次感谢您的贡献！