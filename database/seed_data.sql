INSERT INTO flights (source, destination, airline, price, departure_time, duration, stops) VALUES
-- Toronto ↔ Vancouver
('toronto', 'vancouver', 'air canada', 420, '08:00', 300, 0),
('toronto', 'vancouver', 'westjet', 390, '13:30', 305, 0),
('toronto', 'vancouver', 'flair airlines', 250, '06:15', 330, 1),

-- Toronto ↔ Montreal
('toronto', 'montreal', 'porter', 120, '09:00', 75, 0),
('toronto', 'montreal', 'air canada', 150, '17:45', 80, 0),
('toronto', 'montreal', 'westjet', 110, '07:30', 90, 1),

-- Vancouver ↔ Calgary
('vancouver', 'calgary', 'westjet', 140, '10:30', 90, 0),
('vancouver', 'calgary', 'air canada', 160, '19:00', 95, 0),
('vancouver', 'calgary', 'flair airlines', 95, '06:45', 110, 1),

-- Toronto ↔ Calgary
('toronto', 'calgary', 'air canada', 280, '08:45', 260, 0),
('toronto', 'calgary', 'westjet', 260, '15:15', 265, 0),
('toronto', 'calgary', 'air transat', 230, '21:00', 280, 1);
