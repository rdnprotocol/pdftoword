@echo off
chcp 65001 >nul
echo ========================================
echo   PDF to Word - .exe Бэлтгэх
echo   (Code Signing идэвхгүй)
echo ========================================
echo.

REM Code signing cache цэвэрлэх
echo Code signing cache цэвэрлэж байна...
if exist "%LOCALAPPDATA%\electron-builder\Cache\winCodeSign" (
    rmdir /s /q "%LOCALAPPDATA%\electron-builder\Cache\winCodeSign" 2>nul
)

REM Өмнөх build-ийг цэвэрлэх
echo Өмнөх build-ийг цэвэрлэж байна...
if exist "frontend\dist" (
    rmdir /s /q "frontend\dist" 2>nul
)

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
REM Code signing идэвхгүй болгох
set CSC_IDENTITY_AUTO_DISCOVERY=false
set WIN_CSC_LINK=
set WIN_CSC_KEY_PASSWORD=
call npm run electron-pack
if errorlevel 1 (
    echo.
    echo АЛДАА: Electron багцлахад алдаа гарлаа!
    echo.
    echo ШИЙДЭЛ: PowerShell-ийг "Run as Administrator" гэж нээж дахин оролдоно уу.
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
pause
