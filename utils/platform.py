#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Platform detection helpers
# ============================================================

import sys

def is_windows() -> bool:
    return sys.platform.startswith("win")

def is_linux() -> bool:
    return sys.platform.startswith("linux")

def platform_name() -> str:
    return "Windows" if is_windows() else ("Linux" if is_linux() else sys.platform)
