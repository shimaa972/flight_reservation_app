import tkinter as tk
from tkinter import messagebox
import database

def open_update_window(root):
    update_window = tk.Toplevel(root)
    update_window.title("Update Reservation")
    update_window.geometry("400x300")

    tk.Label(update_window, text="Reservation ID:").pack()
    entry_id = tk.Entry(update_window)
    entry_id.pack()

    tk.Label(update_window, text="New Name:").pack()
    entry_name = tk.Entry(update_window)
    entry_name.pack()

    tk.Label(update_window, text="New Flight Number:").pack()
    entry_flight_number = tk.Entry(update_window)
    entry_flight_number.pack()

    tk.Label(update_window, text="New Departure:").pack()
    entry_departure = tk.Entry(update_window)
    entry_departure.pack()

    tk.Label(update_window, text="New Destination:").pack()
    entry_destination = tk.Entry(update_window)
    entry_destination.pack()

    tk.Label(update_window, text="New Date:").pack()
    entry_date = tk.Entry(update_window)
    entry_date.pack()

    tk.Label(update_window, text="New Seat Number:").pack()
    entry_seat_number = tk.Entry(update_window)
    entry_seat_number.pack()

    def update_flight():
        id = entry_id.get()
        name = entry_name.get()
        flight_number = entry_flight_number.get()
        departure = entry_departure.get()
        destination = entry_destination.get()
        date = entry_date.get()
        seat_number = entry_seat_number.get()
        database.update_reservation(id, name, flight_number, departure, destination, date, seat_number)
        messagebox.showinfo("Success", "Reservation Updated Successfully")
        update_window.destroy()

    tk.Button(update_window, text="Update Reservation", command=update_flight).pack()

def open_delete_window(root):
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Reservation")
    delete_window.geometry("300x200")

    tk.Label(delete_window, text="Reservation ID:").pack()
    entry_id = tk.Entry(delete_window)
    entry_id.pack()

    def delete_flight():
        id = entry_id.get()
        database.delete_reservation(id)
        messagebox.showinfo("Success", "Reservation Deleted Successfully")
        delete_window.destroy()

    tk.Button(delete_window, text="Delete Reservation", command=delete_flight).pack()
