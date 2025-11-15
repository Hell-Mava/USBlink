#!/usr/bin/env python3
# ============================================================
# Project: USBlink
# Author: Sohel Shaik
# Occupation: Cybersecurity student (Ethical Hacking, VAPT, Wireless Security)
# GitHub: https://github.com/Hell-Mava
# Description: Backend detection utility for PyUSB and pywinusb
# ============================================================

def has_pyusb():
    try:
        import usb.backend.libusb1 as lb
        return lb.get_backend() is not None
    except Exception:
        return False

def backend_name():
    if has_pyusb():
        return "pyusb"
    try:
        from pywinusb import hid  # noqa: F401
        return "pywinusb"
    except Exception:
        pass
    return None
