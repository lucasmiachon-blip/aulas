#!/usr/bin/env bash
# P0: Audit Trail — logs tool calls to daily JSONL
# WT-aware: detects if running inside a git worktree
# Pure bash — no node/jq dependency
# Output: ~/.claude/session-logs/YYYY-MM-DD.jsonl

set -euo pipefail

INPUT=$(cat 2>/dev/null || echo '{}')

DIR="$HOME/.claude/session-logs"
mkdir -p "$DIR"
LOGFILE="$DIR/$(date +%Y-%m-%d).jsonl"

# Single git call: line 1 = branch, line 2 = git-dir
GIT_INFO=$(git rev-parse --abbrev-ref HEAD --git-dir 2>/dev/null || true)
BRANCH="${GIT_INFO%%$'\n'*}"
GIT_DIR="${GIT_INFO##*$'\n'}"
BRANCH=${BRANCH:-detached}

# Detect worktree from git-dir path
WORKTREE=""
if [[ "${GIT_DIR:-}" == *worktrees* ]]; then
  _tmp="${GIT_DIR%%/.git/worktrees/*}"
  WORKTREE="${_tmp##*/}"
fi

# Extract JSON string value (pure bash regex — no grep/sed)
jv() {
  local re="\"$1\":\"([^\"]*)\""
  if [[ "$INPUT" =~ $re ]]; then
    printf '%s' "${BASH_REMATCH[1]}"
  fi
}

TOOL=$(jv tool_name);    TOOL=${TOOL:-unknown}
SESSION=$(jv session_id); SESSION=${SESSION:-no-session}

# Detail priority: query > prompt > command > file_path > pattern > skill > ?
DETAIL=$(jv file_path)
[[ -z "$DETAIL" ]] && DETAIL=$(jv pattern)
[[ -z "$DETAIL" ]] && DETAIL=$(jv skill)
DETAIL=${DETAIL:-?}

CMD=$(jv command)
if [[ -n "$CMD" ]]; then
  DETAIL="${CMD%%\\n*}"; DETAIL="${DETAIL:0:120}"
fi
_p=$(jv prompt);  [[ -n "$_p" ]] && DETAIL="${_p:0:80}"
_q=$(jv query);   [[ -n "$_q" ]] && DETAIL="${_q:0:80}"

# JSON-escape: \ → \\, " → \"
esc() { local s="${1//\\/\\\\}"; printf '%s' "${s//\"/\\\"}"; }

TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# Build JSONL entry
LINE=$(printf '{"ts":"%s","tool":"%s","session":"%s","detail":"%s","cwd":"%s","branch":"%s"' \
  "$TS" "$(esc "$TOOL")" "$(esc "$SESSION")" "$(esc "$DETAIL")" "$(esc "$PWD")" "$(esc "$BRANCH")")

if [[ -n "$WORKTREE" ]]; then
  LINE+=$(printf ',"worktree":"%s"' "$(esc "$WORKTREE")")
else
  LINE+=',"worktree":null'
fi

# duration_ms (number — no escaping needed)
_dur_re='"duration_ms":([0-9]+)'
[[ "$INPUT" =~ $_dur_re ]] && LINE+=$(printf ',"duration_ms":%s' "${BASH_REMATCH[1]}")

LINE+='}'
echo "$LINE" >> "$LOGFILE" 2>/dev/null

exit 0
