-- Flights Table
CREATE TABLE IF NOT EXISTS flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    destination TEXT NOT NULL,
    airline TEXT NOT NULL,
    price INTEGER NOT NULL,
    departure_time TEXT NOT NULL,
    duration INTEGER NOT NULL,
    stops INTEGER NOT NULL
);

-- Bookings Table
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    flight_id INTEGER NOT NULL,
    seat TEXT NOT NULL,
    meal TEXT NOT NULL,
    FOREIGN KEY (flight_id) REFERENCES flights(id)
);

-- User Table
CREATE TABLE IF NOT EXISTS users_preferences(
    session_id TEXT PRIMARY KEY,
    preferred_airline TEXT,
    seat_preference TEXT,
    budget INTEGER
);

