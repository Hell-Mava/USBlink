#!/usr/bin/env python3
# =============================================================
# Project: USBlink
# Author: Sohel Shaik
# GitHub: https://github.com/Hell-Mava
# Description: Recruiter-friendly USB security toolkit
# =============================================================

from utils.logger import log_info, log_warn
from utils.backend_check import backend_name
from modules import device_monitor, storage_scan, anomaly_detector, badusb_detect, suspicious_files

def run():
    log_info("Running full USBlink scan...")

    backend = backend_name()
    if backend:
        log_info(f"USB backend selected: {backend}")
    else:
        log_warn("No USB backend available; proceeding with limited functionality")

    # Execute modules
    dm = device_monitor.run_device_monitor()
    ad = anomaly_detector.run_anomaly_detection()
    bd = badusb_detect.run_badusb_scan()
    ss = storage_scan.run_storage_scan()
    sf = suspicious_files.run_file_scan(ss)

    # === User-friendly verdicts ===
    log_info("=== Scan Results ===")

    # Device monitor
    log_info(f"USB Devices: {len(dm['findings'])} found")

    # Anomaly detection
    if any("No anomalies" in f for f in ad["findings"]):
        log_info("Anomaly Detection Verdict: No anomalies detected")
    else:
        log_info("Anomaly Detection Verdict: Anomalies found")

    # BadUSB / HID verdict
    if any(("Untrusted HID" in f) or ("BadUSB" in f) for f in bd["findings"]):
        log_info("BadUSB/HID Verdict: Suspicious HID device(s) found")
        for finding in bd["findings"]:
            if "Untrusted HID" in finding or "BadUSB" in finding:
                log_info(f" -> {finding}")
    else:
        log_info("BadUSB/HID Verdict: No HID anomalies detected")

    # Storage mounts
    log_info(f"Storage Devices: {len(ss['mounts'])} removable mount(s) detected")

    # Suspicious files
    if any("Suspicious" in f for f in sf["findings"]):
        log_info("File Scan Verdict: Suspicious file(s) found")
        for finding in sf["findings"]:
            if "Suspicious" in finding:
                log_info(f" -> {finding}")
    else:
        log_info("File Scan Verdict: No suspicious files found")

    log_info("=== End of Scan ===")

    return {
        "device_monitor": dm,
        "anomaly_detection": ad,
        "badusb_scan": bd,
        "storage_scan": ss,
        "file_scan": sf
    }

if __name__ == "__main__":
    run()
