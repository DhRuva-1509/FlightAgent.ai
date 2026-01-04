import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "flights.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def search_flights(source=None, destination=None, max_price=None, airline=None, directlyOnly=False):
    query = "SELECT * FROM flights WHERE 1=1"
    params = []

    if source:
        query += " AND source = ?"
        params.append(source.lower())
    
    if destination:
        query += " AND destination = ?"
        params.append(destination.lower())
    
    if max_price:
        query += " AND price <= ?"
        params.append(max_price)
    
    if airline:
        query += " AND airline = ?"
        params.append(airline.lower())
    
    if directlyOnly:
        query += " AND stops = 0"

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
    
    return rows

def get_flight_by_id(flight_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM flights WHERE id = ?",
            (flight_id,)
        )
        return cursor.fetchone()


def get_booking_history():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT b.id, b.name, f.source, f.destination, f.airline, f.price, b.booking_time
            FROM bookings b
            JOIN flights f ON b.flight_id = f.id
            ORDER BY b.booking_time DESC
        """)
        return cursor.fetchall()
    