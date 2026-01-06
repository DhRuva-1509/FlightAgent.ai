import json
from database.db import get_connection

# ---------------- DATABASE FUNCTIONS ----------------

def add_flight(source, destination, airline, price, departure_time, duration, stops):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO flights (source, destination, airline, price, departure_time, duration, stops)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (source, destination, airline, price, departure_time, duration, stops))

    conn.commit()
    conn.close()
    return "Flight successfully added."


def get_flights(source=None, destination=None, max_price=None, airline=None):
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT * FROM flights WHERE 1=1"
    params = []

    if source:
        query += " AND source = ?"
        params.append(source)
    if destination:
        query += " AND destination = ?"
        params.append(destination)
    if max_price:
        query += " AND price <= ?"
        params.append(max_price)
    if airline:
        query += " AND airline = ?"
        params.append(airline)

    cur.execute(query, params)
    results = cur.fetchall()
    conn.close()
    return results


def add_booking(name, flight_id, seat, meal):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO bookings (name, flight_id, seat, meal)
        VALUES (?, ?, ?, ?)
    """, (name, flight_id, seat, meal))

    conn.commit()
    conn.close()
    return "Booking confirmed successfully."


def get_bookings_by_name(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT b.id, f.source, f.destination, f.airline, b.seat, b.meal
        FROM bookings b
        JOIN flights f ON b.flight_id = f.id
        WHERE b.name = ?
    """, (name,))

    results = cur.fetchall()
    conn.close()
    return results

# ---------------- TOOL SCHEMAS ----------------

add_flight_function = {
    "name": "add_flight",
    "description": "Add a new flight",
    "parameters": {
        "type": "object",
        "properties": {
            "source": {"type": "string"},
            "destination": {"type": "string"},
            "airline": {"type": "string"},
            "price": {"type": "integer"},
            "departure_time": {"type": "string"},
            "duration": {"type": "integer"},
            "stops": {"type": "integer"},
        },
        "required": ["source", "destination", "airline", "price", "departure_time", "duration", "stops"],
        "additionalProperties": False
    }
}

get_flights_function = {
    "name": "get_flights",
    "description": "Fetch flights with optional filters",
    "parameters": {
        "type": "object",
        "properties": {
            "source": {"type": "string"},
            "destination": {"type": "string"},
            "max_price": {"type": "integer"},
            "airline": {"type": "string"}
        },
        "additionalProperties": False
    }
}

add_booking_function = {
    "name": "add_booking",
    "description": "Book a seat on a flight",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "flight_id": {"type": "integer"},
            "seat": {"type": "string"},
            "meal": {"type": "string"}
        },
        "required": ["flight_id"],
        "additionalProperties": False
    }
}

get_bookings_by_name_function = {
    "name": "get_bookings_by_name",
    "description": "Get bookings by passenger name",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string"}
        },
        "required": ["name"],
        "additionalProperties": False
    }
}

TOOLS = [
    {"type": "function", "function": add_flight_function},
    {"type": "function", "function": get_flights_function},
    {"type": "function", "function": add_booking_function},
    {"type": "function", "function": get_bookings_by_name_function},
]

# ---------------- TOOL HANDLER ----------------

def handle_tool_calls(message):
    responses = []

    for tool_call in message.tool_calls:
        args = json.loads(tool_call.function.arguments)

        if tool_call.function.name == "add_flight":
            add_flight(**args)
            responses.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": "Flight added successfully."
            })

        elif tool_call.function.name == "get_flights":
            rows = get_flights(**args)
            flights = [{
                "id": r[0],
                "source": r[1],
                "destination": r[2],
                "airline": r[3],
                "price": r[4],
                "departure_time": r[5],
                "duration": r[6],
                "stops": r[7],
            } for r in rows]

            responses.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(flights)
            })

        elif tool_call.function.name == "add_booking":
            add_booking(**args)
            responses.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": "Booking confirmed."
            })

        elif tool_call.function.name == "get_bookings_by_name":
            rows = get_bookings_by_name(args["name"])
            bookings = [{
                "booking_id": r[0],
                "source": r[1],
                "destination": r[2],
                "airline": r[3],
                "seat": r[4],
                "meal": r[5],
            } for r in rows]

            responses.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(bookings)
            })

    return responses
