#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Tests for storage scan
# ============================================================

from modules.storage_scan import run_storage_scan

def test_storage_scan_structure():
    res = run_storage_scan()
    assert "findings" in res and "severity" in res
    assert isinstance(res["findings"], list)
    assert isinstance(res["severity"], list)
