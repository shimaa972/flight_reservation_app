import tkinter as tk
from tkinter import ttk
import database

def open_view_window(root):
    view_window = tk.Toplevel(root)
    view_window.title("View Reservations")
    view_window.geometry("600x400")

    tree = ttk.Treeview(view_window, columns=("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Flight", text="Flight")
    tree.heading("Departure", text="Departure")
    tree.heading("Destination", text="Destination")
    tree.heading("Date", text="Date")
    tree.heading("Seat", text="Seat")
    tree.pack(fill=tk.BOTH, expand=True)

    reservations = database.show_reservations()
    for res in reservations:
        tree.insert("", "end", values=res)
