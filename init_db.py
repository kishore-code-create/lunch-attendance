import sqlite3
import pandas as pd
import os

DB_PATH = 'data/attendance.db'

def init_database(excel_path):
    """Initialize database with roll numbers from Excel file"""
    
    # Read Excel file
    df = pd.read_excel(excel_path)
    
    # Clean roll numbers (remove extra spaces)
    df['Roll Number'] = df['Roll Number'].str.strip()
    
    # Create database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS attendance
                 (roll_number TEXT PRIMARY KEY, 
                  name TEXT,
                  timestamp TEXT,
                  scanned INTEGER DEFAULT 0)''')
    
    # Clear existing data
    c.execute('DELETE FROM attendance')
    
    # Insert roll numbers
    for _, row in df.iterrows():
        c.execute('INSERT INTO attendance (roll_number, name, scanned) VALUES (?, ?, 0)', 
                  (row['Roll Number'], row['Name ']))
    
    conn.commit()
    conn.close()
    
    print(f"Database initialized with {len(df)} roll numbers")

if __name__ == "__main__":
    excel_file = "../Registrations for IEEE NEXUS 2026 (Responses) (1).xlsx"
    if os.path.exists(excel_file):
        init_database(excel_file)
    else:
        print(f"Excel file not found: {excel_file}")
