# LLM (llama.cpp) Суулгах Заавар

## Таны одоогийн байдал

✅ llama.cpp файлуудыг татаж авсан байна (`llama-b7972-bin-win-cpu-x64` хавтас)

## Суулгах алхмууд

### Алхам 1: llama.cpp хавтас үүсгэх

`backend` хавтас дотор `llama.cpp` хавтас үүсгэх:

```bash
cd backend
mkdir llama.cpp
```

### Алхам 2: Executable файлыг хуулах

Таны татаж авсан хавтаснаас (`llama-b7972-bin-win-cpu-x64`) дараах файлуудын аль нэгийг хуулах:

**Сонголт 1: `llama-cli.exe` (Зөвлөмжтэй)**
- `llama-cli.exe` файлыг олох
- `backend/llama.cpp/llama-cli.exe` руу хуулах

**Сонголт 2: `main.exe` (хэрэв байвал)**
- `main.exe` файлыг олох
- `backend/llama.cpp/main.exe` руу хуулах

### Алхам 3: Шалгах

Файл зөв байрласан эсэхийг шалгах:

```bash
dir backend\llama.cpp
```

Дараах файлуудын аль нэг байх ёстой:
- `backend/llama.cpp/llama-cli.exe` ✅
- Эсвэл `backend/llama.cpp/main.exe` ✅

## Монгол LLM загвар (Сонголттой)

LLM загвар байхгүй бол програм энгийн текст цэвэрлэлт хийх болно.

Хэрэв LLM загвар суулгахыг хүсвэл:

1. Монгол хэл дэмжих LLM загвар олох (.gguf формат)
2. `backend/models/` хавтас руу хуулах
3. Жишээ нэр: `mongolian.gguf`

## Хурдан заавар (Copy-Paste)

**PowerShell дээр:**

```powershell
# 1. llama.cpp хавтас үүсгэх
New-Item -ItemType Directory -Force -Path "backend\llama.cpp"

# 2. llama-cli.exe-ийг хуулах (таны татаж авсан хавтасны замыг өөрчлөх)
Copy-Item "C:\Users\Таны_нэр\Downloads\llama-b7972-bin-win-cpu-x64\llama-cli.exe" -Destination "backend\llama.cpp\llama-cli.exe"
```

**Эсвэл Windows Explorer дээр:**
1. `backend` хавтас нээх
2. `llama.cpp` хавтас үүсгэх
3. Татаж авсан хавтаснаас `llama-cli.exe`-ийг хуулах
4. `backend/llama.cpp/` хавтас руу буулгах

## Шалгах

Суулгалт зөв болсон эсэхийг шалгах:

```bash
cd backend
python -c "from pathlib import Path; p = Path('llama.cpp/llama-cli.exe'); print('Exists:', p.exists())"
```

## Тэмдэглэл

- `llama-cli.exe` эсвэл `main.exe` аль нь байсан ч ажиллана
- Код нь хоёуланг нь хайх болно
- LLM загвар байхгүй бол програм ажиллахгүй гэсэн үг биш - энгийн цэвэрлэлт хийх болно
