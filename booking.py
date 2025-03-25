import tkinter as tk
from tkinter import messagebox
import database

def open_book_window(root):
    book_window = tk.Toplevel(root)
    book_window.title("Book a Flight")
    book_window.geometry("400x300")

    # حقول الإدخال
    tk.Label(book_window, text="Passenger Name:").pack()
    entry_name = tk.Entry(book_window)
    entry_name.pack()

    tk.Label(book_window, text="Flight Number:").pack()
    entry_flight_number = tk.Entry(book_window)
    entry_flight_number.pack()

    tk.Label(book_window, text="Departure:").pack()
    entry_departure = tk.Entry(book_window)
    entry_departure.pack()

    tk.Label(book_window, text="Destination:").pack()
    entry_destination = tk.Entry(book_window)
    entry_destination.pack()

    tk.Label(book_window, text="Date:").pack()
    entry_date = tk.Entry(book_window)
    entry_date.pack()

    tk.Label(book_window, text="Seat Number:").pack()
    entry_seat_number = tk.Entry(book_window)
    entry_seat_number.pack()

    # زر لحجز الرحلة
    def book_flight():
        name = entry_name.get()
        flight_number = entry_flight_number.get()
        departure = entry_departure.get()
        destination = entry_destination.get()
        date = entry_date.get()
        seat_number = entry_seat_number.get()
        if name and flight_number and departure and destination and date and seat_number:
            database.add_reservation(name, flight_number, departure, destination, date, seat_number)
            messagebox.showinfo("Success", "Reservation Added Successfully")
            book_window.destroy()
        else:
            messagebox.showerror("Error", "All fields must be filled!")

    tk.Button(book_window, text="Book Flight", command=book_flight).pack()
