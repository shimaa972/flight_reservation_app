import tkinter as tk
from tkinter import messagebox
import booking  # استيراد ملف الحجز
import reservations  # استيراد ملف عرض الحجوزات
import edit_reservation  # استيراد ملف تعديل الحجز

# واجهة المستخدم الرئيسية
def main_window():
    root = tk.Tk()
    root.title("Flight Reservation System")
    root.geometry("600x400")

    # زر إضافة حجز
    def open_book_window():
        booking.open_book_window(root)  # استدعاء دالة فتح نافذة الحجز من ملف booking.py

    # زر عرض الحجوزات
    def open_view_window():
        reservations.open_view_window(root)  # استدعاء دالة عرض الحجوزات من ملف reservations.py

    # زر تحديث الحجز
    def open_update_window():
        edit_reservation.open_update_window(root)  # استدعاء دالة تحديث الحجز من ملف edit_reservation.py

    # زر حذف الحجز
    def open_delete_window():
        edit_reservation.open_delete_window(root)  # استدعاء دالة حذف الحجز من ملف edit_reservation.py

    # أزرار التنقل في الصفحة الرئيسية
    tk.Button(root, text="Book a Flight", command=open_book_window).pack(pady=10)
    tk.Button(root, text="View Reservations", command=open_view_window).pack(pady=10)
    tk.Button(root, text="Update Reservation", command=open_update_window).pack(pady=10)
    tk.Button(root, text="Delete Reservation", command=open_delete_window).pack(pady=10)

    root.mainloop()

# تشغيل التطبيق
if __name__ == "__main__":
    main_window()  # استدعاء دالة main_window لتشغيل الواجهة
