# booking.py
from datetime import date

class Booking:
    """Represents a room booking."""
    def __init__(self, booking_id, guest, room, check_in, check_out, status="confirmed"):
        self._booking_id = booking_id
        self._guest = guest
        self._room = room
        self._check_in = check_in
        self._check_out = check_out
        self._status = status

    def __str__(self):
        return f"Booking ID: {self._booking_id}, Guest: {self._guest.get_name()}, Room: {self._room.get_number()}, Check-in: {self._check_in}, Check-out: {self._check_out}, Status: {self._status}"

    # Getters and setters
    def get_booking_id(self): return self._booking_id
    def set_booking_id(self, booking_id): self._booking_id = booking_id
    def get_guest(self): return self._guest
    def set_guest(self, guest): self._guest = guest
    def get_room(self): return self._room
    def set_room(self, room): self._room = room
    def get_check_in(self): return self._check_in
    def set_check_in(self, check_in): self._check_in = check_in
    def get_check_out(self): return self._check_out
    def set_check_out(self, check_out): self._check_out = check_out
    def get_status(self): return self._status
    def set_status(self, status): self._status = status