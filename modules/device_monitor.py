#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# ============================================================

from typing import List, Dict
from utils.logger import log_info, log_warn
from utils.config_loader import load_trustlist, is_trusted
from utils.platform import is_windows
from utils.backend_check import has_pyusb

def _list_devices_pyusb() -> List[Dict]:
    try:
        import usb.core
        devices = []
        for dev in usb.core.find(find_all=True):
            vid = f"{dev.idVendor:04X}"
            pid = f"{dev.idProduct:04X}"
            devices.append({"vid": vid, "pid": pid, "role": "Unknown"})
        return devices
    except Exception:
        log_warn("PyUSB failed. Trying pywinusb fallback...")
        return []

def _list_devices_pywinusb() -> List[Dict]:
    try:
        from pywinusb import hid
        devices = []
        for dev in hid.HidDeviceFilter().get_devices():
            vid = f"{dev.vendor_id:04X}"
            pid = f"{dev.product_id:04X}"
            devices.append({"vid": vid, "pid": pid, "role": "HID"})
        return devices
    except Exception:
        log_warn("pywinusb fallback failed.")
        return []

def run_device_monitor() -> Dict:
    trust = load_trustlist()
    devices = _list_devices_pyusb() if has_pyusb() else []
    if not devices and is_windows():
        devices = _list_devices_pywinusb()

    findings, severities = [], []
    for d in devices:
        trusted = is_trusted(d["vid"], d["pid"], d["role"], trust)
        findings.append(
            f"Detected USB - VID:{d['vid']} PID:{d['pid']} Role:{d['role']} Trusted:{'Yes' if trusted else 'No'}"
        )
        severities.append("Medium" if d["role"] == "HID" and not trusted else "Low")

    if not findings:
        findings.append("No USB devices detected at this time.")
        severities.append("Low")

    log_info(f"Device monitor found {len(devices)} device(s)")
    return {"findings": findings, "severity": severities}
