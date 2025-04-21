from cinema.lib.seat_allocator import SeatMap
from cinema.lib.booking_manager import BookingManager
from cinema.ui.console_interface import ConsoleUI

class Cinema:
    def __init__(self, title, rows, seats_per_row):
        self.title = title
        self.seat_map = SeatMap(rows, seats_per_row)
        self.booking_manager = BookingManager()

    def book_tickets(self):
        num = ConsoleUI.input_ticket_count(self.seat_map.available_count())
        if num is None:
            return

        default_seats = self.seat_map.find_best_seats(num)
        if not default_seats or len(default_seats) < num:
            print("Not enough contiguous seats available.")
            return

        booking_id = self.booking_manager.generate_id()
        print(f"Successfully reserved {num} {self.title} tickets. Booking ID: {booking_id}")
        self.seat_map.display(highlight_seats=default_seats)

        choice = ConsoleUI.input_seat_position()
        if choice:
            if len(choice) >= 2 and choice[0].isalpha() and choice[1:].isdigit():
                row_letter = choice[0].upper()
                row = ord(row_letter) - 65 + 1
                col = int(choice[1:])
                if 1 <= row <= self.seat_map.rows and 1 <= col <= self.seat_map.seats_per_row:
                        if not self.seat_map.is_available(row, col):
                            print("Some of the selected seats are already booked. Showing current seat map:")
                            self.seat_map.display()
                            print("Please try booking again.")
                            return
                        seats_selected = self.seat_map.allocate_from(row, col, num)

                        if len(seats_selected) == num and all(
                                self.seat_map.is_available(r, c) for r, c in seats_selected):
                            default_seats = seats_selected
                        else:
                            print("Not enough seats available from that starting position. Showing current seat map:")
                            self.seat_map.display()
                            print("Please try booking again.")
                            return
                else:
                    print("Invalid seat position. Using default selection.")
            else:
                print("Invalid input format. Using default selection.")

        self.seat_map.reserve(default_seats)
        self.booking_manager.add_booking(booking_id, default_seats)
        print(f"Booking ID: {booking_id} confirmed.")

    def check_booking(self):
        try:
            booking_id = ConsoleUI.input_booking_id()
            if not booking_id:
                return
            seats = self.booking_manager.get_booking(booking_id)
            if seats:
                print(f"Booking ID: {booking_id} Selected seats:")
                self.seat_map.display(highlight_seats=seats)
            else:
                print("Booking ID not found.")
        except ValueError:
            print("Invalid input")