# Flight Booking System

## Project Title

Flight Booking System


##  Overview of the Project

This project is a basic command-line interface (CLI) application that simulates a flight booking system. It allows a user to interact with a predefined list of flights, check seat availability, book one-way or round-trip tickets, and view a list of all current bookings. All data (flights and bookings) are stored in simple Python lists and are **not persistent**; the data resets every time the program is closed and restarted.


##  Features

The system provides the following functionalities through its main menu:

* **View Flights (Option 1):** Displays a list of all available flights, including the Flight ID, departure city, destination city, and the current number of available seats.
* **Book a Flight (Option 2):**
    * Allows booking of an **outbound** journey.
    * Checks for flight existence and seat availability.
    * Prompts the user to book an optional **return** journey immediately after the outbound booking.
    * Automatically decrements the available seat count upon successful booking.
    * Prints a formatted ticket confirmation.
* **View All Bookings (Option 3):** Displays a simple list of all passenger names and the Flight ID associated with their booking(s).
* **Exit (Option 4):** Closes the application.



##  Technologies/Tools Used

* **Language:** Python 3
* **Tools:** Standard Python interpreter (No external libraries required)



## Steps to Install & Run the Project

### Prerequisites

You must have **Python 3** installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation and Execution

1.  **Save the Code:** Copy the entire Python script (including the `flights` list, `bookings` list, and all defined functions) and save it to a file named `flight_booking.py` (or any `.py` extension).
2.  **Open Terminal:** Navigate to the directory where you saved the file using your command line or terminal.
3.  **Run the Application:** Execute the script using the Python interpreter:

    ```bash
    python flight_booking.py
    ```

4.  **Interaction:** The system's main menu will be displayed. Enter the number corresponding to the action you wish to perform (1, 2, 3, or 4).



##  Instructions for Testing

Follow these steps to test the core functionalities of the system:

### 1. Test Viewing Flights

1.  Start the application.
2.  Choose option **1** (**View Flights**).
3.  **Expected Outcome:** A list of all six initial flights should be displayed, and all should show their full initial capacity (e.g., F501 with 40 seats).

### 2. Test Booking a One-Way Flight

1.  Choose option **2** (**Book a Flight**).
2.  Enter a valid Flight ID (e.g., `F501`).
3.  Enter your name (e.g., `Alice`).
4.  Choose option **2** for the return ticket (**No**).
5.  Choose option **1** (**View Flights**) again.
6.  **Expected Outcome:**
    * A ticket for Alice on F501 should be printed.
    * When viewing flights, F501 should now show **39** seats left.

### 3. Test Booking a Round-Trip Flight

1.  Choose option **2** (**Book a Flight**).
2.  Enter a valid outbound Flight ID (e.g., `F235`).
3.  Enter your name (e.g., `Bob`).
4.  Choose option **1** for the return ticket (**Yes**).
5.  Enter a valid return Flight ID (e.g., `F501`).
6.  Choose option **3** (**View All Bookings**).
7.  **Expected Outcome:**
    * Tickets for Bob on F235 and F501 should be printed.
    * In the View All Bookings list, there should be two entries for Bob: one for `F235` and one for `F501`.

### 4. Test Booking on a Full Flight

1.  **To set up the test:** Keep booking seats on a single flight (e.g., F897 which has 15 seats) until its seat count is **0**.
2.  Attempt to book another seat on that now-full flight (e.g., `F897`).
3.  **Expected Outcome:** The system should print the message **"No seats left on this flight"** and block the booking.
