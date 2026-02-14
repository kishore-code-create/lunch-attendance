# 🚀 DEPLOYMENT GUIDE

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `lunch-attendance`
3. Make it **Public**
4. Don't initialize with README
5. Click "Create repository"

## Step 2: Push Code to GitHub

Copy your repository URL (looks like: `https://github.com/YOUR_USERNAME/lunch-attendance.git`)

Run these commands:

```bash
cd lunch_system
git remote remove origin
git remote add origin YOUR_GITHUB_URL_HERE
git branch -M main
git push -u origin main
```

## Step 3: Deploy on Streamlit Cloud

### Deploy Student App (Public)

1. Go to https://share.streamlit.io
2. Click "New app"
3. Select your repository: `YOUR_USERNAME/lunch-attendance`
4. Branch: `main`
5. Main file path: `student_app.py`
6. App URL: Choose custom URL like `nexus-lunch-student`
7. Click "Deploy"

### Deploy Scanner App (Private)

1. Click "New app" again
2. Same repository
3. Main file path: `scanner_app.py`
4. App URL: `nexus-lunch-scanner`
5. Click "Deploy"

### Deploy Dashboard App (Private)

1. Click "New app" again
2. Same repository
3. Main file path: `dashboard_app.py`
4. App URL: `nexus-lunch-dashboard`
5. Click "Deploy"

## Step 4: Initialize Database on Cloud

For EACH deployed app:

1. Open the app URL
2. Click "⋮" menu → "Settings" → "Secrets"
3. The database will auto-initialize on first run

OR manually run init_db.py once locally and commit the database:

```bash
# Remove data/ from .gitignore
# Edit .gitignore and comment out: # data/

git add data/attendance.db
git commit -m "Add initialized database"
git push
```

## Step 5: Create QR Code Poster

1. Copy your student app URL (e.g., `https://nexus-lunch-student.streamlit.app`)
2. Edit `create_poster.py` and update the URL
3. Run: `python create_poster.py`
4. Print `lunch_poster.png`
5. Place near canteen entrance

## 📱 Your App URLs

After deployment, you'll have:

- **Student App**: `https://nexus-lunch-student.streamlit.app` (Share this publicly)
- **Scanner App**: `https://nexus-lunch-scanner.streamlit.app` (Keep private)
- **Dashboard**: `https://nexus-lunch-dashboard.streamlit.app` (Keep private)

## 🔒 Security (Optional)

Add password protection to scanner and dashboard:

```python
# Add at top of scanner_app.py and dashboard_app.py
import streamlit as st

if 'authenticated' not in st.session_state:
    password = st.text_input("Enter Password", type="password")
    if password == "nexus2026":
        st.session_state.authenticated = True
        st.rerun()
    else:
        st.stop()
```

## ✅ Testing

1. Open student app → Enter roll number → Get QR
2. Open scanner app → Enter same roll number → Verify
3. Open dashboard → See attendance marked

## 🐛 Troubleshooting

**Database not persisting:**
- Commit the database file to git (see Step 4)

**Apps not connecting:**
- All apps must use the same database
- Ensure `data/attendance.db` is in git

**Excel file missing:**
- Upload Excel file to repository
- Or initialize database locally and commit it

---

**Ready to deploy? Follow steps 1-5 above!**
