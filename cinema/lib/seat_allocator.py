class SeatMap:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = [['.' for _ in range(seats_per_row)] for _ in range(rows)]

    def display(self, highlight_seats=None):
        print("\n   SCREEN")
        header = "    " + " ".join(str(i+1).rjust(2) for i in range(self.seats_per_row))
        print(header)
        for idx, row in enumerate(reversed(self.seats)):
            row_label = chr(65 + (self.rows - idx - 1))
            row_display = []
            for seat_idx, seat in enumerate(row):
                pos = (self.rows - idx, seat_idx + 1)
                if highlight_seats and pos in highlight_seats:
                    row_display.append('o')
                else:
                    row_display.append(seat)
            print(f"{row_label} | " + "  ".join(row_display))
        print(header)

    def available_count(self):
        return sum(row.count('.') for row in self.seats)

    def reserve(self, seats):
        for row, col in seats:
            self.seats[row-1][col-1] = '#'

    def is_available(self, row, col):
        return self.seats[row-1][col-1] == '.'

    def find_best_seats(self, num_tickets):
        seats_selected = []
        mid = (self.seats_per_row + 1) / 2
        rows_order = list(range(1, self.rows + 1))
        for r in rows_order:
            available = [(r, c+1) for c in range(self.seats_per_row) if self.is_available(r, c+1)]
            available.sort(key=lambda x: abs(x[1]-mid))
            for seat in available:
                if len(seats_selected) < num_tickets:
                    seats_selected.append(seat)
                else:
                    return seats_selected
        return seats_selected

    def allocate_from(self, start_row, start_col, num_tickets):
        seats_selected = []
        rows_order = list(range(start_row, self.rows + 1))
        start_found = False
        for r in rows_order:
            c_start = start_col if not start_found else 1
            for c in range(c_start, self.seats_per_row+1):
                if self.is_available(r, c):
                    seats_selected.append((r, c))
                    if len(seats_selected) == num_tickets:
                        return seats_selected
            start_found = True
        return seats_selected