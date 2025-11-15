#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Tests for device monitor
# ============================================================

from modules.device_monitor import run_device_monitor

def test_device_monitor_structure():
    res = run_device_monitor()
    assert isinstance(res, dict)
    assert "findings" in res and "severity" in res
    assert isinstance(res["findings"], list)
    assert isinstance(res["severity"], list)
