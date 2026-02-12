import sqlite3  
from pathlib import Path
DB_PATH = Path(__file__).parent / 'radio.db'
def get_connection():
    return sqlite3.connect(DB_PATH)



def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS spots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            callsign TEXT,
            frequency REAL,
            band TEXT,
            mode TEXT,
            created_at TEXT,
            source TEXT
        )
    """)

    conn.commit()
    conn.close()
