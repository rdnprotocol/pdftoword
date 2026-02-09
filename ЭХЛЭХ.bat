@echo off
chcp 65001 >nul
echo ========================================
echo   PDF to Word - Эхлэх заавар
echo ========================================
echo.

echo [1/3] Backend суулгах...
cd backend
if not exist "venv" (
    echo Python dependencies суулгаж байна...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo АЛДАА: Python dependencies суулгахад алдаа гарлаа!
        pause
        exit /b 1
    )
) else (
    echo Backend dependencies аль хэдийн суулгагдсан байна.
)
cd ..

echo.
echo [2/3] Frontend суулгах...
cd frontend
if not exist "node_modules" (
    echo Node.js dependencies суулгаж байна...
    call npm install
    if errorlevel 1 (
        echo АЛДАА: Node.js dependencies суулгахад алдаа гарлаа!
        pause
        exit /b 1
    )
) else (
    echo Frontend dependencies аль хэдийн суулгагдсан байна.
)
cd ..

echo.
echo ========================================
echo   Суулгалт дууссан!
echo ========================================
echo.
echo ДАРААГИЙН АЛХМУУД:
echo.
echo 1. Backend ажиллуулах (Терминал 1):
echo    run_backend.bat
echo.
echo 2. Frontend ажиллуулах (Терминал 2):
echo    run_frontend.bat
echo.
echo 3. Electron ажиллуулах (Терминал 3):
echo    run_electron.bat
echo.
echo ДЭЛГЭРЭНГҮЙ ЗААВАР: ЭХЛЭХ_ЗААВАР.md файлыг уншина уу
echo.
pause
