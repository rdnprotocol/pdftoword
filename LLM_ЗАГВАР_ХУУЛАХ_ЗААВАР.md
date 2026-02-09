# LLM Загварыг Хуулах Заавар

## LLM загвар гэж юу вэ?

LLM (Large Language Model) загвар нь OCR-ийн алдааг автоматаар засах, албан ёсны оффис хэлбэрт шилжүүлэхэд ашиглана.

## LLM загвар байхгүй бол?

**Асуудалгүй!** Програм ажиллахгүй гэсэн үг биш. Энгийн текст цэвэрлэлт хийх болно:
- Хэт их зайг арилгах
- Мөрүүдийг цэвэрлэх
- Үндсэн форматлах

## LLM загварыг хаана хуулах вэ?

### Development (Хөгжүүлэлт) горимд:

**Хавтас:** `backend/models/`

**Жишээ:**
```
d:\office AI helper\
└── backend\
    └── models\
        └── mongolian.gguf  ← Энд хуулах
```

### Production (Суулгасан) апп дээр:

**Хавтас:** Суулгасан апп-ийн `resources/backend/models/`

**Жишээ:**
```
C:\Program Files\PDF to Word\
└── resources\
    └── backend\
        └── models\
            └── mongolian.gguf  ← Энд хуулах
```

**Эсвэл Portable хувилбар:**
```
PDF to Word X.X.X.exe (файл байгаа хавтас)\
└── resources\
    └── backend\
        └── models\
            └── mongolian.gguf  ← Энд хуулах
```

## Алхмууд

### Development горимд:

1. **`backend/models/` хавтас руу орох**
   ```bash
   cd backend\models
   ```

2. **LLM загварыг хуулах**
   - Татаж авсан `.gguf` файлыг хуулах
   - Нэрийг `mongolian.gguf` болгох (эсвэл `config.py` дээр замыг өөрчлөх)

3. **Шалгах**
   ```bash
   cd backend
   python check_llm.py
   ```

### Production апп дээр:

#### Арга 1: NSIS Installer (Суулгасан)

1. **Аппыг суулгах** (хэрэв суулгаагүй бол)
   - `PDF to Word Setup X.X.X.exe` ажиллуулах
   - Суулгах (жишээ: `C:\Program Files\PDF to Word`)

2. **Models хавтас олох**
   - Суулгасан хавтас руу орох
   - `resources\backend\models\` хавтас олох

3. **LLM загварыг хуулах**
   - `.gguf` файлыг `resources\backend\models\` хавтас руу хуулах
   - Нэрийг `mongolian.gguf` болгох

4. **Аппыг дахин эхлүүлэх**

#### Арга 2: Portable хувилбар

1. **Portable файлын байршлыг олох**
   - `PDF to Word X.X.X.exe` файл байгаа хавтас

2. **Models хавтас үүсгэх**
   ```
   PDF to Word X.X.X.exe (файл байгаа хавтас)\
   └── resources\
       └── backend\
           └── models\  ← Энэ хавтас үүсгэх
   ```

3. **LLM загварыг хуулах**
   - `.gguf` файлыг `models\` хавтас руу хуулах
   - Нэрийг `mongolian.gguf` болгох

4. **Аппыг дахин эхлүүлэх**

## Windows Explorer дээр:

### Development:

1. `backend` хавтас нээх
2. `models` хавтас нээх (хэрэв байхгүй бол үүсгэх)
3. LLM загварыг (`mongolian.gguf`) хуулах

### Production:

1. Суулгасан апп-ийн хавтас олох:
   - `C:\Program Files\PDF to Word\` (эсвэл суулгасан газар)
2. `resources\backend\models\` хавтас руу орох
3. LLM загварыг хуулах

## PowerShell командууд:

### Development:

```powershell
# Models хавтас үүсгэх (хэрэв байхгүй бол)
New-Item -ItemType Directory -Force -Path "backend\models"

# LLM загварыг хуулах (таны замыг өөрчлөх)
Copy-Item "C:\Users\Таны_нэр\Downloads\mongolian.gguf" -Destination "backend\models\mongolian.gguf"
```

### Production:

```powershell
# Models хавтас үүсгэх
$appPath = "C:\Program Files\PDF to Word"
New-Item -ItemType Directory -Force -Path "$appPath\resources\backend\models"

# LLM загварыг хуулах
Copy-Item "C:\Users\Таны_нэр\Downloads\mongolian.gguf" -Destination "$appPath\resources\backend\models\mongolian.gguf"
```

## Шалгах

LLM загвар зөв байрласан эсэхийг шалгах:

### Development:

```bash
cd backend
python check_llm.py
```

### Production:

Аппыг эхлүүлээд UI дээр LLM статусыг шалгах:
- ✅ **LLM загвар бэлэн байна** (ногоон) - зөв байрласан
- ℹ️ **Энгийн текст цэвэрлэлт ашиглана** (шар) - LLM байхгүй эсвэл буруу байрласан

## Тэмдэглэл

- **Файлын нэр:** `mongolian.gguf` (эсвэл `config.py` дээр замыг өөрчлөх)
- **Хавтас:** `backend/models/` (development) эсвэл `resources/backend/models/` (production)
- **Хэмжээ:** LLM загварууд их хэмжээтэй байдаг (GB-аар)
- **Формат:** `.gguf` форматтай байх ёстой

## Асуудал гарвал

### LLM олдсонгүй гэж гарвал:

1. Файлын нэрийг шалгах (`mongolian.gguf`)
2. Хавтасын замыг шалгах (`models/`)
3. Файл зөв хуулагдсан эсэхийг шалгах
4. Аппыг дахин эхлүүлэх

### Хавтас олохгүй байвал:

**Development:**
- `backend/models/` хавтас үүсгэх

**Production:**
- Суулгасан апп-ийн `resources/backend/models/` хавтас үүсгэх

## Дүгнэлт

**Development:** `backend/models/mongolian.gguf`  
**Production:** `resources/backend/models/mongolian.gguf` (суулгасан апп-ийн дотор)

LLM загвар байхгүй бол програм ажиллахгүй гэсэн үг биш - энгийн текст цэвэрлэлт хийх болно.
