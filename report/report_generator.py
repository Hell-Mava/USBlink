#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Timestamped text report generator
# ============================================================

from datetime import datetime
from typing import Dict, List, Tuple
from utils.risk_scoring import score_from_severities, overall_severity
from utils.file_utils import write_text
from utils.logger import log_info

def _flatten_findings(results: Dict) -> List[Tuple[str, str]]:
    items: List[Tuple[str, str]] = []
    for module, data in results.items():
        if not data:
            continue
        for f in data.get("findings", []):
            items.append((module, f))
    return items

def generate_report(results: Dict) -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"report_{ts}.txt"

    severities: List[str] = []
    for data in results.values():
        s = data.get("severity", [])
        if isinstance(s, list):
            severities.extend(s)
        elif isinstance(s, str):
            severities.append(s)

    score = score_from_severities(severities)
    sev = overall_severity(severities) if severities else "Low"

    lines: List[str] = []
    lines.append(f"USBlink Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 60)
    lines.append(f"Risk Score: {score}/100")
    lines.append(f"Severity: {sev}")
    lines.append("")
    lines.append("Findings:")
    for module, item in _flatten_findings(results):
        lines.append(f" - [{module}] {item}")
    lines.append("")
    lines.append("Recommendations:")
    lines.append(" - Unplug suspicious devices immediately.")
    lines.append(" - Avoid executables/scripts on USB storage.")
    lines.append(" - Whitelist (trust) only known devices.")
    lines.append(" - Run USBlink regularly.")

    content = "\n".join(lines)
    write_text(path, content)
    log_info(f"Report saved: {path}")
    return path
