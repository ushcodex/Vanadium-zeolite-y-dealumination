#!/usr/bin/env python3
"""Compatibility entry point for building the current ABU thesis document."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.build_thesis_docx import main


if __name__ == "__main__":
    main()
