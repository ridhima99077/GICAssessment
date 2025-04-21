import unittest
from unittest.mock import patch
from cinema.ui.console_interface import ConsoleUI

class TestConsoleUI(unittest.TestCase):

    @patch('builtins.input', side_effect=['', '3'])
    def test_input_ticket_count_blank_first_then_valid(self, mock_input):
        result = ConsoleUI.input_ticket_count(5)
        self.assertIsNone(result)  # first blank input should return None

    @patch('builtins.input', side_effect=['abc', '-1', '100', '2'])
    def test_input_ticket_count_invalid_inputs(self, mock_input):
        result = ConsoleUI.input_ticket_count(5)
        self.assertEqual(result, 2)

    @patch('builtins.input', return_value='A05')
    def test_input_seat_position_valid(self, mock_input):
        self.assertEqual(ConsoleUI.input_seat_position(), 'A05')

    @patch('builtins.input', return_value='')
    def test_input_seat_position_blank(self, mock_input):
        self.assertEqual(ConsoleUI.input_seat_position(), '')

    @patch('builtins.input', return_value='GIC0001')
    def test_input_booking_id_valid(self, mock_input):
        self.assertEqual(ConsoleUI.input_booking_id(), 'GIC0001')

if __name__ == "__main__":
    unittest.main()