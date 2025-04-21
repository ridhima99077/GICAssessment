import unittest
from cinema.lib.booking_manager import BookingManager

class TestBookingManager(unittest.TestCase):

    def setUp(self):
        self.manager = BookingManager()

    def test_generate_booking_id(self):
        id1 = self.manager.generate_id()
        id2 = self.manager.generate_id()
        self.assertEqual(id1, "GIC0001")
        self.assertEqual(id2, "GIC0002")

    def test_add_and_get_booking(self):
        self.manager.add_booking("GIC0001", [(1, 1), (1, 2)])
        seats = self.manager.get_booking("GIC0001")
        self.assertEqual(seats, [(1, 1), (1, 2)])

    def test_get_nonexistent_booking(self):
        self.assertIsNone(self.manager.get_booking("GIC9999"))

if __name__ == "__main__":
    unittest.main()
