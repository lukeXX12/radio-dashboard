from db import get_connection


def spots_last_minutes(minutes=15):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"""
        SELECT COUNT(*) FROM spots
        WHERE created_at >= datetime('now', '-{minutes} minutes')
    """)

    count = cur.fetchone()[0]
    conn.close()
    return count


def spots_by_band():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT band, COUNT(*) as cnt
        FROM spots
        GROUP BY band
        ORDER BY cnt DESC
    """)

    rows = cur.fetchall()
    conn.close()

    return [{"band": r[0], "count": r[1]} for r in rows]
