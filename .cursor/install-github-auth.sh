#!/usr/bin/env bash
# Re-authorize gh/git against GitHub for Cloud Agents when a durable token is present.
# Cursor injects secrets as env vars. Prefer GITHUB_TOKEN; fall back to GH_TOKEN.
set -euo pipefail

TOKEN="${GITHUB_TOKEN:-${GH_TOKEN:-}}"

if [[ -z "$TOKEN" ]]; then
  # Already logged in from a previous interactive device login on this VM?
  if gh auth status -h github.com >/dev/null 2>&1; then
    echo "GitHub: using existing gh login on this machine."
    gh auth setup-git >/dev/null
    exit 0
  fi
  echo "GitHub: no GITHUB_TOKEN/GH_TOKEN secret and no existing gh login."
  echo "Add a GITHUB_TOKEN secret (repo write) in Cursor Cloud Agent secrets, or run: gh auth login"
  exit 0
fi

# Non-interactive login from the durable secret
printf '%s\n' "$TOKEN" | gh auth login --hostname github.com --with-token --git-protocol https --insecure-storage
gh auth setup-git
gh auth status -h github.com
echo "GitHub: authorized via secret for this agent run."
