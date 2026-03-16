#!/usr/bin/env bash
# Pre-commit: (1) guard Classe C on main, (2) guard shared/ on WTs,
#             (3) slide-count regression gate, (4) lint on change.
# Called by .git/hooks/pre-commit. Versionado no repo.
set -e

BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")

# ── Guard 1: Classe C content blocked on main ──
# Slides, CSS, JS, references = content. Must go through worktree branches.
# Bypass: ALLOW_MAIN_CONTENT=1 git commit (emergency only)
if [ "$BRANCH" = "main" ] && [ -z "$ALLOW_MAIN_CONTENT" ]; then
  CLASSE_C=$(git diff --cached --name-only | grep -E '^aulas/.*/slides/|^aulas/.*\.(css|js)$|^aulas/.*/references/' || true)
  if [ -n "$CLASSE_C" ]; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║  BLOQUEADO: Classe C (conteúdo) em main                 ║"
    echo "║  Slides, CSS, JS e references devem ir pela worktree.   ║"
    echo "║  Bypass emergencial: ALLOW_MAIN_CONTENT=1 git commit    ║"
    echo "╚══════════════════════════════════════════════════════════╝"
    echo ""
    echo "Arquivos bloqueados:"
    echo "$CLASSE_C" | sed 's/^/  → /'
    echo ""
    exit 1
  fi
fi

# ── Guard 2: shared/ is READ-ONLY on feature branches ──
# Only main can edit shared/. WTs must defer changes to main session.
# Bypass: ALLOW_SHARED_EDIT=1 git commit (emergency only)
if [ "$BRANCH" != "main" ] && [ -z "$ALLOW_SHARED_EDIT" ]; then
  SHARED_EDITS=$(git diff --cached --name-only | grep -E '^shared/' || true)
  if [ -n "$SHARED_EDITS" ]; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║  BLOQUEADO: shared/ é READ-ONLY em worktrees            ║"
    echo "║  Edições em shared/ devem ir pelo branch main.          ║"
    echo "║  Bypass emergencial: ALLOW_SHARED_EDIT=1 git commit     ║"
    echo "╚══════════════════════════════════════════════════════════╝"
    echo ""
    echo "Arquivos bloqueados:"
    echo "$SHARED_EDITS" | sed 's/^/  → /'
    echo ""
    exit 1
  fi
fi

# ── Guard 3: Slide-count regression gate ──
# After merges, verify slide count didn't decrease. Catches silent rollbacks.
# Each aula declares expected count in _manifest.js (grep for 'id:' entries).
if [ "$BRANCH" != "main" ]; then
  AULA=""
  case "$BRANCH" in
    *cirrose*)     AULA="cirrose" ;;
    *metanalise*)  AULA="metanalise" ;;
    *grade*)       AULA="grade" ;;
    *osteoporose*) AULA="osteoporose" ;;
  esac

  if [ -n "$AULA" ]; then
    MANIFEST="aulas/$AULA/slides/_manifest.js"
    if [ -f "$MANIFEST" ]; then
      EXPECTED=$(grep -c "id:" "$MANIFEST" 2>/dev/null || echo "0")
      SLIDE_DIR="aulas/$AULA/slides"
      ACTUAL=$(find "$SLIDE_DIR" -name '*.html' -not -name '_*' 2>/dev/null | wc -l | tr -d ' ')

      if [ "$ACTUAL" -lt "$EXPECTED" ]; then
        echo ""
        echo "╔══════════════════════════════════════════════════════════╗"
        echo "║  ALERTA: Possível rollback de slides!                   ║"
        echo "║  Slides em disco ($ACTUAL) < manifest ($EXPECTED).      ║"
        echo "║  Verifique se um merge não sobrescreveu slides.         ║"
        echo "╚══════════════════════════════════════════════════════════╝"
        echo ""
        echo "  Aula: $AULA"
        echo "  Manifest espera: $EXPECTED slides"
        echo "  Em disco: $ACTUAL slides"
        echo ""
        echo "  Se intencional: ALLOW_SLIDE_LOSS=1 git commit"
        if [ -z "$ALLOW_SLIDE_LOSS" ]; then
          exit 1
        fi
      fi
    fi
  fi
fi

# ── Lints ──
SLIDES_CHANGED=$(git diff --cached --name-only | grep -E 'aulas/.*/slides/.*\.html$' || true)
CASE_OR_MANIFEST=$(git diff --cached --name-only | grep -E '(CASE\.md|_manifest\.js)$' || true)

if [ -n "$SLIDES_CHANGED" ]; then
  echo "→ lint:slides (slides modificados detectados)..."
  npm run lint:slides
fi

if [ -n "$CASE_OR_MANIFEST" ]; then
  echo "→ lint:case-sync (CASE.md ou _manifest.js modificados)..."
  npm run lint:case-sync
fi
