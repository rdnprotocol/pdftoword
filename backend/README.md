# PDF to Word - Backend

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Tesseract OCR:
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Install with Mongolian language pack
   - Add to PATH or set TESSDATA_PREFIX environment variable

3. Install Poppler (for PDF to image conversion):
   - Download from: https://github.com/oschwartz10612/poppler-windows/releases
   - Add to PATH

4. (Optional) Setup llama.cpp:
   - Download llama.cpp from: https://github.com/ggerganov/llama.cpp
   - Compile or download pre-built Windows executable
   - Place in `llama.cpp/` directory
   - Download Mongolian LLM model (.gguf format) to `models/` directory

## Run

```bash
python main.py
```

Server runs on http://127.0.0.1:8000
