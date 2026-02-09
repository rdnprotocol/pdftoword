# Virtual Environment Заавар

## Virtual Environment гэж юу вэ?

Virtual environment нь Python packages-уудыг тусдаа байрлуулах хавтас юм. Энэ нь системийн Python-оос тусдаа байдаг.

## Одоогийн байдал

✅ Virtual environment (`.venv`) байна  
✅ Dependencies суулгагдсан

## Ашиглах

### Арга 1: Автомат (Зөвлөмжтэй)

**`run_backend.bat`** файлыг ажиллуулах - автоматаар virtual environment ашиглана.

### Арга 2: Гараар

**PowerShell дээр:**
```powershell
# Virtual environment идэвхжүүлэх
.venv\Scripts\Activate.ps1

# Backend ажиллуулах
cd backend
python main.py
```

**CMD дээр:**
```cmd
.venv\Scripts\activate.bat
cd backend
python main.py
```

## Тэмдэглэл

- Virtual environment идэвхжүүлсний дараа `(.venv)` гэж терминал дээр харагдана
- Dependencies аль хэдийн суулгагдсан
- Хэрэв virtual environment байхгүй бол системийн Python ашиглана

## Асуудал гарвал

### "Activate.ps1 cannot be loaded"

PowerShell дээр execution policy тохируулах:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### "No module named 'fastapi'"

Virtual environment идэвхжүүлээгүй байна:
```powershell
.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
```
