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

# عرض الحجوزات
def show_reservations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()
    return rows

# تحديث الحجز
def update_reservation(id, name, flight_number, departure, destination, date, seat_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''UPDATE reservations
                      SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
                      WHERE id = ?''', (name, flight_number, departure, destination, date, seat_number, id))
    conn.commit()
    conn.close()

# حذف الحجز
def delete_reservation(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id = ?", (id,))
    conn.commit()
    conn.close()
