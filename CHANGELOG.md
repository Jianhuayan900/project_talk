# 更新日志

本文档记录了项目的所有重要变更。

格式基于[Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循[语义化版本](https://semver.org/lang/zh-CN/)。

## [未发布]

### 计划中
- 支持更多IDE（IntelliJ IDEA、Eclipse等）
- 增加语音输入功能
- 支持代码块高亮和语法分析
- 添加任务进度跟踪界面

## [1.0.0] - 2024-04-08

### 新增
- 基础聊天功能
- WebSocket实时通信
- 多会话管理
- 消息标签系统（预设标签和自定义标签）
- 历史记录加载（支持按时间范围过滤）
- 成员提及功能（@提及）
- 多主题切换（亮色、暗色、随系统）
- 背景自定义（颜色和图片）
- 字体大小调节（小、中、大）
- 响应式设计
- 消息时间显示
- 设置持久化（localStorage）

### IDE集成特性
- 多智能助手协作支持
- 角色认定机制
- 跨助手通信
- 项目任务管理
- 跨对话持久化
- IDE上下文感知

### 技术实现
- FastAPI后端框架
- Vue 3前端框架
- WebSocket双向通信
- JSON文件存储
- RESTful API接口
- CORS跨域支持

### 文档
- 完整的README文档
- API接口文档
- 使用指南
- 集成指南
- 常见问题解答
- 系统架构说明

### 开发工具
- Windows启动脚本
- 依赖管理（requirements.txt）
- Git版本控制
- 开发环境配置

## 版本说明

### 版本号规则
- **主版本号**：不兼容的API变更
- **次版本号**：向下兼容的功能性新增
- **修订号**：向下兼容的问题修正

### 变更类型
- **新增**：新功能
- **变更**：现有功能的变更
- **弃用**：即将移除的功能
- **移除**：已移除的功能
- **修复**：bug修复
- **安全**：安全相关的修复

## 链接

- [GitHub仓库](https://github.com/Jianhuayan900/project_talk)
- [问题追踪](https://github.com/Jianhuayan900/project_talk/issues)
- [发布页面](https://github.com/Jianhuayan900/project_talk/releases)