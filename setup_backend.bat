@echo off
echo Installing Python dependencies...
cd backend
pip install -r requirements.txt
echo.
echo Backend setup complete!
echo.
echo IMPORTANT: Make sure you have installed:
echo 1. Tesseract OCR with Mongolian language pack
echo 2. Poppler for PDF conversion
echo 3. (Optional) llama.cpp and Mongolian LLM model
echo.
pause
