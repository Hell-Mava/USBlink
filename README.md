# USBlink

Author: Sohel Shaik  
GitHub: https://github.com/Hell-Mava

USBlink is a Windows + Linux CLI tool that scans USB devices for risks:
- Device enumeration with trust list
- HID anomaly detection (default burst typing rule)
- Storage scan for autorun.inf, hidden files, and dangerous types (.exe, .bat, .vbs, .lnk)
- BadUSB heuristic (composite HID + Mass Storage)
- Timestamped text reports (e.g., report_20251115_134500.txt)

## Install
```bash
python -m venv venv
# Windows PowerShell:
venv\Scripts\Activate.ps1
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt

