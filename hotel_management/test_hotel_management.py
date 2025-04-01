# test_hotel_management.py
import unittest
from datetime import date
from hotel_management.person import Person
from hotel_management.guest import Guest
from hotel_management.staff import Staff
from hotel_management.room import Room
from hotel_management.booking import Booking
from hotel_management.payment import Payment
from hotel_management.invoice import Invoice
from hotel_management.service import Service
from hotel_management.room_inventory import RoomInventory

class TestHotelManagement(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.guest1 = Guest("Mohamed", "123-456-7890", "mohamed@example.com", "G123")
        self.guest2 = Guest("Bob", "987-654-3210", "bob@example.com", "G456")
        self.staff1 = Staff("Charlie", "111-222-3333", "charlie@hotel.com", "S001", "Manager")
        self.staff2 = Staff("David", "444-555-6666", "david@hotel.com", "S002", "Housekeeping")
        self.room1 = Room(101, "Single", ["Wi-Fi", "TV"], 100.00)
        self.room2 = Room(102, "Double", ["Wi-Fi", "TV", "Mini-bar"], 150.00)
        self.booking1 = Booking("B001", self.guest1, self.room1, date(2024, 10, 20), date(2024, 10, 25))
        self.payment1 = Payment("P001", 500.00, "Credit Card")
        self.invoice1 = Invoice("I001", self.booking1, ["Room (5 nights)", "Wi-Fi"], 500.00)
        self.service1 = Service("S001", "Housekeeping")
        self.inventory = RoomInventory([self.room1, self.room2])

    def test_guest_account_creation(self):
        self.assertEqual(self.guest1.get_name(), "Mohamed")
        self.assertEqual(self.guest1.get_loyalty_id(), "G123")
        self.assertEqual(self.guest2.get_name(), "Bob")
        self.assertEqual(self.guest2.get_loyalty_id(), "G456")

    def test_search_available_rooms(self):
        available_rooms = self.inventory.find_available_rooms(date(2024, 10, 20), date(2024, 10, 25))
        self.assertEqual(len(available_rooms), 2)
        available_single_rooms = self.inventory.find_available_rooms(date(2024, 10, 20), date(2024, 10, 25), room_type="Single")
        self.assertEqual(len(available_single_rooms), 1)

    def test_making_room_reservation(self):
        booking = Booking("B002", self.guest2, self.room2, date(2024, 11, 1), date(2024, 11, 5))
        self.assertEqual(booking.get_booking_id(), "B002")
        self.assertEqual(booking.get_guest(), self.guest2)

    def test_booking_confirmation_notification(self):
        # Simulate sending a confirmation email (not implemented here)
        print("Booking confirmation sent for Booking ID: B001")
        print("Booking confirmation sent for Booking ID: B002")

    def test_invoice_generation_for_booking(self):
        invoice = Invoice("I002", self.booking1, ["Room (5 nights)", "Wi-Fi", "Mini-bar"], 750.00)
        self.assertEqual(invoice.get_total(), 750.00)
        self.assertEqual(invoice.get_booking(), self.booking1)

    def test_processing_payment_methods(self):
        payment = Payment("P002", 750.00, "Mobile Wallet")
        self.assertEqual(payment.get_method(), "Mobile Wallet")
        self.assertEqual(payment.get_amount(), 750.00)

    def test_displaying_reservation_history(self):
        print(f"Reservation History for {self.guest1.get_name()}:")
        print(self.booking1)
        print(f"Reservation History for {self.guest2.get_name()}:")
        print(Booking("B002", self.guest2, self.room2, date(2024, 11, 1), date(2024, 11, 5)))

    def test_cancellation_of_reservation(self):
        self.booking1.set_status("cancelled")
        self.room1.set_available(True)  # Room becomes available again
        print(f"Booking {self.booking1.get_booking_id()} cancelled.")
        print(f"Room {self.room1.get_number()} is now available.")

if __name__ == '__main__':
    unittest.main()