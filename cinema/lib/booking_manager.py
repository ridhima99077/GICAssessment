class BookingManager:
    def __init__(self):
        self.bookings = {}
        self.counter = 1

    def generate_id(self):
        bid = f"GIC{self.counter:04d}"
        self.counter += 1
        return bid

    def add_booking(self, booking_id, seats):
        self.bookings[booking_id] = seats

    def get_booking(self, booking_id):
        return self.bookings.get(booking_id)