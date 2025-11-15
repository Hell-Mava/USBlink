<div align="center">

# 🔗 USBlink  
### A Modular Python Toolkit for USB Threat Detection, BadUSB Analysis & Device Security

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

</div>

-------------------------------------------------------------------------------
## 🧭 Overview
USBlink is a lightweight, security‑focused Python framework used to detect, 
monitor, and analyze suspicious USB activity in real time. It demonstrates 
practical cybersecurity concepts such as BadUSB detection, device forensics, 
and system monitoring making it ideal for VAPT students and recruiter demos.
-------------------------------------------------------------------------------

## 🚀 Features (Premium Overview)

1️⃣ **Real‑Time USB Monitoring**
     Detect and log every USB device that connects.

2️⃣ **BadUSB Detection**
     Identify spoofed devices, unknown vendors, and anomalies.

3️⃣ **File Activity Observation**
     Watch for unusual or suspicious file transfers.

4️⃣ **Automated Report Generation**
     Clean, timestamped reports saved in the `/reports` folder.

5️⃣ **Modular Architecture**
     Add custom scanners easily inside `modules/`.

6️⃣ **CLI Execution** 
     Perfect for demos, labs, and interviews.

-------------------------------------------------------------------------------
## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
Download the project from GitHub.

    git clone https://github.com/Hell-Mava/USBlink.git

### 2️⃣ Move Into the Project Directory
Navigate into the USBlink folder.

    cd USBlink

### 3️⃣ Create a Virtual Environment
Create an isolated Python environment.

    python -m venv venv

### 4️⃣ Activate the Virtual Environment
**Linux / macOS:**
        source venv/bin/activate

**Windows:**
        venv\Scripts\activate

### 5️⃣ Install All Dependencies
**Install all required packages.**

    pip install -r requirements.txt

-------------------------------------------------------------------------------
## ▶️ Running USBlink

### 1️⃣ Start the Tool
**Launch the main script.**

    python usblink.py run

Expected Output:
    [+] Monitoring USB devices...
    [+] Device detected: Kingston USB 3.0
    [!] Suspicious device flagged: Unknown Vendor ID
    Report saved: report_YYYY-MM-DD.txt

-------------------------------------------------------------------------------
## 📂 Project Structure

USBLINK/
│── usblink.py          → Main execution script  
│── modules/            → Detection & scanning modules  
│── utils/              → Helper utilities  
│── reports/            → Auto‑generated reports  
│── requirements.txt    → Dependencies  
│── README.md           → Documentation  

-------------------------------------------------------------------------------
## 📌 Why This Project Is Useful

### 🎓 For Students  
Real hands‑on cybersecurity + Python experience.

### 👔 For Recruiters  
Demonstrates practical detection logic and modular design.

### 🛡️ For VAPT Practice  
Helps understand hardware‑level attack vectors.

### 🧪 For Labs  
Good base for training environments and research.

-------------------------------------------------------------------------------
## 📜 License
This project is licensed under the **MIT License**.

-------------------------------------------------------------------------------
## 👨‍💻 Author
**Sohel Shaik**  
GitHub: Hell-Mava  
LinkedIn: https://www.linkedin.com/in/sohel-shaik-894288282/

-------------------------------------------------------------------------------
<div align="center">
✨ USBlink — Small Tool. Strong Defense. Professional Impact. ✨
</div>
-------------------------------------------------------------------------------
