# LLM Crash Асуудлыг Шийдвэрлэх

## Асуудал

llama-cli.exe crash хийж байна (return code 3221225781). Энэ нь:
- DLL файлууд байхгүй байж магадгүй
- llama-cli.exe буруу хувилбар байж магадгүй
- Model файл эвдэрсэн байж магадгүй

## Шалгах

### 1. DLL файлууд байгаа эсэхийг шалгах

```powershell
cd "d:\office AI helper\backend\llama.cpp"
Get-ChildItem *.dll
```

Хэрэв DLL файлууд байхгүй бол:
- llama-cli.exe-тэй хамт байрлах DLL файлуудыг хуулах хэрэгтэй
- Эсвэл Visual C++ Redistributable суулгах хэрэгтэй

### 2. llama-cli.exe зөв ажиллаж байгаа эсэхийг шалгах

```powershell
cd "d:\office AI helper\backend\llama.cpp"
.\llama-cli.exe --help
```

Хэрэв crash хийвэл:
- llama-cli.exe буруу хувилбар байж магадгүй
- Дахин татаж авах хэрэгтэй

### 3. Model файл зөв эсэхийг шалгах

```powershell
cd "d:\office AI helper\backend\models"
Get-Item mongolian.gguf | Select-Object Name, Length
```

Model файлын хэмжээ ойролцоогоор 3.27 GB байх ёстой.

## Шийдэл

### Сонголт 1: DLL файлуудыг хуулах

1. llama-cli.exe-ийг татаж авсан хавтсаас бүх DLL файлуудыг олох
2. `backend/llama.cpp/` хавтас руу хуулах
3. Дахин тест хийх

### Сонголт 2: Visual C++ Redistributable суулгах

1. Microsoft Visual C++ Redistributable татаж авах:
   - https://aka.ms/vs/17/release/vc_redist.x64.exe
2. Суулгах
3. Дахин тест хийх

### Сонголт 3: llama-cli.exe дахин татаж авах

1. llama.cpp-ийн албан ёсны вэбсайтаас дахин татаж авах
2. `backend/llama.cpp/` хавтас руу хуулах
3. Дахин тест хийх

### Сонголт 4: main.exe ашиглах

Хэрэв `main.exe` байвал:
1. `backend/llama.cpp/main.exe` руу хуулах
2. `config.py` дээр замыг өөрчлөх

## Одоогийн байдал

✅ Model байна: `D:\office AI helper\backend\models\mongolian.gguf` (3.27 GB)  
✅ llama-cli.exe байна: `D:\office AI helper\backend\llama.cpp\llama-cli.exe`  
❌ llama-cli.exe crash хийж байна

## Тэмдэглэл

- Одоогоор програм энгийн текст цэвэрлэлт ашиглаж байна
- LLM ашиглахгүй байгаа тул OCR алдаа засах чадвар хязгаарлагдмал
- DLL асуудлыг шийдсэний дараа LLM ажиллах болно

## Тест хийх

```bash
cd backend
python test_llm_direct.py
```

Хэрэв LLM ажиллаж байвал:
- "LLM correction successful" гэж харагдана
- Output текст өөрчлөгдөнө

Хэрэв ажиллахгүй байвал:
- "LLM error" гэж харагдана
- Return code 3221225781 гэж харагдана
