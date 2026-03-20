#!/usr/bin/env bash
# Hook — TeammateIdle: Enforce quality gates before teammate stops
# If lint fails or build fails, force teammate to continue (exit 2).
# If no slide files changed, allow stop (exit 0).

INPUT=$(cat 2>/dev/null || echo '{}')

TEAMMATE=$(node -e "
const d=JSON.parse(process.argv[1] || '{}');
console.log(d.teammate_name||'unknown');
" "$INPUT" 2>/dev/null)

# Auto-detect aula from git branch
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
AULA=""
case "$BRANCH" in
  *cirrose*)     AULA="cirrose" ;;
  *metanalise*)  AULA="metanalise" ;;
  *grade*)       AULA="grade" ;;
  *osteo*)       AULA="osteoporose" ;;
  *)             exit 0 ;;  # On main or unknown branch, don't gate
esac

# Check if slide files were modified (staged or unstaged)
SLIDE_CHANGES=$(git diff --name-only HEAD 2>/dev/null | grep -c "aulas/$AULA/slides/" || echo "0")

# If no slide changes, teammate can stop
if [ "$SLIDE_CHANGES" -eq 0 ]; then
  exit 0
fi

# Run lint check
LINT_RESULT=$(npm run lint:slides 2>&1) || {
  echo "TeammateIdle gate: lint:slides FAIL — teammate must fix before stopping." >&2
  exit 2
}

# All gates passed
exit 0
