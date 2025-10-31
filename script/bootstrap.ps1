if (Test-Path ".venv") {
  Write-Host "✅ Environment already exists, skipping setup."
  Write-Host "ℹ️  Open a new terminal or run: .\.venv\Scripts\Activate.ps1"
  exit 0
}
$ProgressPreference = 'SilentlyContinue'
Write-Host "📦 Installing uv package manager..."
iwr https://astral.sh/uv/install.ps1 -useb | iex
$env:Path = "$env:USERPROFILE\.cargo\bin;$env:USERPROFILE\.local\bin;$env:Path"
Write-Host "🐍 Installing Python 3.12..."
uv python install 3.12
Write-Host "📁 Creating virtual environment..."
uv venv .venv --python 3.12
Write-Host "📦 Installing dependencies..."
. .\.venv\Scripts\Activate.ps1
uv pip install -U pip
if (Test-Path requirements.txt) { uv pip install -r requirements.txt }
Write-Host "✅ Environment ready!"
Write-Host "ℹ️  Open a new terminal and the Python environment will activate automatically."
