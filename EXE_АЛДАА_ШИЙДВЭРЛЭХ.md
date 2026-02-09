# .exe Бэлтгэх Алдаа Шийдвэрлэх

## Алдаа: "Cannot create symbolic link"

Энэ алдаа нь code signing-ийн хэсэгт гарч байна. Windows дээр symbolic link үүсгэхэд admin эрх шаардлагатай.

## Шийдэл

### Арга 1: Code signing идэвхгүй болгох (Зөвлөмжтэй)

`package.json` файлд `"sign": false` нэмсэн. Одоо дахин оролдох:

```bash
cd frontend
npm run electron-pack
```

### Арга 2: Admin эрхтэйгээр ажиллуулах

PowerShell-ийг "Run as Administrator" гэж нээх:

1. PowerShell-ийг олох
2. Баруун товч дарах
3. "Run as Administrator" сонгох
4. Дараа нь:

```powershell
cd "d:\office AI helper\frontend"
npm run electron-pack
```

### Арга 3: Cache цэвэрлэх

```powershell
# Cache хавтас устгах
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\electron-builder\Cache\winCodeSign"

# Дахин оролдох
cd frontend
npm run electron-pack
```

## Одоогийн байдал

✅ `package.json` файлд `"sign": false` нэмсэн
✅ Code signing идэвхгүй болгосон

Одоо дахин оролдох:

```bash
cd frontend
npm run electron-pack
```

## Тэмдэглэл

- Code signing нь зөвхөн худалдаалах аппуудад шаардлагатай
- Development/Personal ашиглалтад шаардлагагүй
- Signing идэвхгүй болгосон тохиолдолд Windows Defender warning гарч болно (энэ нь хэвийн)
