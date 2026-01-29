#!/usr/bin/env bash
# Usage: ./copy_and_rename.sh <SOURCE> <TARGET>
set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <SOURCE> <TARGET>"
  exit 1
fi

SOURCE="$1"
TARGET="$2"

if [ ! -f "$SOURCE" ]; then
  echo "Source file '$SOURCE' does not exist."
  exit 2
fi

cp "$SOURCE" "$TARGET"
echo "Copied '$SOURCE' to '$TARGET'"
