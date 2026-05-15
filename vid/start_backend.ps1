# VID Local Backend Launcher (No Docker)
Write-Host "--------------------------------------------------" -ForegroundColor Cyan
Write-Host "   VID - Virtual Identification System (Backend)   " -ForegroundColor Cyan
Write-Host "--------------------------------------------------" -ForegroundColor Cyan

# -- Function to Setup Venv --
function Setup-Venv($path, $reqs) {
    if (!(Test-Path "$path/venv")) {
        Write-Host "[SETUP] Creating Venv for $path..." -ForegroundColor Yellow
        python -m venv "$path/venv"
        & "$path/venv/Scripts/python.exe" -m pip install --upgrade pip
        if ($reqs) { & "$path/venv/Scripts/pip.exe" install -r "$path/$reqs" }
        else { & "$path/venv/Scripts/pip.exe" install fastapi uvicorn pydantic }
    }
}

# Setup all services
Setup-Venv "backend/services/ums-service" "requirements.txt"
Setup-Venv "backend/services/academic-admin-service" ""
Setup-Venv "backend/gateway" "requirements.txt"

# -- Start Auth Service --
Write-Host "[AUTH] Launching Auth Service on port 8001..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend/services/ums-service; .\venv\Scripts\activate; uvicorn main:app --port 8001 --reload"

# -- Start Academic Service --
Write-Host "[ACADEMIC] Launching Academic Service on port 8002..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend/services/academic-admin-service; .\venv\Scripts\activate; uvicorn main:app --port 8002 --reload"

# -- Start Gateway --
Write-Host "[GATEWAY] Launching API Gateway on http://localhost:5000..." -ForegroundColor Green
cd backend/gateway
.\venv\Scripts\activate
python main.py
