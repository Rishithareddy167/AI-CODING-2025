-- (Removed T-SQL fragments that were SQL Server specific: IDENTITY, GETDATE, PRINT, stray ORDER BY etc.)
-- The remainder of this file is a MySQL-compatible schema and queries.
-- MySQL-compatible Hotel Reservation schema, sample data, and queries

DROP TABLE IF EXISTS Bookings;
DROP TABLE IF EXISTS Rooms;
DROP TABLE IF EXISTS Guests;

CREATE TABLE Guests (
    GuestID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(20) NOT NULL,
    Address VARCHAR(200),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(10),
    Country VARCHAR(50),
    DateOfBirth DATE,
    CreatedDate DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY,
    RoomNumber VARCHAR(10) NOT NULL UNIQUE,
    RoomType VARCHAR(50) NOT NULL,
    Capacity INT NOT NULL,
    PricePerNight DECIMAL(10,2) NOT NULL,
    Description TEXT,
    Amenities TEXT,
    Floor INT,
    Status VARCHAR(20) DEFAULT 'Available',
    CreatedDate DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    GuestID INT NOT NULL,
    RoomID INT NOT NULL,
    CheckInDate DATE NOT NULL,
    CheckOutDate DATE NOT NULL,
    NumberOfGuests INT NOT NULL,
    TotalPrice DECIMAL(10,2),
    BookingStatus VARCHAR(20) DEFAULT 'Confirmed',
    SpecialRequests TEXT,
    CreatedDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (GuestID) REFERENCES Guests(GuestID),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID),
    CHECK (CheckOutDate > CheckInDate),
    CHECK (NumberOfGuests > 0)
);

-- Sample data
INSERT INTO Guests (FirstName, LastName, Email, PhoneNumber, Address, City, State, ZipCode, Country, DateOfBirth)
VALUES
  ('John','Smith','john.smith@email.com','555-0101','123 Main Street','New York','NY','10001','USA','1980-05-15'),
  ('Emily','Johnson','emily.johnson@email.com','555-0102','456 Oak Avenue','Los Angeles','CA','90001','USA','1990-07-22'),
  ('Michael','Brown','michael.brown@email.com','555-0103','789 Pine Road','Chicago','IL','60601','USA','1985-03-10'),
  ('Sarah','Davis','sarah.davis@email.com','555-0104','321 Elm Street','Houston','TX','77001','USA','1992-11-30'),
  ('Robert','Wilson','robert.wilson@email.com','555-0105','654 Maple Drive','Phoenix','AZ','85001','USA','1975-09-18'),
  ('Jennifer','Martinez','jennifer.martinez@email.com','555-0106','987 Cedar Lane','Philadelphia','PA','19101','USA','1988-02-14'),
  ('David','Anderson','david.anderson@email.com','555-0107','147 Birch Court','San Antonio','TX','78201','USA','1983-08-25'),
  ('Jessica','Taylor','jessica.taylor@email.com','555-0108','258 Spruce Way','San Diego','CA','92101','USA','1995-01-05');

INSERT INTO Rooms (RoomNumber, RoomType, Capacity, PricePerNight, Description, Amenities, Floor, Status)
VALUES
  ('101','Single',1,79.99,'Cozy single bedroom with modern amenities','TV, WiFi, Air Conditioning, Private Bathroom',1,'Available'),
  ('102','Single',1,79.99,'Comfortable single room with city view','TV, WiFi, Air Conditioning, Private Bathroom',1,'Available'),
  ('103','Double',2,129.99,'Spacious double bedroom with king-size bed','TV, WiFi, Air Conditioning, Private Bathroom, Mini Fridge',1,'Occupied'),
  ('104','Double',2,129.99,'Luxurious double room with garden view','TV, WiFi, Air Conditioning, Private Bathroom, Mini Fridge, Balcony',1,'Available'),
  ('201','Suite',4,199.99,'Elegant suite with separate living area','TV, WiFi, Air Conditioning, Private Bathroom, Kitchenette, Sofa, Balcony',2,'Available'),
  ('202','Suite',4,199.99,'Premium suite with ocean view','TV, WiFi, Air Conditioning, Private Bathroom, Kitchenette, Sofa, Balcony, Jacuzzi',2,'Available'),
  ('203','Deluxe',6,299.99,'Luxurious deluxe room with all amenities','TV, WiFi, Air Conditioning, Private Bathroom, Kitchenette, Sofa, Balcony, Jacuzzi, Gym Access',2,'Available'),
  ('301','Double',2,139.99,'Modern double room with contemporary design','TV, WiFi, Air Conditioning, Private Bathroom, Mini Fridge',3,'Available'),
  ('302','Single',1,89.99,'Premium single room with executive lounge access','TV, WiFi, Air Conditioning, Private Bathroom, Work Desk',3,'Available'),
  ('303','Suite',4,219.99,'Executive suite with full amenities','TV, WiFi, Air Conditioning, Private Bathroom, Kitchenette, Sofa, Balcony, Work Area',3,'Occupied');

