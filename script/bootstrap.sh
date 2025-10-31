#!/usr/bin/env bash
set -euo pipefail
if [ -d ".venv" ]; then
  echo "[OK] Environment already exists, skipping setup."
  echo "[INFO] Open a new terminal or run: source .venv/bin/activate"
  exit 0
fi
echo "[SETUP] Installing uv package manager..."
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.cargo/bin:$HOME/.local/bin:$PATH"
echo "[SETUP] Installing Python 3.12..."
uv python install 3.12
echo "[SETUP] Creating virtual environment..."
uv venv .venv --python 3.12
echo "[SETUP] Installing dependencies..."
. .venv/bin/activate
uv pip install -U pip
[ -f requirements.txt ] && uv pip install -r requirements.txt || true
echo "[OK] Environment ready!"
echo "[INFO] Open a new terminal and the Python environment will activate automatically."
