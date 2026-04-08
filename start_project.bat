@echo off
REM AI聊天项目总启动脚本
REM 启动前后端服务

echo 正在启动AI聊天项目...
echo 后端服务将在 http://localhost:8001 运行
echo 前端服务将在 http://localhost:8080 运行
echo.

REM 启动后端服务（在新窗口中）
start "AI聊天后端" cmd /k "cd /d %~dp0\backend && python main.py"

timeout /t 3 /nobreak >nul

REM 启动前端服务（在新窗口中）
start "AI聊天前端" cmd /k "cd /d %~dp0\frontend && python -m http.server 8080"

echo 项目已启动！
echo 访问 http://localhost:8080/index.html 使用实时聊天功能
echo.
pause