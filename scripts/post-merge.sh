#!/usr/bin/env bash
# Post-merge: detect content regression in slide HTML files.
# Runs AFTER every git merge. Shows diff of slide changes for manual review.
set -e

BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")

AULA=""
case "$BRANCH" in
  *cirrose*)     AULA="cirrose" ;;
  *metanalise*)  AULA="metanalise" ;;
  *grade*)       AULA="grade" ;;
  *osteoporose*) AULA="osteoporose" ;;
esac

if [ -z "$AULA" ]; then
  exit 0
fi

SLIDE_DIR="aulas/$AULA/slides"
MANIFEST="$SLIDE_DIR/_manifest.js"

# Check 1: slide count
if [ -f "$MANIFEST" ]; then
  EXPECTED=$(grep -c "id:" "$MANIFEST" 2>/dev/null || echo "0")
  ACTUAL=$(find "$SLIDE_DIR" -name '*.html' -not -name '_*' 2>/dev/null | wc -l | tr -d ' ')

  if [ "$ACTUAL" -lt "$EXPECTED" ]; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║  ALERTA: Slides DESAPARECERAM apos merge!               ║"
    echo "║  Disco: $ACTUAL  |  Manifest: $EXPECTED                 ║"
    echo "║  REVERTA IMEDIATAMENTE:                                  ║"
    echo "║  git checkout HEAD~1 -- $SLIDE_DIR/                      ║"
    echo "╚══════════════════════════════════════════════════════════╝"
    echo ""
  fi
fi

# Check 2: content changes in slides (the silent rollback detector)
SLIDE_DIFF=$(git diff HEAD~1 HEAD --stat -- "$SLIDE_DIR/"*.html 2>/dev/null || true)

if [ -n "$SLIDE_DIFF" ]; then
  echo ""
  echo "╔══════════════════════════════════════════════════════════╗"
  echo "║  ATENCAO: O merge MODIFICOU slides HTML!                ║"
  echo "║  Verifique se o conteudo nao foi revertido.             ║"
  echo "╚══════════════════════════════════════════════════════════╝"
  echo ""
  echo "Slides alterados pelo merge:"
  echo "$SLIDE_DIFF"
  echo ""
  echo "Para ver o diff completo:"
  echo "  git diff HEAD~1 HEAD -- $SLIDE_DIR/"
  echo ""
  echo "Se o merge REVERTEU conteudo, restaurar:"
  echo "  git checkout HEAD~1 -- $SLIDE_DIR/"
  echo "  git commit -m 'fix: restore slides after merge rollback'"
  echo ""
fi

# Check 3: CSS changes in aula-specific CSS
CSS_FILE="aulas/$AULA/$AULA.css"
if [ -f "$CSS_FILE" ]; then
  CSS_DIFF=$(git diff HEAD~1 HEAD --stat -- "$CSS_FILE" 2>/dev/null || true)
  if [ -n "$CSS_DIFF" ]; then
    echo "⚠ O merge tambem alterou $CSS_FILE — verificar."
    echo ""
  fi
fi
