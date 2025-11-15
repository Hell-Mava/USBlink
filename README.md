USBlink README
-------------------

<div align="center">

# 🔗 USBlink  
### A Modular Python Toolkit for USB Threat Detection, BadUSB Analysis & Device Security

[Python 3.10+]
[MIT License]
[Windows | Linux]
[Active Development]

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

1️⃣ Clone the repository  
git clone https://github.com/Hell-Mava/USBlink.git

2️⃣ Move into the project folder  
cd USBlink

3️⃣ Create a virtual environment  
python -m venv venv

4️⃣ Activate the virtual environment  
Linux/macOS:  
source venv/bin/activate  
Windows:  
venv\Scripts\activate

5️⃣ Install dependencies  
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
Email: 1914sohel@gmail.com

---

USBlink — A small tool with strong defensive potential.
