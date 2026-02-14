@echo off
echo Starting IEEE NEXUS 2026 Lunch System...
echo.
echo Student App will run on: http://localhost:8501
echo Scanner App will run on: http://localhost:8502
echo Admin Dashboard will run on: http://localhost:8503
echo.
echo Press Ctrl+C to stop all apps
echo.

start cmd /k "streamlit run student_app.py --server.port 8501"
timeout /t 3 /nobreak >nul
start cmd /k "streamlit run scanner_app.py --server.port 8502"
timeout /t 3 /nobreak >nul
start cmd /k "streamlit run dashboard_app.py --server.port 8503"

echo All apps started!
pause
