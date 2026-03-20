#!/usr/bin/env bash
# Hook 4 — SubagentStop: Append 1-line summary to NOTES.md for every subagent that completes.
# Format: [DATA] [AGENT:id] — concluído. Status: [PASS/FAIL/PARTIAL]

INPUT=$(cat 2>/dev/null || echo '{}')

AGENT_TYPE=$(node -e "
const d=JSON.parse(process.argv[1] || '{}');
console.log(d.agent_type||'unknown');
" "$INPUT" 2>/dev/null)

AGENT_ID=$(node -e "
const d=JSON.parse(process.argv[1] || '{}');
console.log((d.agent_id||'?').slice(0,8));
" "$INPUT" 2>/dev/null)

LAST_MSG=$(node -e "
const d=JSON.parse(process.argv[1] || '{}');
console.log((d.last_assistant_message||'').slice(0,300));
" "$INPUT" 2>/dev/null)

CWD=$(node -e "
const d=JSON.parse(process.argv[1] || '{}');
console.log(d.cwd||'.');
" "$INPUT" 2>/dev/null)

DATE=$(date '+%Y-%m-%d %H:%M')
BRANCH=$(git branch --show-current 2>/dev/null)
AULA=""
case "$BRANCH" in
  *cirrose*)     AULA="cirrose" ;;
  *metanalise*)  AULA="metanalise" ;;
  *grade*)       AULA="grade" ;;
  *osteo*)       AULA="osteoporose" ;;
  *)             AULA="unknown" ;;
esac
NOTES="$CWD/aulas/$AULA/NOTES.md"

# Infer status from last message content
LOWER_MSG=$(echo "$LAST_MSG" | tr '[:upper:]' '[:lower:]')
STATUS="PARTIAL"
if echo "$LOWER_MSG" | grep -qE "fail|erro|error|cannot|unable|not found|exception"; then
    STATUS="FAIL"
elif echo "$LOWER_MSG" | grep -qE "complet|done|finish|ok\b|pass|succes|conclu"; then
    STATUS="PASS"
fi

# Create NOTES.md if it doesn't exist
if [ ! -f "$NOTES" ]; then
    printf "# NOTES — %s\n\n" "$AULA" > "$NOTES"
fi

printf "\n[%s] [%s:%s] — concluído. Status: %s\n" "$DATE" "$AGENT_TYPE" "$AGENT_ID" "$STATUS" >> "$NOTES"

exit 0
