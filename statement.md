 Flight Booking System

1. Problem Statement
Many entry-level programming courses require students to demonstrate basic proficiency in data structure manipulation, function definition, and control flow in a practical, yet simple, application. The challenge is to implement a functional text-based booking system that can manage predefined flight data and dynamically track bookings and remaining seat inventory without relying on complex external databases or file systems. This project serves as a foundational exercise to consolidate core programming concepts.

2. Scope of the Project
The scope of this project is strictly limited to a console-based simulation.
Inclusions:
Management of static flight data (Flight ID, route, capacity).
Functions for viewing available flights.
Logic for booking one-way and round-trip journeys.
Real-time decrementing of available seats upon booking.
Listing of all current bookings.
Exclusions (Out of Scope):
Data persistence (data is lost upon program exit).
User authentication or different user roles (e.g., admin, passenger).
Advanced features like flight search by city, booking cancellation, or modification.
Graphical User Interface (GUI) or web integration.
Error handling for non-numeric input for menu choices.

4. Target Users

The primary target users for this simple application are:
Programming Students: Individuals learning fundamental concepts of Python (lists, functions, loops, conditional logic).
Instructors/Tutors: Used as a straightforward, runnable example or a quick assignment solution review.
Beginners: Anyone needing a minimal working example of a data management application built solely with core Python structures.

4. High-Level Features
   
Data Viewing
Users can easily view all currently defined flights, their routes, and the exact number of seats available.
Booking & Inventory
Allows sequential booking of both outbound and optional return flights. Automatically updates the seat count, ensuring no overbooking occurs when seats reach zero.
Booking Confirmation
Prints a confirmation ticket summarizing the booking details (Passenger Name, Flight ID, Route) immediately after a successful reservation.
Record Keeping
A dedicated feature to list all historical bookings made during the current session, showing which passenger is on which flight.

