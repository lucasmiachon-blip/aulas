#!/usr/bin/env bash
# Pre-commit: (1) guard Classe C on main, (2) guard shared/ on WTs,
#             (3) slide-count regression gate, (4) slide integrity,
#             (5) guard Classe A/B on WTs, then lint on change.
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

# ── Guard 4: Slide integrity — build must run after content changes ──
# If slide HTMLs changed but .slide-integrity didn't, the build was skipped.
# This catches cases where a merge changed slides but nobody ran build:cirrose.
if [ "$BRANCH" != "main" ]; then
  SLIDES_STAGED=$(git diff --cached --name-only | grep -E 'aulas/.*/slides/.*\.html$' || true)
  INTEGRITY_STAGED=$(git diff --cached --name-only | grep -E '\.slide-integrity$' || true)

  if [ -n "$SLIDES_STAGED" ] && [ -z "$INTEGRITY_STAGED" ]; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║  AVISO: Slides mudaram mas build nao rodou!             ║"
    echo "║  Rode 'npm run build:cirrose' para atualizar            ║"
    echo "║  o fingerprint .slide-integrity.                        ║"
    echo "║  Bypass: ALLOW_NO_BUILD=1 git commit                   ║"
    echo "╚══════════════════════════════════════════════════════════╝"
    echo ""
    echo "Slides alterados sem rebuild:"
    echo "$SLIDES_STAGED" | sed 's/^/  → /'
    echo ""
    if [ -z "$ALLOW_NO_BUILD" ]; then
      exit 1
    fi
  fi
fi

# ── Guard 5: Class A/B governance files should live on main ──
# Warns and blocks when governance/infra files are edited on feature branches.
# Files inside aulas/*/ are Class C (aula-specific docs) and are excluded.
# Bypass: ALLOW_AB_ON_WT=1 git commit
if [ "$BRANCH" != "main" ] && [ -z "$ALLOW_AB_ON_WT" ]; then
  AB_EDITS=$(git diff --cached --name-only | grep -E '^(\.cursor/rules/|\.claude/|CLAUDE\.md$|docs/|tasks/|scripts/|\.gitignore$|vite\.config\.js$|README\.md$|ERROR-LOG\.md$|CHANGELOG\.md$)' | grep -v '^aulas/' || true)
  if [ -n "$AB_EDITS" ]; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║  BLOQUEADO: Classe A/B editada em feature branch        ║"
    echo "║  Governança/infra deve ser commitada em main.           ║"
    echo "║  Bypass: ALLOW_AB_ON_WT=1 git commit                   ║"
    echo "╚══════════════════════════════════════════════════════════╝"
    echo ""
    echo "Arquivos bloqueados:"
    echo "$AB_EDITS" | sed 's/^/  → /'
    echo ""
    exit 1
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
