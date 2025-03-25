import tkinter as tk
from tkinter import messagebox
import booking
import reservations
import edit_reservation

def main_window():
    root = tk.Tk()
    root.title("Flight Reservation System")
    root.geometry("600x400")

    # زر إضافة حجز
    def open_book_window():
        booking.open_book_window(root)

    # زر عرض الحجوزات
    def open_view_window():
        reservations.open_view_window(root)

    # زر تحديث الحجز
    def open_update_window():
        edit_reservation.open_update_window(root)

    # زر حذف الحجز
    def open_delete_window():
        edit_reservation.open_delete_window(root)

    # أزرار التنقل في الصفحة الرئيسية
    tk.Button(root, text="Book a Flight", command=open_book_window).pack(pady=10)
    tk.Button(root, text="View Reservations", command=open_view_window).pack(pady=10)
    tk.Button(root, text="Update Reservation", command=open_update_window).pack(pady=10)
    tk.Button(root, text="Delete Reservation", command=open_delete_window).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_window()
