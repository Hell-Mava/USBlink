#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Suspicious file scanning for removable USB volumes (heuristic)
# ============================================================

from typing import List, Dict
import os
from utils.logger import log_info, log_warn

SUSPICIOUS_NAMES = {
    "autorun.inf", "desktop.ini",
    "readme.scr", "thumbs.db"
}

SUSPICIOUS_EXTS = {
    ".bat", ".cmd", ".vbs", ".js", ".jse", ".ps1", ".psm1", ".scr", ".exe", ".dll"
}

SUSPICIOUS_DIRS = {
    "RECYCLER", "$RECYCLE.BIN", "System Volume Information"
}

MAX_FILES_PER_MOUNT = 3000  # safety cap to avoid huge scans

def _scan_mount(mount_path: str) -> List[str]:
    findings: List[str] = []
    count = 0
    for root, dirs, files in os.walk(mount_path):
        # Flag suspicious directories
        for d in dirs:
            if d in SUSPICIOUS_DIRS:
                findings.append(f"Suspicious directory: {os.path.join(root, d)}")

        # Check files
        for f in files:
            count += 1
            if count > MAX_FILES_PER_MOUNT:
                findings.append(f"Scan limit reached at {mount_path}, consider deeper scan manually")
                return findings

            lower = f.lower()
            path = os.path.join(root, f)
            _, ext = os.path.splitext(lower)

            if lower in SUSPICIOUS_NAMES:
                findings.append(f"Suspicious filename: {path}")
            elif ext in SUSPICIOUS_EXTS:
                findings.append(f"Suspicious extension ({ext}): {path}")

            # Basic hidden/system flag on Windows (heuristic)
            try:
                attrs = os.stat(path)
                # Placeholder: real hidden/system checking would use win32 APIs
                # Keep it simple and fast for now.
            except Exception:
                continue

    return findings

def run_file_scan(storage_scan_result: Dict) -> Dict:
    mounts = storage_scan_result.get("mounts", [])
    findings: List[str] = []
    severities: List[str] = []

    for m in mounts:
        mpath = m.get("mount")
        if not mpath:
            continue
        mf = _scan_mount(mpath)
        if mf:
            findings.extend([f"[{mpath}] {x}" for x in mf])
            severities.extend(["Medium" if "Suspicious directory" in " ".join(mf) else "High" if any(ext in " ".join(mf) for ext in SUSPICIOUS_EXTS) else "Low"] * len(mf))
        else:
            findings.append(f"[{mpath}] No suspicious files detected")
            severities.append("Low")

    if not findings:
        findings.append("No removable mounts to scan or no suspicious files found")
        severities.append("Low")

    log_info(f"File scan evaluated {len(mounts)} mount(s)")
    return {"findings": findings, "severity": severities}
