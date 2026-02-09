"""
Test LLM functionality
"""
from ai_fix import LLMCorrector
import os

print("=" * 50)
print("LLM Test")
print("=" * 50)

corrector = LLMCorrector()

print(f"\n1. Model path: {corrector.model_path}")
print(f"   Exists: {os.path.exists(corrector.model_path)}")

print(f"\n2. llama.cpp path: {corrector.llama_cpp_path}")
print(f"   Exists: {os.path.exists(corrector.llama_cpp_path)}")

if os.path.exists(corrector.model_path) and os.path.exists(corrector.llama_cpp_path):
    print("\n3. Testing LLM correction...")
    test_text = "Тест бичвэр OCR алдаатай"
    try:
        result = corrector.correct_text(test_text)
        print(f"   Input: {test_text}")
        print(f"   Output: {result}")
        print(f"   Used LLM: {result != test_text}")
    except Exception as e:
        print(f"   ERROR: {e}")
        import traceback
        traceback.print_exc()
else:
    print("\n3. LLM not available - skipping test")

print("\n" + "=" * 50)
