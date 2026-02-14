# 🍽️ IEEE NEXUS 2026 - Lunch Attendance System

A complete QR code-based lunch token system with 3 separate Streamlit apps for students, scanner operators, and admins.

## 📋 Features

### 1. **Student App** (`student_app.py`)
- Students enter their roll number
- Generate unique QR code token
- One-time use validation
- Clean, mobile-friendly interface

### 2. **Scanner App** (`scanner_app.py`)
- Verify QR codes at lunch counter
- Manual roll number entry
- Real-time attendance marking
- Live statistics display
- Duplicate detection

### 3. **Admin Dashboard** (`dashboard_app.py`)
- Real-time attendance monitoring
- Search and filter attendees
- Export reports (CSV)
- Recent activity tracking
- Auto-refresh option
- Reset functionality

## 🚀 Quick Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Initialize Database
```bash
python init_db.py
```
This will load all 215 roll numbers from the Excel file into the database.

### Step 3: Run the Apps

**For Students (Mobile/Public Access):**
```bash
streamlit run student_app.py --server.port 8501
```

**For Scanner (Lunch Counter):**
```bash
streamlit run scanner_app.py --server.port 8502
```

**For Admin (Dashboard):**
```bash
streamlit run dashboard_app.py --server.port 8503
```

## 📱 Usage Flow

1. **Students**: 
   - Scan QR code poster → Opens student app
   - Enter roll number → Get QR token
   - Show QR at counter

2. **Scanner Operator**:
   - Open scanner app on device
   - Scan student's QR or enter roll number manually
   - System validates and marks attendance

3. **Admin**:
   - Monitor real-time progress
   - View who has eaten
   - Export reports
   - Handle issues

## 🌐 Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. Push code to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

2. Deploy on Streamlit Cloud:
   - Go to https://share.streamlit.io
   - Connect your GitHub repo
   - Deploy each app separately:
     - `student_app.py` → Public URL for students
     - `scanner_app.py` → Private URL for counter
     - `dashboard_app.py` → Private URL for admin

3. Create QR code poster with student app URL

### Option 2: Local Network (No Internet)

1. Find your local IP:
```bash
ipconfig  # Windows
ifconfig  # Mac/Linux
```

2. Run apps with your IP:
```bash
streamlit run student_app.py --server.address 192.168.1.X --server.port 8501
streamlit run scanner_app.py --server.address 192.168.1.X --server.port 8502
streamlit run dashboard_app.py --server.address 192.168.1.X --server.port 8503
```

3. Students access: `http://192.168.1.X:8501`
4. Scanner: `http://192.168.1.X:8502`
5. Admin: `http://192.168.1.X:8503`

### Option 3: Heroku/Railway/Render

Create `Procfile`:
```
web: streamlit run student_app.py --server.port $PORT
```

Deploy each app as separate service.

## 📊 Database Structure

**Table: attendance**
- `roll_number` (TEXT, PRIMARY KEY)
- `name` (TEXT)
- `timestamp` (TEXT)
- `scanned` (INTEGER, 0 or 1)

## 🎨 Customization

### Change Event Name
Edit the title in each app file:
```python
st.title("🍽️ YOUR EVENT NAME")
```

### Modify Colors
Update the CSS in each app's `st.markdown()` section.

### Add Fields
Modify `init_db.py` to include additional columns from Excel.

## 🔒 Security Tips

1. **Password protect scanner/admin apps:**
```python
import streamlit as st

password = st.text_input("Enter Password", type="password")
if password != "your_password":
    st.stop()
```

2. **Use HTTPS** when deploying publicly

3. **Backup database** regularly:
```bash
cp data/attendance.db data/attendance_backup.db
```

## 📱 Creating QR Code Poster

1. Deploy student app
2. Get the URL (e.g., `https://your-app.streamlit.app`)
3. Generate QR code:
```python
import qrcode
qr = qrcode.make("https://your-app.streamlit.app")
qr.save("poster_qr.png")
```
4. Create poster with:
   - Event name
   - QR code
   - Instructions
   - Print and place near canteen

## 🐛 Troubleshooting

**Database not found:**
```bash
python init_db.py
```

**Port already in use:**
```bash
streamlit run app.py --server.port 8504
```

**Excel file not found:**
- Ensure Excel file is in parent directory
- Update path in `init_db.py`

## 📞 Support

For issues or questions, contact the IEEE NEXUS 2026 tech team.

## 📄 License

MIT License - Free to use and modify

---

**Built with ❤️ for IEEE NEXUS 2026**
