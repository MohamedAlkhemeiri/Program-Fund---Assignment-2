# room.py
class Room:
    """Represents a hotel room."""
    def __init__(self, number, room_type, amenities, price, available=True):
        self._number = number
        self._type = room_type
        self._amenities = amenities
        self._price = price
        self._available = available

    def __str__(self):
        return f"Room {self._number} ({self._type}), Amenities: {self._amenities}, Price: ${self._price}, Available: {self._available}"

    # Getters and setters
    def get_number(self): return self._number
    def set_number(self, number): self._number = number
    def get_type(self): return self._type
    def set_type(self, room_type): self._type = room_type
    def get_amenities(self): return self._amenities
    def set_amenities(self, amenities): self._amenities = amenities
    def get_price(self): return self._price
    def set_price(self, price): self._price = price
    def is_available(self): return self._available
    def set_available(self, available): self._available = available