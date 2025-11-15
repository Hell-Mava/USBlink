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

def _enumerate_hid_devices() -> List[Dict]:
    devices = []
    try:
        if is_windows():
            from pywinusb import hid
            for dev in hid.HidDeviceFilter().get_devices():
                devices.append({"vid": f"{dev.vendor_id:04X}", "pid": f"{dev.product_id:04X}", "role": "HID"})
        else:
            import usb.core
            for dev in usb.core.find(find_all=True):
                for cfg in dev:
                    for intf in cfg:
                        if intf.bInterfaceClass == 0x03:  # HID class
                            devices.append({"vid": f"{dev.idVendor:04X}", "pid": f"{dev.idProduct:04X}", "role": "HID"})
    except Exception as e:
        log_warn(f"HID enumeration failed: {e}")
    return devices

def run_badusb_scan() -> Dict:
    trust = load_trustlist()
    hid_devs = _enumerate_hid_devices()
    findings, severities = [], []

    for d in hid_devs:
        trusted = is_trusted(d["vid"], d["pid"], "HID", trust)
        if not trusted:
            findings.append(f"Untrusted HID device VID:{d['vid']} PID:{d['pid']} — potential BadUSB")
            severities.append("High")
        else:
            findings.append(f"HID device OK VID:{d['vid']} PID:{d['pid']} Trusted:Yes")
            severities.append("Low")

    if not findings:
        findings.append("No HID anomalies detected")
        severities.append("Low")

    log_info(f"BadUSB scan evaluated {len(hid_devs)} HID device(s)")
    return {"findings": findings, "severity": severities}
