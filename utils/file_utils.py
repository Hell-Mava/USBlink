#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: File utilities
# ============================================================

import os

def ensure_parent_dir(path: str) -> None:
    parent = os.path.dirname(path)
    if parent and not os.path.exists(parent):
        os.makedirs(parent, exist_ok=True)

def write_text(path: str, content: str) -> str:
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

def list_dir_safe(path: str):
    try:
        return os.listdir(path)
    except Exception:
        return []
