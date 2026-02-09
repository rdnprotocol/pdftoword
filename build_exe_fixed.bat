@echo off
chcp 65001 >nul
echo ========================================
echo   PDF to Word - .exe Бэлтгэх
echo ========================================
echo.

REM Өмнөх build-ийг цэвэрлэх
echo Өмнөх build-ийг цэвэрлэж байна...
if exist "frontend\dist" (
    rmdir /s /q "frontend\dist" 2>nul
)

REM LLM загварыг хаах (хэрэв нээлттэй бол)
echo LLM загварыг шалгаж байна...
taskkill /F /IM python.exe /FI "WINDOWTITLE eq *mongolian*" 2>nul >nul

cd frontend

echo [1/2] React аппыг бэлтгэж байна...
call npm run build
if errorlevel 1 (
    echo АЛДАА: React апп бэлтгэхэд алдаа гарлаа!
    pause
    exit /b 1
)

echo.
echo [2/2] Electron аппыг багцлаж байна...
set CSC_IDENTITY_AUTO_DISCOVERY=false
call npm run electron-pack
if errorlevel 1 (
    echo АЛДАА: Electron багцлахад алдаа гарлаа!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Бэлтгэлт амжилттай!
echo ========================================
echo.
echo Гаралт: frontend\dist\
echo.
echo Файлууд:
echo - PDF to Word Setup X.X.X.exe (Суулгах)
echo - PDF to Word X.X.X.exe (Portable)
echo.
echo ТЭМДЭГЛЭЛ: LLM загвар (.gguf) багцлагдаагүй.
echo Хэрэглэгч өөрсдөө backend\models\ хавтас руу хуулах хэрэгтэй.
echo.
pause
