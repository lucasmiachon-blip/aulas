#!/usr/bin/env bash
# Hook — TaskCompleted: Validate task completion criteria
# Blocks task completion (exit 2) if uncommitted slide changes exist.
# Logs completion to audit trail.

INPUT=$(cat 2>/dev/null || echo '{}')

TASK_ID=$(node -e "
const d=JSON.parse(process.argv[1] || '{}');
console.log(d.task_id||'?');
" "$INPUT" 2>/dev/null)

TASK_SUBJECT=$(node -e "
const d=JSON.parse(process.argv[1] || '{}');
console.log((d.task_subject||'').slice(0,100));
" "$INPUT" 2>/dev/null)

# Check for uncommitted changes in slide files
UNCOMMITTED=$(git diff --name-only 2>/dev/null | grep "aulas/.*/slides/" || true)
STAGED=$(git diff --cached --name-only 2>/dev/null | grep "aulas/.*/slides/" || true)

if [ -n "$UNCOMMITTED" ] || [ -n "$STAGED" ]; then
  echo "TaskCompleted gate: uncommitted slide changes detected. Commit before marking task done." >&2
  echo "  Uncommitted: $UNCOMMITTED $STAGED" >&2
  exit 2
fi

# Log completion
DATE=$(date '+%Y-%m-%d %H:%M')
LOG_DIR="$HOME/.claude/session-logs"
mkdir -p "$LOG_DIR" 2>/dev/null
echo "{\"ts\":\"$DATE\",\"event\":\"task_completed\",\"task_id\":\"$TASK_ID\",\"subject\":\"$TASK_SUBJECT\"}" >> "$LOG_DIR/$(date '+%Y-%m-%d').jsonl" 2>/dev/null

exit 0
