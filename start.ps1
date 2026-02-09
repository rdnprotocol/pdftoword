# Office AI Helper - PowerShell скрипт
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Office AI Helper - Програмыг асаах" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Frontend суулгаагүй бол суулгах
if (-not (Test-Path "frontend\node_modules")) {
    Write-Host "Frontend суулгаагүй байна. Суулгаж байна..." -ForegroundColor Yellow
    Set-Location frontend
    npm install
    if ($LASTEXITCODE -ne 0) {
        Write-Host "АЛДАА: Frontend суулгахад алдаа гарлаа!" -ForegroundColor Red
        Set-Location ..
        pause
        exit 1
    }
    Set-Location ..
    Write-Host "Frontend суулгагдсан!" -ForegroundColor Green
    Write-Host ""
}

Write-Host "Backend эхлүүлж байна..." -ForegroundColor Green
Start-Process cmd -ArgumentList "/k", "cd /d `"$PWD\backend`" && python main.py" -WindowStyle Normal

Start-Sleep -Seconds 3

Write-Host "Frontend эхлүүлж байна..." -ForegroundColor Green
Start-Process cmd -ArgumentList "/k", "cd /d `"$PWD\frontend`" && npm start" -WindowStyle Normal

Start-Sleep -Seconds 8

Write-Host "Electron эхлүүлж байна..." -ForegroundColor Green
Start-Process cmd -ArgumentList "/k", "cd /d `"$PWD\frontend`" && npm run electron-dev" -WindowStyle Normal

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Бүх сервис эхлүүлсэн!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Гурван цонх нээгдсэн:" -ForegroundColor Yellow
Write-Host "- Backend (http://127.0.0.1:8000)" -ForegroundColor White
Write-Host "- Frontend (http://localhost:3000)" -ForegroundColor White
Write-Host "- Electron (Desktop app)" -ForegroundColor White
Write-Host ""
Write-Host "Програмыг хаахдаа бүх цонхыг хаана уу." -ForegroundColor Yellow
Write-Host ""
