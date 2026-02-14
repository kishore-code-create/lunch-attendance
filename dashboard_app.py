import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import time

DB_PATH = 'data/attendance.db'

st.set_page_config(page_title="Admin Dashboard", page_icon="📊", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stButton>button {
        background-color: #dc3545;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("📊 Admin Dashboard - IEEE NEXUS 2026")
st.markdown("### Lunch Attendance Management")
st.markdown("---")

# Auto-refresh toggle
auto_refresh = st.sidebar.checkbox("🔄 Auto Refresh (5s)", value=False)

# Get data
def get_all_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM attendance ORDER BY scanned DESC, name", conn)
    conn.close()
    return df

df = get_all_data()

# Statistics
total = len(df)
scanned = len(df[df['scanned'] == 1])
remaining = total - scanned
percentage = (scanned / total * 100) if total > 0 else 0

# Display metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Total Registered", total)
with col2:
    st.metric("✅ Served", scanned, delta=f"{percentage:.1f}%")
with col3:
    st.metric("⏳ Remaining", remaining)
with col4:
    st.metric("🕐 Last Update", datetime.now().strftime("%H:%M:%S"))

st.markdown("---")

# Progress bar
st.subheader("📈 Progress")
st.progress(scanned / total if total > 0 else 0)
st.write(f"**{scanned} out of {total}** people have been served lunch")

st.markdown("---")

# Tabs
tab1, tab2, tab3 = st.tabs(["📋 All Attendees", "✅ Served", "⏳ Pending"])

with tab1:
    st.subheader("All Registered Attendees")
    
    # Search
    search = st.text_input("🔍 Search by Name or Roll Number")
    if search:
        filtered_df = df[df['name'].str.contains(search, case=False, na=False) | 
                        df['roll_number'].str.contains(search, case=False, na=False)]
    else:
        filtered_df = df
    
    # Display table
    display_df = filtered_df.copy()
    display_df['Status'] = display_df['scanned'].apply(lambda x: '✅ Served' if x == 1 else '⏳ Pending')
    display_df['Timestamp'] = display_df['timestamp'].fillna('-')
    
    st.dataframe(
        display_df[['roll_number', 'name', 'Status', 'Timestamp']],
        use_container_width=True,
        height=400
    )
    
    # Download button
    csv = display_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Full Report (CSV)",
        data=csv,
        file_name=f"lunch_attendance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

with tab2:
    st.subheader("✅ Served Attendees")
    served_df = df[df['scanned'] == 1].copy()
    served_df['Served At'] = pd.to_datetime(served_df['timestamp']).dt.strftime('%H:%M:%S')
    
    st.dataframe(
        served_df[['roll_number', 'name', 'Served At']],
        use_container_width=True,
        height=400
    )
    
    st.info(f"Total: {len(served_df)} people served")

with tab3:
    st.subheader("⏳ Pending Attendees")
    pending_df = df[df['scanned'] == 0]
    
    st.dataframe(
        pending_df[['roll_number', 'name']],
        use_container_width=True,
        height=400
    )
    
    st.warning(f"Total: {len(pending_df)} people pending")

st.markdown("---")

# Admin actions
st.subheader("⚙️ Admin Actions")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Refresh Data"):
        st.rerun()

with col2:
    if st.button("⚠️ Reset All Attendance", type="secondary"):
        if st.session_state.get('confirm_reset', False):
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute('UPDATE attendance SET scanned = 0, timestamp = NULL')
            conn.commit()
            conn.close()
            st.success("✅ All attendance records reset!")
            st.session_state.confirm_reset = False
            time.sleep(1)
            st.rerun()
        else:
            st.session_state.confirm_reset = True
            st.warning("⚠️ Click again to confirm reset")

# Recent activity
st.markdown("---")
st.subheader("🕐 Recent Activity (Last 10)")
recent_df = df[df['scanned'] == 1].sort_values('timestamp', ascending=False).head(10)
if len(recent_df) > 0:
    recent_df['Time'] = pd.to_datetime(recent_df['timestamp']).dt.strftime('%H:%M:%S')
    st.dataframe(
        recent_df[['Time', 'roll_number', 'name']],
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("No activity yet")

# Auto refresh
if auto_refresh:
    time.sleep(5)
    st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>IEEE NEXUS 2026 | Admin Dashboard</p>", unsafe_allow_html=True)
