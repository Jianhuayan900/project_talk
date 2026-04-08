@echo off
REM AI聊天项目启动脚本
REM 确保在项目根目录下运行

echo 正在启动AI聊天后端服务...

REM 切换到后端目录
cd /d "%~dp0\backend"

REM 启动后端服务
python main.py

pause