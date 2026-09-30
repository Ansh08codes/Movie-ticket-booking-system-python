# Project Statement

## Project Title

Movie Ticket Booking System

## 1. Problem Statement

Booking movie tickets manually can be inconvenient because users need to know which movies are available, which seats are already booked, and how much a ticket costs. A simple command-line system can organize these basic booking activities in one place.

The Movie Ticket Booking System provides a small Python-based solution where a user can view available movies, check seats, book a seat, cancel a booking, and see the ticket amount.

## 2. Scope of the Project

The project focuses on the basic operations of a movie ticket booking system through a command-line interface.

The current scope includes:

- Displaying the available movies
- Showing movie genre, rating, and ticket price
- Displaying the seat layout for a selected movie
- Booking an available seat
- Preventing an already booked seat from being booked again
- Cancelling a booking
- Displaying the ticket amount
- Handling invalid user input

The project is intended as a small academic Python application. Bookings are maintained while the program is running and are reset when the program is closed. Database storage, online payment, user accounts, and real-time booking are outside the current scope.

## 3. Target Users

The intended users are:

- Students learning or demonstrating basic Python programming concepts
- Users who want to perform simple movie ticket booking operations through a terminal
- Academic evaluators who need to test the project from the command line

## 4. High-Level Features

### 1. Movie Display

The system displays the available movies along with their genre, rating, and ticket price.

### 2. Seat Display

The system displays the seats for the selected movie and shows which seats are available or already booked.

### 3. Ticket Booking

The user can select a movie and an available seat. The system confirms the booking and displays the ticket amount.

### 4. Booking Cancellation

The user can select a movie and cancel a previously booked seat.

### 5. Input Validation

The system checks invalid movie numbers, invalid seat numbers, already booked seats, and invalid numeric input.

## 5. Technology Used

- Python 3
- Command Line Interface
- GitHub for version control and project submission