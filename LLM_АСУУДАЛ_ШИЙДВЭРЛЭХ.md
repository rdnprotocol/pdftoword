# LLM Model Ашиглахгүй Байгаа Асуудлыг Шийдвэрлэх

## Асуудал

Model байгаа боловч ашиглахгүй байна.

## Шалгах

### 1. Model болон llama.cpp байгаа эсэхийг шалгах

```bash
cd backend
python check_llm.py
```

Энэ нь:
- ✅ Model байгаа эсэхийг харуулна
- ✅ llama.cpp байгаа эсэхийг харуулна

### 2. LLM тест хийх

```bash
cd backend
python test_llm.py
```

Энэ нь LLM зөв ажиллаж байгаа эсэхийг шалгана.

## Нийтлэг асуудлууд

### Асуудал 1: Model path буруу

**Шалгах:**
```python
from ai_fix import LLMCorrector
import os
c = LLMCorrector()
print(os.path.exists(c.model_path))
```

**Шийдэл:**
- `backend/models/mongolian.gguf` файл байгаа эсэхийг шалгах
- Хэрэв нэр өөр бол `config.py` дээр замыг өөрчлөх

### Асуудал 2: llama.cpp crash хийж байна

**Шалгах:**
```bash
cd backend\llama.cpp
.\llama-cli.exe --help
```

**Шийдэл:**
- llama-cli.exe зөв суулгагдсан эсэхийг шалгах
- Зарим хувилбарууд `main.exe` ашигладаг - нэрийг шалгах
- DLL файлууд байгаа эсэхийг шалгах (llama.dll, mtmd.dll гэх мэт)

### Асуудал 3: Model хэмжээ их байна

**Шалгах:**
- Model файлын хэмжээг шалгах
- RAM хангалттай эсэхийг шалгах

**Шийдэл:**
- Илүү жижиг quantized хувилбар ашиглах (Q4_K_M, Q8_0)

### Асуудал 4: Encoding алдаа

**Шалгах:**
- Backend лог дээр Unicode алдаа харагдаж байгаа эсэх

**Шийдэл:**
- Код дээр `errors='replace'` нэмсэн
- UTF-8 encoding ашиглаж байна

## Debug мэдээлэл

Backend лог дээр дараах мэдээлэл харагдана:

```
DEBUG: Model path: ...
DEBUG: Model exists: True/False
DEBUG: llama.cpp path: ...
DEBUG: llama.cpp exists: True/False
DEBUG: Using LLM: True/False
Using LLM for text correction...
Running LLM: ...
```

## Шийдэл

### 1. Backend дахин эхлүүлэх

```bash
cd backend
python main.py
```

### 2. Лог шалгах

Backend терминал дээр debug мэдээллийг харах:
- Model path
- llama.cpp path
- Using LLM: True/False
- LLM error messages

### 3. Хэрэв LLM ашиглахгүй бол:

1. **Model path шалгах:**
   - `backend/models/mongolian.gguf` байгаа эсэх
   - Нэрийг шалгах

2. **llama.cpp шалгах:**
   - `backend/llama.cpp/llama-cli.exe` байгаа эсэх
   - Ажиллуулах боломжтой эсэхийг шалгах

3. **Backend дахин эхлүүлэх**

## Тэмдэглэл

- LLM ашиглах нь удаан хугацаа шаардаж болно (хэдэн секунд)
- Model хэмжээ их байвал илүү удаан байна
- Хэрэв timeout гарвал `ai_fix.py` дээр timeout-ийг нэмэгдүүлэх

## Хэрэв бүх зүйл зөв боловч ашиглахгүй бол:

Backend лог-ийг шалгаж, алдааны мэдээллийг харах:
- `DEBUG:` мэдээлэл
- `LLM error:` мэдээлэл
- `Warning:` мэдээлэл
