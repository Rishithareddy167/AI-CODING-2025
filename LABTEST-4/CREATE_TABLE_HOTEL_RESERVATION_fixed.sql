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

-- Insert a small set of sample data (expand as needed)
INSERT INTO Guests (FirstName, LastName, Email, PhoneNumber, City, State, Country, DateOfBirth)
VALUES
  ('John','Smith','john.smith@example.com','555-0101','New York','NY','USA','1980-05-15'),
  ('Emily','Johnson','emily.johnson@example.com','555-0102','Los Angeles','CA','USA','1990-07-22');

INSERT INTO Rooms (RoomNumber, RoomType, Capacity, PricePerNight, Description, Amenities, Floor, Status)
VALUES
  ('101','Single',1,79.99,'Cozy single room','TV, WiFi, AC',1,'Available'),
  ('102','Double',2,129.99,'Double room with queen bed','TV, WiFi, AC, Mini Fridge',1,'Available');

INSERT INTO Bookings (GuestID, RoomID, CheckInDate, CheckOutDate, NumberOfGuests, TotalPrice, BookingStatus)
VALUES
  (1,2,'2025-11-15','2025-11-18',2,389.97,'Confirmed');

-- Example: find available rooms between two dates (replace literals with parameters in your client)
SET @CheckInDate = '2025-11-20';
SET @CheckOutDate = '2025-11-25';

SELECT r.RoomID, r.RoomNumber, r.RoomType, r.Capacity, r.PricePerNight,
       DATEDIFF(@CheckOutDate,@CheckInDate) AS NumberOfNights,
       (r.PricePerNight * DATEDIFF(@CheckOutDate,@CheckInDate)) AS TotalPrice
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

-- Stored procedure: check room availability (example)
DELIMITER $$
CREATE PROCEDURE sp_CheckRoomAvailability(
  IN pCheckInDate DATE,
  IN pCheckOutDate DATE,
  IN pRoomType VARCHAR(50)
)
BEGIN
  SELECT r.*
  FROM Rooms r
  WHERE (pRoomType IS NULL OR r.RoomType = pRoomType)
    AND r.Status = 'Available'
    AND NOT EXISTS (
      SELECT 1 FROM Bookings b
      WHERE b.RoomID = r.RoomID
        AND b.BookingStatus IN ('Confirmed','Completed')
        AND b.CheckInDate < pCheckOutDate
        AND b.CheckOutDate > pCheckInDate
    )
  ORDER BY r.PricePerNight, r.RoomNumber;
END$$
DELIMITER ;

-- View: active bookings
CREATE OR REPLACE VIEW vw_ActiveBookings AS
SELECT b.BookingID, CONCAT(g.FirstName,' ',g.LastName) AS GuestName, r.RoomNumber, r.RoomType, b.CheckInDate, b.CheckOutDate,
       DATEDIFF(b.CheckOutDate,b.CheckInDate) AS StayDuration, b.TotalPrice, b.BookingStatus
FROM Bookings b
JOIN Guests g ON b.GuestID = g.GuestID
JOIN Rooms r ON b.RoomID = r.RoomID
WHERE b.BookingStatus = 'Confirmed' AND b.CheckOutDate >= CURDATE();

-- Quick test: select active bookings
SELECT * FROM vw_ActiveBookings ORDER BY CheckInDate;
