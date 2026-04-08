# 项目配置模板

使用此文件来配置您的项目信息。复制此文件为 `config.json` 并修改相应的值。

```json
{
  "project": {
    "name": "project_talk",
    "description": "AI助手聊天模块",
    "version": "1.0.0",
    "author": "Jianhuayan900",
    "email": "369752868@qq.com",
    "license": "MIT",
    "repository": "https://github.com/Jianhuayan900/project_talk"
  },
  "github": {
    "username": "Jianhuayan900",
    "repository": "project_talk",
    "issues_url": "https://github.com/Jianhuayan900/project_talk/issues",
    "releases_url": "https://github.com/Jianhuayan900/project_talk/releases",
    "security_url": "https://github.com/Jianhuayan900/project_talk/security"
  },
  "server": {
    "host": "0.0.0.0",
    "port": 8001,
    "debug": false
  },
  "features": {
    "enable_ai_integration": true,
    "enable_file_upload": false,
    "enable_voice_input": false,
    "max_file_size_mb": 10
  }
}
```

## 需要修改的个性化信息

在以下文件中，您需要替换占位符信息：

### 1. README.md
- 项目描述中的作者信息
- 联系方式

### 2. LICENSE
- 版权年份和作者名称

### 3. CONTRIBUTING.md
- GitHub仓库URL（5处）
- Issues链接（2处）

### 4. CODE_OF_CONDUCT.md
- 项目团队邮箱（1处）

### 5. CHANGELOG.md
- GitHub仓库链接（3处）

### 6. SECURITY.md
- 安全团队邮箱（2处）
- GitHub安全链接（2处）

### 7. .github/ISSUE_TEMPLATE/*.md
- 通常不需要修改

### 8. .github/PULL_REQUEST_TEMPLATE.md
- 通常不需要修改

## 快速替换指南

### 使用文本编辑器的批量替换功能

1. 打开所有需要修改的文件
2. 使用"查找和替换"功能
3. 替换以下占位符：

| 占位符 | 替换为您的信息 |
|---------|---------------|
| `Jianhuayan900` | 您的GitHub用户名 |
| `369752868@qq.com` | 您的邮箱地址 |
| `Jianhuayan900` | 您的真实姓名或昵称 |
| `2024` | 当前年份（如需要） |

### 使用sed命令（Linux/Mac）

```bash
# 在项目根目录执行
find . -type f \( -name "*.md" -o -name "*.txt" \) -exec sed -i '' 's/yourusername/YOUR_USERNAME/g' {} +
find . -type f \( -name "*.md" -o -name "*.txt" \) -exec sed -i '' 's/your-email@example.com/YOUR_EMAIL/g' {} +
find . -type f \( -name "*.md" -o -name "*.txt" \) -exec sed -i '' 's/Your Name/YOUR_NAME/g' {} +
```

### 使用PowerShell（Windows）

```powershell
# 在项目根目录执行
Get-ChildItem -Recurse -Include *.md,*.txt | ForEach-Object {
    (Get-Content $_.FullName) -replace 'yourusername', 'YOUR_USERNAME' | Set-Content $_.FullName
    (Get-Content $_.FullName) -replace 'your-email@example.com', 'YOUR_EMAIL' | Set-Content $_.FullName
    (Get-Content $_.FullName) -replace 'Your Name', 'YOUR_NAME' | Set-Content $_.FullName
}
```

## 验证修改

修改完成后，请验证：

1. **检查所有链接**
   - GitHub仓库链接是否正确
   - Issues链接是否可访问
   - Releases链接是否正确

2. **检查联系信息**
   - 邮箱地址是否正确
   - 作者信息是否准确

3. **测试功能**
   - 启动项目是否正常
   - 文档链接是否有效
   - 模板是否正常工作

## 注意事项

- **不要修改**：`.gitignore` 文件中的占位符
- **谨慎修改**：代码文件中的占位符（如果有）
- **备份原文件**：批量替换前建议备份
- **提交前检查**：使用`git diff`查看所有更改

## 示例配置

假设您的GitHub用户名是 `Jianhuayan900`，邮箱是 `369752868@qq.com`，姓名是 `Jianhuayan900`：

```bash
# 替换后的示例链接
https://github.com/Jianhuayan900/project_talk
https://github.com/Jianhuayan900/project_talk/issues
369752868@qq.com
```

## 需要帮助？

如果在配置过程中遇到问题，请：

1. 查看项目的README.md
2. 提交Issue寻求帮助
3. 参考GitHub官方文档

---

**配置完成后，请删除此文件或将其重命名为 `config.json.example`**