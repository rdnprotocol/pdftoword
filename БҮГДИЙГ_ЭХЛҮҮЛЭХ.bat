@echo off
chcp 65001 >nul
echo ========================================
echo   PDF to Word - Бүгдийг эхлүүлэх
echo ========================================
echo.

echo Backend эхлүүлж байна...
if exist ".venv\Scripts\activate.bat" (
    start "PDF to Word - Backend" cmd /k "cd backend && call ..\..venv\Scripts\activate.bat && python main.py"
) else (
    start "PDF to Word - Backend" cmd /k "cd backend && python main.py"
)

timeout /t 3 /nobreak >nul

echo Frontend эхлүүлж байна...
start "PDF to Word - Frontend" cmd /k "cd frontend && npm start"

timeout /t 5 /nobreak >nul

echo Electron эхлүүлж байна...
start "PDF to Word - Electron" cmd /k "cd frontend && npm run electron-dev"

echo.
echo ========================================
echo   Бүх сервис эхлүүлсэн!
echo ========================================
echo.
echo Гурван цонх нээгдсэн:
echo - Backend (http://127.0.0.1:8000)
echo - Frontend (http://localhost:3000)
echo - Electron (Desktop app)
echo.
echo Програмыг хаахдаа бүх цонхыг хаана уу.
echo.
pause
