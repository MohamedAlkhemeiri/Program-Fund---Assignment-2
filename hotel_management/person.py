# person.py
class Person:
    """Base class for people (guests, staff)."""
    def __init__(self, name, contact, email):
        self._name = name
        self._contact = contact
        self._email = email

    def __str__(self):
        return f"Name: {self._name}, Contact: {self._contact}, Email: {self._email}"

    # Getters and setters
    def get_name(self): return self._name
    def set_name(self, name): self._name = name
    def get_contact(self): return self._contact
    def set_contact(self, contact): self._contact = contact
    def get_email(self): return self._email
    def set_email(self, email): self._email = email