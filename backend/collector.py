import random
from datetime import datetime
from db import get_connection


BANDS = ["HF", "VHF", "UHF"]
MODES = ["SSB", "CW", "FT8"]
CALLSIGNS = ["K1ABC", "DL7XYZ", "4L1AAA", "JA2BCD"]


def collect_spot():
    return {
        "callsign": random.choice(CALLSIGNS),
        "frequency": round(random.uniform(3.5, 145.0), 3),
        "band": random.choice(BANDS),
        "mode": random.choice(MODES),
        "created_at": datetime.utcnow().isoformat(),
        "source": "mock"
    }


def save_spot(spot):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO spots (callsign, frequency, band, mode, created_at, source)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        spot["callsign"],
        spot["frequency"],
        spot["band"],
        spot["mode"],
        spot["created_at"],
        spot["source"]
    ))

    conn.commit()
    conn.close()


def run():
    spot = collect_spot()
    save_spot(spot)
    print("Saved:", spot)
