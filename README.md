This code implements a Cinema Booking System where:

A Seat Map of the cinema is created.

Users can:

* Book seats automatically (best seats picked).
* Try manual seat selection.
* Get a Booking ID.
* Check booking details later using their Booking ID.

It runs in the console/terminal with user inputs.

## **Module Breakdown:**

### 1. SeatMap (Manages seating layout)

Creates a grid: Rows × Seats per row.

   . means seat is available.
   '#' means seat is booked.

**Important Methods:**

**Method	Purpose**

* **display(highlight_seats):** Shows current seat layout nicely with optional highlights (for showing selection).
* **available_count():** Counts how many seats are still available.
* **reserve(seats):** Marks the given seats as booked (#).
* **is_available(row, col):** Checks if a specific seat is free.
* **find_best_seats(num_tickets):** Automatically finds the "best" seats (centered) for given number.
* **allocate_from(start_row, start_col, num_tickets):** Tries to book seats starting from a particular seat onward.


### 2. BookingManager (Manages bookings)

Handles booking IDs like GIC0001.
Stores which seats are booked under each booking ID.

**Important Methods:**

**Method	Purpose**

**generate_id():**	Makes a new booking ID (GIC0001, GIC0002, etc.).
**add_booking(booking_id, seats):**	Saves a booking with seats.
**get_booking(booking_id):** Retrieves seat details for a given booking ID.


### 3.ConsoleUI (Handles all input/output)

Input handlers with validation and error checks.
Static methods (no need to create an object).

**Method	Purpose**

**input_ticket_count(max_seats):**	Safely asks user for how many tickets they want. Handles blank input, negatives, non-numbers.
**input_seat_position():**	Asks user if they want a custom starting seat.
**input_booking_id():**	Asks user for their booking ID.

### 4. Cinema (Main "controller" of the system)

Combines SeatMap + BookingManager to offer booking and lookup features.
Every movie has its own Cinema instance.

**Important Methods:**

**Method	Purpose**

**book_tickets():**	Full process to book tickets: ask for number, auto-suggest, allow manual start seat override.
**check_booking():** Allows users to lookup their booking using their Booking ID.


### 5. **main() (Entry point)**

Welcomes user to setup:
 Enter Movie Title.
 Rows and Seats per row.
 
Starts main menu loop:
* Book tickets
* Check bookings
* Exit

**Flowchart of Booking**

User runs program

          ↓
 
 Setup Movie Title + Seat Layout
    
           ↓
 
         Menu:
  
           [1] Book tickets → Book → Get Booking ID
           
           [2] Check booking → See seat positions
          
           [3] Exit


### Validations Handled

* Number of tickets must be positive and ≤ available seats.
* Rows must be between 1 and 26.
* Seats per row must be between 1 and 50.
* Manual seat input (like A05) must be correctly formatted.
* Booking ID must exist to view booking.
* If user cancels (blank input), it’s safely handled.

**Few Important Details**

Rows are labeled A-Z.
Bookings try to find seats close to the center.
Users can override the auto-suggested seats by entering a specific starting seat.
Bookings get unique IDs (GICxxxx).
If wrong inputs are given, error messages are displayed, and the system doesn't crash.

Example Output

Welcome to GIC Cinemas Setup
Enter movie title, number of rows and seats per row (e.g., Inception 8 10): Avengers 5 5

Welcome to GIC Cinemas
[1] Book tickets for Avengers (25 seats available)
[2] Check bookings
[3] Exit

Please enter your selection: 1
Enter number of tickets to book, or blank to go back: 3
Successfully reserved 3 Avengers tickets. Booking ID: GIC0001

   SCREEN
   
  1  2  3  4  5

E | .  .  o  o  o

D | .  .  .  .  .

C | .  .  .  .  .

B |                                                                                                                                                                                                                         .  .  .  .  .

A | .  .  .  .  .

    1  2  3  4  5

Enter blank to accept seat selection, or enter new starting seat (e.g., A05): 
Booking ID: GIC0001 confirmed.
