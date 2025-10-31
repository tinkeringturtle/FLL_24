if (Test-Path ".venv") {
  Write-Host "✅ Environment already exists, skipping setup."
  exit 0
}
$ProgressPreference = 'SilentlyContinue'
iwr https://astral.sh/uv/install.ps1 -useb | iex
$env:Path = "$env:USERPROFILE\.cargo\bin;$env:USERPROFILE\.local\bin;$env:Path"
uv python install 3.12
uv venv .venv --python 3.12
. .\.venv\Scripts\Activate.ps1
uv pip install -U pip
if (Test-Path requirements.txt) { uv pip install -r requirements.txt }
Write-Host "✅ Environment ready."
