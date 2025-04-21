import unittest
from io import StringIO
import sys
from unittest.mock import patch

from cinema.lib.seat_allocator import SeatMap

class TestSeatMap(unittest.TestCase):

    def setUp(self):
        self.seat_map = SeatMap(5, 5)

    def test_initial_available_count(self):
        self.assertEqual(self.seat_map.available_count(), 25)

    def test_reserve_seats_successfully(self):
        self.seat_map.reserve([(1, 1), (1, 2)])
        self.assertEqual(self.seat_map.available_count(), 23)

    def test_is_available_true(self):
        self.assertTrue(self.seat_map.is_available(3, 3))

    def test_is_available_false(self):
        self.seat_map.reserve([(3, 3)])
        self.assertFalse(self.seat_map.is_available(3, 3))

    def test_find_best_seats_basic(self):
        seats = self.seat_map.find_best_seats(3)
        self.assertEqual(len(seats), 3)

    def test_allocate_from_successful(self):
        seats = self.seat_map.allocate_from(1, 1, 2)
        self.assertEqual(seats, [(1, 1), (1, 2)])

    def test_allocate_from_not_enough_seats(self):
        self.seat_map.reserve([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)])
        seats = self.seat_map.allocate_from(1, 1, 2)
        self.assertEqual(seats, [(2, 1), (2, 2)])  # Should move to next row

if __name__ == "__main__":
    unittest.main()