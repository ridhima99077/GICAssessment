import unittest
from unittest.mock import patch
from cinema.lib.cinema import Cinema

class TestCinema(unittest.TestCase):

    def setUp(self):
        self.cinema = Cinema("Test Movie", 5, 5)

    @patch('cinema.ui.console_interface.ConsoleUI.input_ticket_count', return_value=2)
    @patch('cinema.ui.console_interface.ConsoleUI.input_seat_position', return_value='')
    def test_book_tickets_success_default_selection(self, mock_seat_input, mock_ticket_input):
        self.cinema.book_tickets()
        self.assertEqual(len(self.cinema.booking_manager.bookings), 1)

    @patch('cinema.ui.console_interface.ConsoleUI.input_ticket_count', return_value=None)
    def test_book_tickets_user_cancel(self, mock_ticket_input):
        self.cinema.book_tickets()
        self.assertEqual(len(self.cinema.booking_manager.bookings), 0)

    @patch('cinema.ui.console_interface.ConsoleUI.input_ticket_count', return_value=30)
    def test_book_tickets_not_enough_seats(self, mock_ticket_input):
        self.cinema.seat_map.reserve([(i,j) for i in range(1,6) for j in range(1,6)])  # reserve all
        self.cinema.book_tickets()
        self.assertEqual(len(self.cinema.booking_manager.bookings), 0)

    @patch('cinema.ui.console_interface.ConsoleUI.input_ticket_count', return_value=2)
    @patch('cinema.ui.console_interface.ConsoleUI.input_seat_position', return_value='Z99')
    def test_book_tickets_invalid_manual_position(self, mock_seat_input, mock_ticket_input):
        self.cinema.book_tickets()
        self.assertEqual(len(self.cinema.booking_manager.bookings), 1)

    @patch('cinema.ui.console_interface.ConsoleUI.input_booking_id', return_value='INVALID')
    def test_check_booking_invalid_id(self, mock_booking_id):
        self.cinema.check_booking()  # Should just print "Booking ID not found."

    @patch('cinema.ui.console_interface.ConsoleUI.input_booking_id', return_value='')
    def test_check_booking_blank_input(self, mock_booking_id):
        self.cinema.check_booking()  # Should simply return without error

    @patch('cinema.ui.console_interface.ConsoleUI.input_ticket_count')
    def test_booking_not_enough_contiguous(self, mock_ticket_count):
        self.cinema.seat_map.reserve([(1, i) for i in range(1, 6)])  # Row 1 full
        mock_ticket_count.return_value = 5
        with patch('builtins.print') as mocked_print:
            self.cinema.book_tickets()
            mocked_print.assert_any_call("Sorry, unable to find enough seats together.")


if __name__ == "__main__":
    unittest.main()