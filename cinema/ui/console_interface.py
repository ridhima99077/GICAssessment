class ConsoleUI:
    @staticmethod
    def input_ticket_count(max_seats):
        while True:
            try:
                num = input("Enter number of tickets to book, or blank to go back: ").strip()
                if not num:
                    return None
                num = int(num)
                if num <= 0:
                    print("Enter a positive number.")
                elif num > max_seats:
                    print(f"Sorry, only {max_seats} seats available.")
                else:
                    return num
            except ValueError:
                print("Invalid input.")

    @staticmethod
    def input_seat_position():
        choice = input("Enter blank to accept seat selection, or enter new starting seat (e.g., A05): ").strip()
        return choice

    @staticmethod
    def input_booking_id():
        return input("Enter booking ID, or blank to go back: ").strip()