INSERT INTO Bookings (GuestID, RoomID, CheckInDate, CheckOutDate, NumberOfGuests, TotalPrice, BookingStatus, SpecialRequests)
VALUES
  (1,3,'2025-11-15','2025-11-18',2,389.97,'Confirmed','High floor room preferred'),
  (2,1,'2025-11-20','2025-11-25',1,399.95,'Confirmed','Early breakfast required'),
  (3,5,'2025-11-22','2025-11-26',4,799.96,'Confirmed','Welcome champagne requested'),
  (4,10,'2025-11-18','2025-11-20',2,439.98,'Confirmed','Late checkout needed'),
  (5,2,'2025-12-01','2025-12-05',1,319.96,'Confirmed','Room near elevator'),
  (6,6,'2025-12-03','2025-12-08',4,999.95,'Confirmed','Honeymoon suite decoration'),
  (7,4,'2025-12-10','2025-12-13',2,389.97,'Confirmed','No disturbance'),
  (8,7,'2025-12-15','2025-12-20',5,1499.95,'Confirmed','Family gathering event');

-- Query: find available rooms between dates
SET @CheckInDate = '2025-11-20';
SET @CheckOutDate = '2025-11-25';

SELECT r.RoomID, r.RoomNumber, r.RoomType, r.Capacity, r.PricePerNight, r.Description, r.Amenities, r.Floor, r.Status,
       DATEDIFF(@CheckOutDate, @CheckInDate) AS NumberOfNights,
       (r.PricePerNight * DATEDIFF(@CheckOutDate, @CheckInDate)) AS TotalPrice
FROM Rooms r
WHERE r.Status = 'Available'
  AND NOT EXISTS (
    SELECT 1 FROM Bookings b
    WHERE b.RoomID = r.RoomID
      AND b.BookingStatus IN ('Confirmed','Completed')
      AND b.CheckInDate < @CheckOutDate
      AND b.CheckOutDate > @CheckInDate
  )
ORDER BY r.Floor, r.RoomNumber;

-- Availability with details
SET @CheckInDate2 = '2025-11-28';
SET @CheckOutDate2 = '2025-12-02';

SELECT r.RoomID, r.RoomNumber, r.RoomType, r.Capacity, r.PricePerNight,
       DATEDIFF(@CheckOutDate2,@CheckInDate2) AS NumberOfNights,
       (r.PricePerNight * DATEDIFF(@CheckOutDate2,@CheckInDate2)) AS EstimatedTotal,
       CASE WHEN r.Capacity >= 4 THEN 'Great for families'
            WHEN r.Capacity >= 2 THEN 'Perfect for couples'
            ELSE 'Ideal for solo travelers' END AS RecommendedFor
FROM Rooms r
WHERE r.Status = 'Available'
  AND NOT EXISTS (
    SELECT 1 FROM Bookings b
    WHERE b.RoomID = r.RoomID
      AND b.BookingStatus IN ('Confirmed','Completed')
      AND b.CheckInDate < @CheckOutDate2
      AND b.CheckOutDate > @CheckInDate2
  )
ORDER BY r.PricePerNight ASC;

-- Find available rooms by type
SET @CheckInDate3 = '2025-12-05';
SET @CheckOutDate3 = '2025-12-10';
SET @RoomType = 'Suite';

SELECT r.RoomID, r.RoomNumber, r.RoomType, r.Capacity, r.PricePerNight, r.Floor, r.Amenities
FROM Rooms r
WHERE r.RoomType = @RoomType
  AND r.Status = 'Available'
  AND NOT EXISTS (
    SELECT 1 FROM Bookings b
    WHERE b.RoomID = r.RoomID
      AND b.BookingStatus IN ('Confirmed','Completed')
      AND b.CheckInDate < @CheckOutDate3
      AND b.CheckOutDate > @CheckInDate3
  )
ORDER BY r.PricePerNight ASC;

-- Room availability summary
SET @CheckInDate4 = '2025-11-20';
SET @CheckOutDate4 = '2025-11-30';

SELECT r.RoomType,
       COUNT(r.RoomID) AS TotalRooms,
       SUM(CASE WHEN r.Status = 'Available'
                AND NOT EXISTS (SELECT 1 FROM Bookings b WHERE b.RoomID = r.RoomID
                                AND b.BookingStatus IN ('Confirmed','Completed')
                                AND b.CheckInDate < @CheckOutDate4
                                AND b.CheckOutDate > @CheckInDate4)
                THEN 1 ELSE 0 END) AS AvailableRooms,
       SUM(CASE WHEN EXISTS (SELECT 1 FROM Bookings b WHERE b.RoomID = r.RoomID
                              AND b.BookingStatus IN ('Confirmed','Completed')
                              AND b.CheckInDate < @CheckOutDate4
                              AND b.CheckOutDate > @CheckInDate4)
                THEN 1 ELSE 0 END) AS BookedRooms,
       AVG(r.PricePerNight) AS AveragePricePerNight
