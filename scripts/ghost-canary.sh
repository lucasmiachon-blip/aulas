#!/usr/bin/env bash
# ghost-canary.sh — Dry-run merge from main without touching the working tree.
# Creates a throwaway branch, attempts merge, reports conflicts, aborts, cleans up.
# Zero commits, zero changes.
#
# Usage: bash scripts/ghost-canary.sh [target_branch]
#   target_branch defaults to "main"

set -euo pipefail

TARGET="${1:-main}"
ORIGINAL_BRANCH="$(git branch --show-current)"
CANARY_BRANCH="canary/ghost-$(date +%s)"

if [ -z "$ORIGINAL_BRANCH" ]; then
  echo "ERROR: detached HEAD — checkout a branch first."
  exit 1
fi

if ! git rev-parse --verify "$TARGET" >/dev/null 2>&1; then
  echo "ERROR: branch '$TARGET' not found. Fetch first?"
  exit 1
fi

# Ensure clean working tree
if [ -n "$(git status --porcelain)" ]; then
  echo "ERROR: working tree not clean. Commit or stash first."
  exit 1
fi

cleanup() {
  git merge --abort 2>/dev/null || true
  git checkout "$ORIGINAL_BRANCH" --quiet 2>/dev/null || true
  git branch -D "$CANARY_BRANCH" --quiet 2>/dev/null || true
}
trap cleanup EXIT

echo "=== Ghost Canary ==="
echo "  from: $ORIGINAL_BRANCH"
echo "  into: $TARGET (dry-run)"
echo ""

# Create throwaway branch at current HEAD
git checkout -b "$CANARY_BRANCH" --quiet

# Attempt merge — capture result
if git merge --no-commit --no-ff "$TARGET" >/dev/null 2>&1; then
  echo "RESULT: clean — no conflicts with $TARGET"
  # Show what would change
  CHANGED=$(git diff --cached --stat | tail -1)
  if [ -n "$CHANGED" ]; then
    echo ""
    echo "Files that would change:"
    git diff --cached --name-status
    echo ""
    echo "$CHANGED"
  fi
  # cleanup trap handles merge --abort
else
  echo "RESULT: CONFLICTS detected"
  echo ""
  # List conflicted files
  git diff --name-only --diff-filter=U 2>/dev/null || true
  echo ""
  echo "Run 'git diff' on canary branch for details (but we're cleaning up now)."
  # cleanup trap handles merge --abort
fi

echo ""
echo "Cleanup: removing $CANARY_BRANCH, restoring $ORIGINAL_BRANCH"
# trap handles cleanup
