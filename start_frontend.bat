@echo off
REM AI聊天前端服务器启动脚本
REM 确保在项目根目录下运行

echo 正在启动AI聊天前端服务器...

REM 切换到前端目录
cd /d "%~dp0\frontend"

REM 启动前端服务器
python -m http.server 8080

pause