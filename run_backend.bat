@echo off
cd backend

REM Check if virtual environment exists
if exist "..\.venv\Scripts\activate.bat" (
    echo Virtual environment олдлоо. Ашиглаж байна...
    call ..\.venv\Scripts\activate.bat
) else (
    echo Virtual environment олдсонгүй. Системийн Python ашиглаж байна...
)

python main.py
pause
