#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Tests for BadUSB detection
# ============================================================

from modules.badusb_detect import run_badusb_detection

def test_badusb_structure():
    res = run_badusb_detection()
    assert "findings" in res and "severity" in res
    assert isinstance(res["findings"], list)
    assert isinstance(res["severity"], list)
