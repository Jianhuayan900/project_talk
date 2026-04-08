@echo off
echo Starting AI Assistant Chat Application...
echo.

echo Starting Backend Server...
start "Backend Server" cmd /k "cd /d "%~dp0backend" && python main.py"

echo Waiting for backend to start...
timeout /t 3 /nobreak >nul

echo Starting Frontend Server...
start "Frontend Server" cmd /k "cd /d "%~dp0frontend" && python -m http.server 8080"

echo.
echo Backend: http://localhost:8001
echo Frontend: http://localhost:8080
echo.
echo Press any key to exit...
pause >nul