import tkinter as tk
from tkinter import messagebox
import sqlite3

# الاتصال بقاعدة البيانات SQLite
def connect_db():
    conn = sqlite3.connect('flights.db')
    return conn

# إنشاء الجدول إذا لم يكن موجودًا
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reservations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        flight_number TEXT,
                        departure TEXT,
                        destination TEXT,
                        date TEXT,
                        seat_number TEXT)''')
    conn.commit()
    conn.close()

# إضافة حجز جديد
def add_reservation(name, flight_number, departure, destination, date, seat_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Reservation Added Successfully")

# عرض الحجوزات
def show_reservations():
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()
    return rows

# تحديث الحجز
def update_reservation(id, name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE reservations
                      SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
                      WHERE id = ?''', (name, flight_number, departure, destination, date, seat_number, id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Reservation Updated Successfully")

# حذف الحجز
def delete_reservation(id):
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Reservation Deleted Successfully")

# واجهة المستخدم الرئيسية
def main_window():
    root = tk.Tk()
    root.title("Flight Reservation System")
    root.geometry("600x400")

    # زر إضافة حجز
    def open_book_window():
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
            add_reservation(name, flight_number, departure, destination, date, seat_number)
            book_window.destroy()

        tk.Button(book_window, text="Book Flight", command=book_flight).pack()

    # زر عرض الحجوزات
    def open_view_window():
        view_window = tk.Toplevel(root)
        view_window.title("View Reservations")
        view_window.geometry("600x400")

        reservations = show_reservations()
        for res in reservations:
            tk.Label(view_window, text=f"ID: {res[0]}, Name: {res[1]}, Flight: {res[2]}, Departure: {res[3]}, Destination: {res[4]}, Date: {res[5]}, Seat: {res[6]}").pack()

    # زر تحديث الحجز
    def open_update_window():
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

        # زر لتحديث الحجز
        def update_flight():
            id = entry_id.get()
            name = entry_name.get()
            flight_number = entry_flight_number.get()
            departure = entry_departure.get()
            destination = entry_destination.get()
            date = entry_date.get()
            seat_number = entry_seat_number.get()
            update_reservation(id, name, flight_number, departure, destination, date, seat_number)
            update_window.destroy()

        tk.Button(update_window, text="Update Reservation", command=update_flight).pack()

    # زر حذف الحجز
    def open_delete_window():
        delete_window = tk.Toplevel(root)
        delete_window.title("Delete Reservation")
        delete_window.geometry("300x200")

        tk.Label(delete_window, text="Reservation ID:").pack()
        entry_id = tk.Entry(delete_window)
        entry_id.pack()

        # زر لحذف الحجز
        def delete_flight():
            id = entry_id.get()
            delete_reservation(id)
            delete_window.destroy()

        tk.Button(delete_window, text="Delete Reservation", command=delete_flight).pack()

    # أزرار التنقل في الصفحة الرئيسية
    tk.Button(root, text="Book a Flight", command=open_book_window).pack(pady=10)
    tk.Button(root, text="View Reservations", command=open_view_window).pack(pady=10)
    tk.Button(root, text="Update Reservation", command=open_update_window).pack(pady=10)
    tk.Button(root, text="Delete Reservation", command=open_delete_window).pack(pady=10)

    create_table()  # إنشاء الجدول عند بدء التطبيق
    root.mainloop()

# تشغيل التطبيق
if __name__ == "__main__":
    main_window()
