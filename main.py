#!/usr/bin/env python3
"""Entrypoint for news-image-20261124.

Copies entry.png from the repository directory to the output
directory named by MAKEFUN_OUTPUT_DIR. Standard library only:
no Pillow, no third-party imports, no network, no timestamps.
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        sys.stderr.write("MAKEFUN_OUTPUT_DIR is not set\n")
        return 1
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
