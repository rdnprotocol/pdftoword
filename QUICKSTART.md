# Quick Start Guide

## Prerequisites

1. **Python 3.8+** installed
2. **Node.js 16+** installed
3. **Tesseract OCR** with Mongolian language pack
4. **Poppler** for PDF conversion
5. (Optional) **llama.cpp** and Mongolian LLM model

## Setup (One-time)

### 1. Backend Setup
```bash
setup_backend.bat
```

Or manually:
```bash
cd backend
pip install -r requirements.txt
```

### 2. Frontend Setup
```bash
setup_frontend.bat
```

Or manually:
```bash
cd frontend
npm install
```

### 3. Configure Tesseract (if not in PATH)
Edit `backend/config.py` and set `TESSERACT_CMD` path.

### 4. (Optional) Setup LLM
- Download llama.cpp: https://github.com/ggerganov/llama.cpp
- Place `main.exe` in `backend/llama.cpp/`
- Download Mongolian LLM model (.gguf) to `backend/models/`

## Running the Application

### Option 1: Development Mode (Recommended)

**Terminal 1 - Backend:**
```bash
run_backend.bat
```
Or: `cd backend && python main.py`

**Terminal 2 - Frontend:**
```bash
run_frontend.bat
```
Or: `cd frontend && npm start`

**Terminal 3 - Electron:**
```bash
run_electron.bat
```
Or: `cd frontend && npm run electron-dev`

### Option 2: Production Build

1. Build React app:
```bash
cd frontend
npm run build
```

2. Package Electron app:
```bash
npm run electron-pack
```

Output: `frontend/dist/Office AI Helper Setup.exe`

## Usage

1. Open the application
2. Click "Файл сонгох" to upload PDF or image
3. Click "OCR + Засах" to process
4. View corrected text
5. Click "Word-д татах" to export

## Troubleshooting

### Tesseract not found
- Install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
- Add to PATH or set path in `backend/config.py`

### Poppler not found
- Download: https://github.com/oschwartz10612/poppler-windows/releases
- Add `bin/` folder to PATH

### Backend connection error
- Ensure backend is running on http://127.0.0.1:8000
- Check firewall settings

### LLM not working
- App will fall back to simple text cleanup if LLM unavailable
- Ensure llama.cpp executable is in `backend/llama.cpp/`
- Ensure model file is in `backend/models/`
