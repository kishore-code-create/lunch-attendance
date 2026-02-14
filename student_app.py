import streamlit as st
import sqlite3
import qrcode
from io import BytesIO
from datetime import datetime

DB_PATH = 'data/attendance.db'

st.set_page_config(page_title="IEEE NEXUS 2026 - Lunch Token", page_icon="🍽️", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .main {background-color: #f0f2f6;}
    .stButton>button {
        width: 100%;
        background-color: #0066cc;
        color: white;
        height: 3em;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    .success-box {
        padding: 20px;
        background-color: #d4edda;
        border: 2px solid #28a745;
        border-radius: 10px;
        text-align: center;
    }
    .error-box {
        padding: 20px;
        background-color: #f8d7da;
        border: 2px solid #dc3545;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("🍽️ IEEE NEXUS 2026")
st.header("Lunch Token Generator")
st.markdown("---")

# Instructions
with st.expander("📋 Instructions", expanded=False):
    st.write("""
    1. Enter your Roll Number exactly as registered
    2. Click 'Generate Token'
    3. Show the QR code at the lunch counter
    4. Each token can only be used once
    """)

# Input
roll_number = st.text_input("Enter Your Roll Number", placeholder="e.g., 1602-25-735-018", max_chars=20)

if st.button("🎫 Generate Token"):
    if not roll_number:
        st.error("⚠️ Please enter your roll number")
    else:
        roll_number = roll_number.strip()
        
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            
            # Check if roll number exists
            c.execute('SELECT name, scanned FROM attendance WHERE roll_number = ?', (roll_number,))
            result = c.fetchone()
            
            if not result:
                st.markdown('<div class="error-box"><h3>❌ Invalid Roll Number</h3><p>This roll number is not registered for the event.</p></div>', unsafe_allow_html=True)
            elif result[1] == 1:
                st.markdown('<div class="error-box"><h3>⚠️ Already Used</h3><p>This token has already been scanned. You cannot use it again.</p></div>', unsafe_allow_html=True)
            else:
                name = result[0]
                
                # Generate QR code
                qr = qrcode.QRCode(version=1, box_size=10, border=4)
                qr.add_data(roll_number)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                
                # Convert to bytes
                buf = BytesIO()
                img.save(buf, format='PNG')
                byte_im = buf.getvalue()
                
                # Display success
                st.markdown('<div class="success-box"><h3>✅ Token Generated Successfully!</h3></div>', unsafe_allow_html=True)
                st.markdown(f"### Welcome, {name}!")
                st.markdown(f"**Roll Number:** {roll_number}")
                
                st.markdown("---")
                st.markdown("### 📱 Your Lunch Token")
                st.markdown("**Show this QR code at the lunch counter:**")
                
                # Display QR code
                st.image(byte_im, width=300)
                
                st.markdown("---")
                st.info("⚠️ **Important:** This token can only be used once. Do not refresh this page.")
                
            conn.close()
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>IEEE NEXUS 2026 | Lunch Management System</p>", unsafe_allow_html=True)
