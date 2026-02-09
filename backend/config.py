"""
Configuration file for Office AI Helper backend.
Set paths and settings here.
"""
import os
from pathlib import Path

# Tesseract path (set if not in PATH)
# Example: TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Poppler path (set if not in PATH)
# Example: POPPLER_PATH = r"C:\poppler\bin"
POPPLER_PATH = r"C:\poppler-25.12.0\Library\bin"

# LLM Model path
MODEL_PATH = Path(__file__).parent / "models" / "mongolian.gguf"

# llama.cpp executable path (can be main.exe or llama-cli.exe)
LLAMA_CPP_PATH = Path(__file__).parent / "llama.cpp" / "llama-cli.exe"


def configure_tesseract():
    """Configure pytesseract with custom path if needed."""
    if TESSERACT_CMD and os.path.exists(TESSERACT_CMD):
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD


def configure_poppler():
    """Configure pdf2image with poppler path if needed."""
    if POPPLER_PATH and os.path.exists(POPPLER_PATH):
        os.environ["PATH"] = str(POPPLER_PATH) + os.pathsep + os.environ.get("PATH", "")