FROM Rooms r
GROUP BY r.RoomType
ORDER BY r.RoomType;

-- Guest booking history
SELECT g.GuestID, CONCAT(g.FirstName,' ',g.LastName) AS GuestName, g.Email,
       COUNT(b.BookingID) AS TotalBookings,
       MAX(b.CheckInDate) AS LastBookingDate,
       SUM(b.TotalPrice) AS TotalSpent
FROM Guests g
LEFT JOIN Bookings b ON g.GuestID = b.GuestID AND b.BookingStatus = 'Confirmed'
GROUP BY g.GuestID, g.FirstName, g.LastName, g.Email
ORDER BY TotalSpent DESC;

-- Revenue analysis (monthly)
SELECT DATE_FORMAT(b.CheckInDate, '%Y-%m') AS `Month`,
       COUNT(b.BookingID) AS TotalBookings,
       SUM(b.TotalPrice) AS TotalRevenue,
       AVG(b.TotalPrice) AS AverageBookingValue,
       AVG(DATEDIFF(b.CheckOutDate,b.CheckInDate)) AS AverageStayLength
FROM Bookings b
WHERE b.BookingStatus IN ('Confirmed','Completed')
GROUP BY DATE_FORMAT(b.CheckInDate, '%Y-%m')
ORDER BY `Month` DESC;

-- Stored procedure: check room availability
DELIMITER $$
CREATE PROCEDURE sp_CheckRoomAvailability(
  IN pCheckInDate DATE,
  IN pCheckOutDate DATE,
  IN pRoomType VARCHAR(50),
  IN pMinCapacity INT
)
BEGIN
  SELECT r.RoomID, r.RoomNumber, r.RoomType, r.Capacity, r.PricePerNight, r.Description, r.Amenities, r.Floor,
         DATEDIFF(pCheckOutDate,pCheckInDate) AS NumberOfNights,
         (r.PricePerNight * DATEDIFF(pCheckOutDate,pCheckInDate)) AS TotalPrice
  FROM Rooms r
  WHERE r.Capacity >= pMinCapacity
    AND (pRoomType IS NULL OR r.RoomType = pRoomType)
    AND r.Status = 'Available'
    AND NOT EXISTS (
      SELECT 1 FROM Bookings b
      WHERE b.RoomID = r.RoomID
        AND b.BookingStatus IN ('Confirmed','Completed')
        AND b.CheckInDate < pCheckOutDate
        AND b.CheckOutDate > pCheckInDate
    )
  ORDER BY r.PricePerNight ASC, r.RoomNumber;
END$$
DELIMITER ;

-- Stored procedure: make a booking
DELIMITER $$
CREATE PROCEDURE sp_MakeBooking(
  IN pGuestID INT,
  IN pRoomID INT,
  IN pCheckInDate DATE,
  IN pCheckOutDate DATE,
  IN pNumberOfGuests INT,
  IN pSpecialRequests TEXT,
  OUT pBookingID INT
)
BEGIN
  DECLARE vRoomPrice DECIMAL(10,2);
  DECLARE vNumberOfNights INT;
  DECLARE vTotalPrice DECIMAL(10,2);

  SELECT PricePerNight INTO vRoomPrice FROM Rooms WHERE RoomID = pRoomID;
  SET vNumberOfNights = DATEDIFF(pCheckOutDate,pCheckInDate);
  SET vTotalPrice = vRoomPrice * vNumberOfNights;

  INSERT INTO Bookings (GuestID, RoomID, CheckInDate, CheckOutDate, NumberOfGuests, TotalPrice, BookingStatus, SpecialRequests)
  VALUES (pGuestID, pRoomID, pCheckInDate, pCheckOutDate, pNumberOfGuests, vTotalPrice, 'Confirmed', pSpecialRequests);

  SET pBookingID = LAST_INSERT_ID();
END$$
DELIMITER ;

-- View: active bookings
CREATE OR REPLACE VIEW vw_ActiveBookings AS
-- Note: apply COLLATE on text concatenation to avoid "Illegal mix of collations" errors
SELECT b.BookingID,
       CONCAT(
         g.FirstName COLLATE utf8mb4_unicode_ci,
         ' ' COLLATE utf8mb4_unicode_ci,
         g.LastName COLLATE utf8mb4_unicode_ci
       ) AS GuestName,
       r.RoomNumber, r.RoomType, b.CheckInDate, b.CheckOutDate,
       DATEDIFF(b.CheckOutDate,b.CheckInDate) AS StayDuration, b.TotalPrice, b.BookingStatus
FROM Bookings b
JOIN Guests g ON b.GuestID = g.GuestID
JOIN Rooms r ON b.RoomID = r.RoomID
WHERE b.BookingStatus = 'Confirmed' AND b.CheckOutDate >= CURDATE();

-- Quick test: select active bookings
SELECT * FROM vw_ActiveBookings ORDER BY CheckInDate;
