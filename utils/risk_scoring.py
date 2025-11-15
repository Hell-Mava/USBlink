#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Risk scoring and severity helpers
# ============================================================

from typing import List

WEIGHTS = {"Low": 5, "Medium": 10, "High": 20, "Critical": 30}
ORDER = ["Low", "Medium", "High", "Critical"]

def score_from_severities(severities: List[str]) -> int:
    total = sum(WEIGHTS.get(s, 0) for s in severities)
    return min(total, 100)

def overall_severity(severities: List[str]) -> str:
    highest = "Low"
    for s in severities:
        if ORDER.index(s) > ORDER.index(highest):
            highest = s
    return highest
