if (Test-Path ".venv") {
  Write-Host "[OK] Environment already exists, skipping setup." -ForegroundColor Green
  Write-Host "[INFO] Open a new terminal or run: .\.venv\Scripts\Activate.ps1" -ForegroundColor Cyan
  exit 0
}
$ProgressPreference = 'SilentlyContinue'
Write-Host "[SETUP] Installing uv package manager..." -ForegroundColor Yellow
iwr https://astral.sh/uv/install.ps1 -useb | iex
$env:Path = "$env:USERPROFILE\.cargo\bin;$env:USERPROFILE\.local\bin;$env:Path"
Write-Host "[SETUP] Installing Python 3.12..." -ForegroundColor Yellow
uv python install 3.12
Write-Host "[SETUP] Creating virtual environment..." -ForegroundColor Yellow
uv venv .venv --python 3.12
Write-Host "[SETUP] Installing dependencies..." -ForegroundColor Yellow
. .\.venv\Scripts\Activate.ps1
uv pip install -U pip
if (Test-Path requirements.txt) { uv pip install -r requirements.txt }
Write-Host "[OK] Environment ready!" -ForegroundColor Green
Write-Host "[INFO] Open a new terminal and the Python environment will activate automatically." -ForegroundColor Cyan
