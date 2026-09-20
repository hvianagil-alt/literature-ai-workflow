#!/usr/bin/env bash
# Cloud Agent install for literature-ai-workflow.
# Idempotent. No required secrets. Soft-configures GitHub auth when a token is present.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "==> Literature AI install"

# Optional helper needs system Python only (stdlib).
if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 is required for scripts/list_papers.py" >&2
  exit 1
fi
python3 --version

# Soft GitHub auth: never fail install if missing (user may skip the secret).
TOKEN="${GITHUB_TOKEN:-${GH_TOKEN:-}}"
if [[ -n "$TOKEN" ]]; then
  if command -v gh >/dev/null 2>&1; then
    printf '%s\n' "$TOKEN" | gh auth login --hostname github.com --with-token --git-protocol https --insecure-storage >/dev/null
    gh auth setup-git >/dev/null
    echo "GitHub: authorized via GITHUB_TOKEN/GH_TOKEN secret."
  else
    echo "GitHub: token present but gh CLI not found; skipping auth."
  fi
elif command -v gh >/dev/null 2>&1 && gh auth status -h github.com >/dev/null 2>&1; then
  gh auth setup-git >/dev/null || true
  echo "GitHub: using existing gh login on this machine."
else
  echo "GitHub: no token and no existing login (optional — push/PR needs auth)."
fi

# Smoke the optional helper (no papers expected on a fresh clone).
python3 scripts/list_papers.py
python3 -m unittest discover -s tests -q

# Confirm skill/agent layout is present (workflow surface).
test -f AGENTS.md
test -f .cursor/agents/literature-review.md
test -f .cursor/agents/literature-critic.md
test -f .cursor/skills/first-conversation/SKILL.md
test -f .cursor/skills/review-harness/SKILL.md
test -f review/memory/index.md
test -f scripts/check_harness.py
test -f .cursor/skills/paper-extraction/SKILL.md
test -f .cursor/skills/literature-table/SKILL.md
test -f .cursor/skills/report-writing/SKILL.md
test -f .cursor/skills/related-paper-exploration/SKILL.md
test -f .cursor/skills/bib-import/SKILL.md
test -f .cursor/skills/oa-fetch/SKILL.md
test -f .cursor/skills/prisma-logging/SKILL.md
test -f examples/literature-table.md
test -f examples/sample-report.md
test -d papers
test -d review/notes

echo "==> Install OK"
