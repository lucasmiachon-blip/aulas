#!/usr/bin/env bash
# Hook 2 — PreToolUse: BLOCK all writes to evidence-db.md
#
# LIMITATION: PreToolUse does not expose agent_type — cannot verify identity of caller.
# Therefore: block ALL writes. Use /sync-evidence with user approval to edit.
# Blocking (exit 2 = block).

INPUT=$(cat 2>/dev/null || echo '{}')

FILE_PATH=$(node -e "
const d=JSON.parse(process.argv[1] || '{}');
console.log((d.tool_input||{}).file_path||'');
" "$INPUT" 2>/dev/null)

# Only apply to evidence-db.md
if [[ "$FILE_PATH" != *"evidence-db.md" ]]; then
    exit 0
fi

# Block
echo "BLOCKED: evidence-db.md só pode ser editado com aprovação do usuário. Use /sync-evidence e peça confirmação." >&2
exit 2
