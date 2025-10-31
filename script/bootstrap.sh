#!/usr/bin/env bash
set -euo pipefail
if [ -d ".venv" ]; then
  echo "✅ Environment already exists, skipping setup."
  exit 0
fi
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.cargo/bin:$HOME/.local/bin:$PATH"
uv python install 3.12
uv venv .venv --python 3.12
. .venv/bin/activate
uv pip install -U pip
[ -f requirements.txt ] && uv pip install -r requirements.txt || true
echo "✅ Environment ready."
