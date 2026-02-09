"""
Direct LLM test with simple text
"""
import sys
import os

# Set UTF-8 encoding for output
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

from ai_fix import LLMCorrector

print("=" * 60)
print("LLM Direct Test")
print("=" * 60)

corrector = LLMCorrector()

print(f"\n1. Model: {corrector.model_path}")
print(f"   Exists: {os.path.exists(corrector.model_path)}")

print(f"\n2. llama.cpp: {corrector.llama_cpp_path}")
print(f"   Exists: {os.path.exists(corrector.llama_cpp_path)}")

if os.path.exists(corrector.model_path) and os.path.exists(corrector.llama_cpp_path):
    print("\n3. Testing with simple text...")
    test_text = "Test OCR text with errors"
    
    print(f"\n   Input: {test_text}")
    print("   Calling correct_text()...")
    
    try:
        result = corrector.correct_text(test_text)
        print(f"\n   Output: {result}")
        print(f"   Changed: {result != test_text}")
        
        if result == test_text:
            print("\n   ⚠️  WARNING: LLM returned original text!")
            print("   This means LLM might not be working correctly.")
    except Exception as e:
        print(f"\n   ❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
else:
    print("\n3. ❌ LLM not available - cannot test")

print("\n" + "=" * 60)
