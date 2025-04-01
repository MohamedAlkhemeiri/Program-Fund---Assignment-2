# staff.py
from person import Person

class Staff(Person):
    """Represents hotel staff."""
    def __init__(self, name, contact, email, staff_id, position):
        super().__init__(name, contact, email)
        self._staff_id = staff_id
        self._position = position

    def __str__(self):
        return f"{super().__str__()}, Staff ID: {self._staff_id}, Position: {self._position}"

    # Getters and setters
    def get_staff_id(self): return self._staff_id
    def set_staff_id(self, staff_id): self._staff_id = staff_id
    def get_position(self): return self._position
    def set_position(self, position): self._position = position