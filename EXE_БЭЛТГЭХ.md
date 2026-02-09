# .exe Файл Бэлтгэх Заавар

## Алхмууд

### 1. React аппыг бэлтгэх

```bash
cd frontend
npm run build
```

Энэ нь `frontend/build/` хавтас үүсгэнэ.

### 2. Electron аппыг багцлах

```bash
cd frontend
npm run electron-pack
```

Эсвэл:

```bash
cd frontend
npm run build
npm run electron-pack
```

### 3. Гаралт

Багцлагдсан файлууд `frontend/dist/` хавтасанд байна:

- **NSIS Installer:** `Office AI Helper Setup X.X.X.exe` (суулгах файл)
- **Portable:** `Office AI Helper X.X.X.exe` (шууд ажиллуулах файл)

## Бүгдийг нэг дор

```bash
cd frontend
npm run electron-pack
```

Энэ нь автоматаар:
1. React аппыг бэлтгэнэ (`npm run build`)
2. Electron аппыг багцлана (`electron-builder`)

## Шалгах

Багцлагдсан файлыг шалгах:

1. `frontend/dist/` хавтас руу орох
2. `Office AI Helper Setup X.X.X.exe` файлыг олох
3. Давхар дарах (double-click)
4. Суулгах
5. Програмыг ажиллуулах

## Тэмдэглэл

- Багцлах хэдэн минут шаардаж болно
- Эхний удаа удаан байж болно (dependencies татаж авах)
- Backend нь `resources/backend/` хавтасанд байна
- Python суулгагдсан байх ёстой (хэрэглэгчийн системд)

## Асуудал гарвал

### "electron-builder not found"
```bash
cd frontend
npm install electron-builder --save-dev
```

### "Build failed"
- Node.js хувилбар шалгах (16+ байх ёстой)
- `npm install` дахин ажиллуулах
- `frontend/build/` хавтас байгаа эсэхийг шалгах

### Backend ажиллахгүй
- Python суулгагдсан эсэхийг шалгах
- Tesseract болон Poppler суулгагдсан эсэхийг шалгах
- Backend dependencies суулгагдсан эсэхийг шалгах

## Хурдан заавар

```bash
# 1. Frontend хавтас руу орох
cd frontend

# 2. Багцлах
npm run electron-pack

# 3. Гаралт: frontend/dist/Office AI Helper Setup X.X.X.exe
```
