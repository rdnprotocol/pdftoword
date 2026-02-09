@echo off
chcp 65001 >nul
echo ========================================
echo   PDF to Word - Програмыг асаах
echo ========================================
echo.

REM Frontend суулгаагүй бол суулгах
if not exist "frontend\node_modules" (
    echo Frontend суулгаагүй байна. Суулгаж байна...
    cd frontend
    call npm install
    if errorlevel 1 (
        echo АЛДАА: Frontend суулгахад алдаа гарлаа!
        pause
        exit /b 1
    )
    cd ..
    echo Frontend суулгагдсан!
    echo.
)

echo Backend эхлүүлж байна...
start "PDF to Word - Backend" cmd /k "cd /d %~dp0backend && python main.py"

timeout /t 3 /nobreak >nul

echo Frontend эхлүүлж байна...
start "PDF to Word - Frontend" cmd /k "cd /d %~dp0frontend && npm start"

timeout /t 8 /nobreak >nul

echo Electron эхлүүлж байна...
start "PDF to Word - Electron" cmd /k "cd /d %~dp0frontend && npm run electron-dev"

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
