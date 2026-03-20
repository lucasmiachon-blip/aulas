#!/usr/bin/env bash
# Hook 2 — PreToolUse: Warn when any agent writes evidence-db.md
#
# LIMITATION: PreToolUse does not expose agent_type — cannot verify identity of caller.
# Workaround: always emit warning. reference-manager knows to expect it.
# Non-blocking (exit 0 + JSON systemMessage).

INPUT=$(cat 2>/dev/null || echo '{}')

FILE_PATH=$(node -e "
const d=JSON.parse(process.argv[1] || '{}');
console.log((d.tool_input||{}).file_path||'');
" "$INPUT" 2>/dev/null)

# Only apply to evidence-db.md
if [[ "$FILE_PATH" != *"evidence-db.md" ]]; then
    exit 0
fi

# Non-blocking warn
printf '{"systemMessage": "\u26a0 evidence-db.md s\u00f3 deve ser editado por reference-manager. Confirme antes de prosseguir."}\n'
exit 0
