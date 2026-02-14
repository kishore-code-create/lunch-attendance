import streamlit as st
import sqlite3
from datetime import datetime
from streamlit_qr_scanner import qr_scanner

DB_PATH = 'data/attendance.db'

st.set_page_config(page_title="Scanner - Lunch Counter", page_icon="📷", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .main {background-color: #1e1e1e; color: white;}
    .stButton>button {
        width: 100%;
        height: 4em;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
    }
    .success-box {
        padding: 30px;
        background-color: #28a745;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 24px;
        margin: 20px 0;
    }
    .error-box {
        padding: 30px;
        background-color: #dc3545;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 24px;
        margin: 20px 0;
    }
    .info-box {
        padding: 20px;
        background-color: #17a2b8;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

st.title("📷 Lunch Counter Scanner")
st.markdown("---")

# Get stats
def get_stats():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM attendance WHERE scanned = 1')
    scanned = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM attendance')
    total = c.fetchone()[0]
    conn.close()
    return scanned, total

scanned_count, total_count = get_stats()

# Display stats
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("✅ Served", scanned_count)
with col2:
    st.metric("⏳ Remaining", total_count - scanned_count)
with col3:
    st.metric("📊 Total", total_count)

st.markdown("---")

# Manual entry option
st.subheader("🔍 Manual Entry")
manual_roll = st.text_input("Enter Roll Number", placeholder="1602-25-735-018")

if st.button("✅ VERIFY & MARK", type="primary"):
    if manual_roll:
        roll_number = manual_roll.strip()
        
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            
            # Check if exists
            c.execute('SELECT name, scanned FROM attendance WHERE roll_number = ?', (roll_number,))
            result = c.fetchone()
            
            if not result:
                st.markdown('<div class="error-box">❌ INVALID<br>Roll number not found</div>', unsafe_allow_html=True)
                st.error(f"Roll Number: {roll_number}")
            elif result[1] == 1:
                st.markdown('<div class="error-box">⚠️ ALREADY SCANNED<br>This person already ate!</div>', unsafe_allow_html=True)
                st.warning(f"Name: {result[0]}")
            else:
                # Mark as scanned
                c.execute('UPDATE attendance SET scanned = 1, timestamp = ? WHERE roll_number = ?',
                          (datetime.now().isoformat(), roll_number))
                conn.commit()
                
                # Get new count
                c.execute('SELECT COUNT(*) FROM attendance WHERE scanned = 1')
                new_count = c.fetchone()[0]
                
                st.markdown(f'<div class="success-box">✅ VERIFIED<br>{result[0]}<br>Roll: {roll_number}</div>', unsafe_allow_html=True)
                st.success(f"Total Served: {new_count}/{total_count}")
                st.balloons()
                
                # Auto refresh after 2 seconds
                st.rerun()
            
            conn.close()
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a roll number")

st.markdown("---")

# QR Scanner option (if library available)
st.subheader("📱 QR Code Scanner")
st.info("💡 Use the manual entry above or integrate with a QR scanner device")

# Alternative: Use camera input
camera_input = st.camera_input("Or scan QR code with camera")
if camera_input:
    st.info("QR scanning from camera requires additional processing. Use manual entry for now.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>IEEE NEXUS 2026 | Scanner Terminal</p>", unsafe_allow_html=True)
