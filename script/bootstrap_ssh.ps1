#!/usr/bin/env bash
set -euo pipefail

# ---- settings ----
EMAIL="${EMAIL:-you@example.com}"              # set once: export EMAIL="you@domain.com"
KEY="${HOME}/.ssh/id_ed25519"
PUB="${KEY}.pub"
TITLE="$(hostname) - $(date +%Y-%m-%d)"

# ---- deps: gh + openssh ----
if ! command -v gh >/dev/null 2>&1; then
  echo "Installing GitHub CLI (gh) is required. See https://cli.github.com/"; exit 1
fi
if ! command -v ssh-keygen >/dev/null 2>&1; then
  echo "OpenSSH not found. Install openssh-client."; exit 1
fi

# ---- key generation (skip if exists) ----
if [ -f "$KEY" ]; then
  echo "Key already exists at $KEY — skipping generation."
else
  mkdir -p ~/.ssh && chmod 700 ~/.ssh
  ssh-keygen -t ed25519 -C "$EMAIL" -f "$KEY" -N ""
  echo "Generated key: $KEY"
fi

# ---- ssh-agent + add key ----
eval "$(ssh-agent -s)" >/dev/null
# macOS: also store passphrase in Keychain if you set one (we used empty passphrase above)
if [[ "$(uname)" == "Darwin" ]]; then
  /usr/bin/ssh-add --apple-use-keychain "$KEY"
else
  ssh-add "$KEY"
fi

# ---- ssh config hygiene ----
if ! grep -q "Host github.com" ~/.ssh/config 2>/dev/null; then
  cat >> ~/.ssh/config <<'EOF'
Host github.com
  HostName github.com
  User git
  AddKeysToAgent yes
  IdentityFile ~/.ssh/id_ed25519
EOF
  chmod 600 ~/.ssh/config
fi

# ---- login to GitHub (once) ----
if ! gh auth status >/dev/null 2>&1; then
  echo "Logging in to GitHub CLI…"
  gh auth login -s admin:public_key -w
fi

# ---- upload public key to GitHub (skip if already uploaded) ----
PUB_CONTENT="$(cat "$PUB")"
if gh ssh-key list --json title,key -q ".[] | select(.key==\"$PUB_CONTENT\")" | grep -q .; then
  echo "Public key already registered on GitHub."
else
  gh ssh-key add "$PUB" -t "$TITLE"
  echo "Uploaded public key to GitHub with title: $TITLE"
fi

# ---- test ----
ssh -T git@github.com || true
echo "✅ SSH key is ready and registered."
