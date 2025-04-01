# room_inventory.py
class RoomInventory:
    """Manages the hotel's room inventory."""
    def __init__(self, rooms=None):
        self._rooms = rooms or []

    def add_room(self, room):
        self._rooms.append(room)

    def find_available_rooms(self, check_in_date, check_out_date, room_type=None, amenities=None):
        available_rooms = []
        for room in self._rooms:
            if room.is_available():
                if room_type and room.get_type() != room_type:
                    continue
                if amenities and not all(amenity in room.get_amenities() for amenity in amenities):
                    continue
                available_rooms.append(room)
        return available_rooms

    def __str__(self):
        return f"Room Inventory: {len(self._rooms)} rooms"