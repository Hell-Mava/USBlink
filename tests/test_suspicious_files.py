#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Tests for suspicious files
# ============================================================

from modules.suspicious_files import run_suspicious_files_scan

def test_suspicious_files_structure():
    res = run_suspicious_files_scan()
    assert "findings" in res and "severity" in res
    assert isinstance(res["findings"], list)
    assert isinstance(res["severity"], list)
