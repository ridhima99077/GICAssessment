from cinema.lib.cinema import Cinema

def main():
    print("Welcome to GIC Cinemas Setup")
    while True:
        try:
            entry = input("Enter movie title, number of rows and seats per row (e.g., Inception 8 10): ").strip()
            if not entry:
                continue
            parts = entry.split()
            if len(parts) < 3:
                print("Please enter valid input.")
                continue
            title = " ".join(parts[:-2])
            rows = int(parts[-2])
            seats = int(parts[-1])
            if 1 <= rows <= 26 and 1 <= seats <= 50:
                break
            else:
                print("Rows must be 1-26, seats per row must be 1-50.")
        except ValueError:
            print("Invalid input.")

    cinema = Cinema(title, rows, seats)

    while True:
        print(f"\nWelcome to GIC Cinemas")
        print(f"[1] Book tickets for {cinema.title} ({cinema.seat_map.available_count()} seats available)")
        print("[2] Check bookings")
        print("[3] Exit")
        choice = input("Please enter your selection: ").strip()

        if choice == '1':
            cinema.book_tickets()
        elif choice == '2':
            cinema.check_booking()
        elif choice == '3':
            print("Thank you for using GIC Cinemas system. Bye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()