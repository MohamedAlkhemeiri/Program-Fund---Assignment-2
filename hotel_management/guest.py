# guest.py
from person import Person

class Guest(Person):
    """Represents a hotel guest."""
    def __init__(self, name, contact, email, loyalty_id, points=0):
        super().__init__(name, contact, email)
        self._loyalty_id = loyalty_id
        self._points = points

    def __str__(self):
        return f"{super().__str__()}, Loyalty ID: {self._loyalty_id}, Points: {self._points}"

    # Getters and setters
    def get_loyalty_id(self): return self._loyalty_id
    def set_loyalty_id(self, loyalty_id): self._loyalty_id = loyalty_id
    def get_points(self): return self._points
    def set_points(self, points): self._points = points