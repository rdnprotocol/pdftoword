"""
LLM configuration check script
"""
import os
import sys
from pathlib import Path
from ai_fix import LLMCorrector

# Set UTF-8 encoding for output
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

print("=" * 50)
print("LLM Configuration Check")
print("=" * 50)
print()

# LLM corrector үүсгэх
corrector = LLMCorrector()

print(f"1. llama.cpp executable:")
print(f"   Зам: {corrector.llama_cpp_path}")
if os.path.exists(corrector.llama_cpp_path):
    print(f"   ✅ Байна: {corrector.llama_cpp_path}")
else:
    print(f"   ❌ Байхгүй: {corrector.llama_cpp_path}")
print()

print(f"2. LLM Model:")
print(f"   Зам: {corrector.model_path}")
if os.path.exists(corrector.model_path):
    file_size = os.path.getsize(corrector.model_path) / (1024 * 1024 * 1024)  # GB
    print(f"   ✅ Байна: {corrector.model_path}")
    print(f"   Хэмжээ: {file_size:.2f} GB")
else:
    print(f"   ❌ Байхгүй: {corrector.model_path}")
print()

# Шалгах
llama_exists = os.path.exists(corrector.llama_cpp_path)
model_exists = os.path.exists(corrector.model_path)

print("=" * 50)
if llama_exists and model_exists:
    print("[OK] LLM fully configured!")
    print("     OCR errors will be corrected using LLM.")
elif llama_exists:
    print("[WARNING] llama.cpp found, but LLM model missing.")
    print("          Program will use simple text cleanup.")
elif model_exists:
    print("[WARNING] LLM model found, but llama.cpp missing.")
    print("          Program will use simple text cleanup.")
else:
    print("[INFO] LLM not configured.")
    print("       Program will use simple text cleanup.")
    print()
    print("To install LLM: See LLM_SUULGAH_ZAAVAR.md file.")
print("=" * 50)
