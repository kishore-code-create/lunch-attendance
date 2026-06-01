# 🎟️ IEEE NEXUS 2026 — Lunch Attendance System

> QR-code based event lunch attendance tracker for IEEE NEXUS 2026 — built with Streamlit

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![Streamlit](https://img.shields.io/badge/Streamlit-3_apps-red?logo=streamlit) ![QR](https://img.shields.io/badge/QR-Code-black) ![SQLite](https://img.shields.io/badge/Database-SQLite-blue)

## 📋 Overview

A real-time QR-code based lunch attendance system built for the IEEE NEXUS 2026 event. Manages lunch token generation, scanning, and admin reporting across three dedicated Streamlit apps — ensuring every participant gets exactly one lunch pass.

## ✨ Features

- 🎫 **Student App** — Enter roll number, generate unique QR token
- 📷 **Scanner App** — Real-time QR scan and validation
- 📊 **Admin Dashboard** — Live attendance stats and export
- 🚫 **Duplicate Prevention** — One token per participant enforced
- 📈 **Poster Generator** — Auto-generate event posters via script

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Web Apps | Streamlit |
| Database | SQLite |
| QR Codes | qrcode, pyzbar |
| Data Export | Pandas |
| Launch | Batch script (Windows) |

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/kishore-code-create/lunch-attendance.git
cd lunch-attendance

# Install dependencies
pip install -r requirements.txt

# Initialise the database
python init_db.py

# Launch all apps (Windows)
start_all.bat

# Or run individually
streamlit run student_app.py
streamlit run scanner_app.py
streamlit run dashboard_app.py
```

## 📁 Project Structure

```
lunch-attendance/
├── student_app.py     # Student token generation
├── scanner_app.py     # QR scanner for operators
├── dashboard_app.py   # Admin dashboard
├── init_db.py         # Database initialisation
├── create_poster.py   # Event poster generator
├── data/              # Local database storage
├── start_all.bat      # Windows launcher
└── requirements.txt
```

## 👨‍💻 Author

**Nanda Kishore** — AI/ML Engineer  
📧 nandakishoredevarashetti@gmail.com  
🔗 [GitHub](https://github.com/kishore-code-create) | [LinkedIn](https://linkedin.com/in/nanda-kishore-devarashetti)

## 📄 License

MIT License

