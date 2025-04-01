# payment.py
class Payment:
    """Represents a payment for a booking."""
    def __init__(self, payment_id, amount, method, status="paid"):
        self._payment_id = payment_id
        self._amount = amount
        self._method = method
        self._status = status

    def __str__(self):
        return f"Payment ID: {self._payment_id}, Amount: ${self._amount}, Method: {self._method}, Status: {self._status}"

    # Getters and setters
    def get_payment_id(self): return self._payment_id
    def set_payment_id(self, payment_id): self._payment_id = payment_id
    def get_amount(self): return self._amount
    def set_amount(self, amount): self._amount = amount
    def get_method(self): return self._method
    def set_method(self, method): self._method = method
    def get_status(self): return self._status
    def set_status(self, status): self._status = status