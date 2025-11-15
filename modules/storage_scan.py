#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Removable storage scan using psutil
# ============================================================

import psutil
from typing import List, Dict
from utils.logger import log_info, log_warn
from utils.platform import is_windows

def _is_removable(part) -> bool:
    """
    Check if a partition is removable.
    On Windows: look for 'removable' in options.
    On Linux/macOS: check common mount paths (/media, /run/media, /volumes).
    """
    try:
        if is_windows():
            return "removable" in (part.opts or "").lower()
        mp = (part.mountpoint or "").lower()
        return mp.startswith("/media/") or mp.startswith("/run/media/") or mp.startswith("/volumes/")
    except Exception:
        return False

def run_storage_scan() -> Dict:
    """
    Scan system partitions and return removable mounts.
    """
    mounts: List[Dict] = []
    try:
        for part in psutil.disk_partitions(all=False):
            if _is_removable(part):
                mounts.append({
                    "mount": part.mountpoint,
                    "fstype": part.fstype,
                    "opts": part.opts
                })
        log_info(f"Storage scan checked {len(mounts)} mount(s)")
    except Exception as e:
        log_warn(f"Storage scan failed safely: {e}")
    return {"mounts": mounts}
