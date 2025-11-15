#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Load YAML configuration files
# ============================================================

import os
import yaml
from utils.logger import log_warn

DEFAULT_TRUST_PATH = os.path.join("config", "trust.yaml")

def load_trustlist(path: str = DEFAULT_TRUST_PATH) -> dict:
    if not os.path.exists(path):
        log_warn(f"Trust list not found at {path}. Proceeding without trusted devices.")
        return {"trusted_devices": []}
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f) or {}
            if "trusted_devices" not in data:
                data["trusted_devices"] = []
            return data
        except Exception:
            log_warn("Failed to parse trust.yaml. Proceeding without trusted devices.")
            return {"trusted_devices": []}

def is_trusted(vid: str, pid: str, role: str, trust_data: dict) -> bool:
    for dev in trust_data.get("trusted_devices", []):
        if dev.get("vid", "").upper() == vid.upper() and dev.get("pid", "").upper() == pid.upper():
            roles = dev.get("roles", [])
            return role in roles or not roles
    return False
