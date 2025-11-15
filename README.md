USBlink README
-------------------

<div align="center">

# 🔗 USBlink  
### A Modular Python Toolkit for USB Threat Detection, BadUSB Analysis & Device Security

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

</div>

---

USBlink is a lightweight, security-focused Python framework designed to detect suspicious USB activity in real time.  
It helps identify BadUSB attacks, unauthorized devices, and unusual file transfers — making it ideal for cybersecurity students, VAPT learners, and technical recruiters.

---

## 🚀 What USBlink Offers

- Real-Time USB Monitoring  
- BadUSB Heuristics Engine  
- File Activity Observation  
- Automated Report Generation  
- Modular Architecture  
- CLI-Based Execution  

---

## 🛠️ Installation & Setup

git clone https://github.com/Hell-Mava/USBlink.git
cd USBlink

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt

---

## ▶️ Running USBlink

python usblink.py run

Example output:

[+] Monitoring USB devices...
[+] Device detected: Kingston USB 3.0
[!] Suspicious device flagged: Unknown Vendor ID
Report saved: report_2025-11-15.txt

---

## 📌 Why This Project Is Useful

- Great for students learning cybersecurity  
- Useful for VAPT practice  
- Shows real detection logic to recruiters  
- Demonstrates hardware-level threat awareness  

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Sohel Shaik  
GitHub: Hell-Mava  
LinkedIn: https://www.linkedin.com/in/sohel-shaik-894288282/

---

<div align="center">
✨ USBlink — A small tool with strong defensive potential. ✨
</div>
