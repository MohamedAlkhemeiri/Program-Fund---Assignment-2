# invoice.py
class Invoice:
    """Represents an invoice for a booking."""
    def __init__(self, invoice_id, booking, items, total):
        self._invoice_id = invoice_id
        self._booking = booking
        self._items = items
        self._total = total

    def __str__(self):
        return f"Invoice ID: {self._invoice_id}, Booking: {self._booking.get_booking_id()}, Items: {self._items}, Total: ${self._total}"

    # Getters and setters
    def get_invoice_id(self): return self._invoice_id
    def set_invoice_id(self, invoice_id): self._invoice_id = invoice_id
    def get_booking(self): return self._booking
    def set_booking(self, booking): self._booking = booking
    def get_items(self): return self._items
    def set_items(self, items): self._items = items
    def get_total(self): return self._total
    def set_total(self, total): self._total = total