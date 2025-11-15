#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Tests for anomaly detection
# ============================================================
from modules.anomaly_detector import run_anomaly_detection

def test_anomaly_detection_structure():
    res = run_anomaly_detection()
    assert "findings" in res and "severity" in res
    assert isinstance(res["findings"], list)
    assert isinstance(res["severity"], list)
