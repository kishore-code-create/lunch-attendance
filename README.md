# Lunch Attendance System — IEEE NEXUS 2026

A QR-code based event lunch attendance tracker built for IEEE NEXUS 2026. Manages token generation, real-time validation, and admin reporting across three Streamlit applications.

**Stack:** Python · Streamlit · SQLite · qrcode · pyzbar · Pandas

---

## Overview

Manual attendance at large events is error-prone and slow. This system issues unique QR tokens to registered participants, validates them at meal counters in real time, and gives organisers a live dashboard of attendance data.

## Applications

| App | File | Purpose |
|-----|------|---------|
| Student Portal | `student_app.py` | Enter roll number, generate one-time QR token |
| Scanner | `scanner_app.py` | Camera-based token validation at the counter |
| Admin Dashboard | `dashboard_app.py` | Live stats, attendance log, CSV export |

## Features

- One token per participant — duplicates rejected at scan
- Real-time validation with instant feedback
- Admin dashboard with live headcount and export
- Windows batch launcher for quick multi-app startup

## Getting Started

```bash
git clone https://github.com/kishore-code-create/lunch-attendance.git
cd lunch-attendance
pip install -r requirements.txt
python init_db.py

# Windows — launch all apps
start_all.bat

# Or individually
streamlit run student_app.py
streamlit run scanner_app.py
streamlit run dashboard_app.py
```

## Project Structure

```
lunch-attendance/
├── student_app.py      # Student token generation
├── scanner_app.py      # QR scanner for operators
├── dashboard_app.py    # Admin dashboard
├── init_db.py          # Database initialisation
├── create_poster.py    # Event poster generator
├── data/               # Local SQLite database
├── start_all.bat       # Windows multi-app launcher
└── requirements.txt
```

## Author

**Nanda Kishore** — [nandakishoredevarashetti@gmail.com](mailto:nandakishoredevarashetti@gmail.com)  
[GitHub](https://github.com/kishore-code-create) · [LinkedIn](https://linkedin.com/in/nanda-kishore-devarashetti)

---

MIT License
