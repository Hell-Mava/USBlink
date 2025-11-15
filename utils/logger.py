#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Simple logger utilities
# ============================================================

from datetime import datetime

def _ts() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_info(msg: str) -> None:
    print(f"[INFO { _ts() }] {msg}")

def log_warn(msg: str) -> None:
    print(f"[WARN { _ts() }] {msg}")

def log_error(msg: str) -> None:
    print(f"[ERROR { _ts() }] {msg}")
