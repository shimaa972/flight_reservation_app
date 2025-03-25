# Flight Reservation System

A simple flight reservation system built with Python using `tkinter` for the user interface and `SQLite` for storing reservation data. The system allows users to book flights, view existing reservations, update their details, and delete reservations.

## Features

- **Book a Flight**: Allows users to book a new flight with details like passenger name, flight number, departure, destination, date, and seat number.
- **View Reservations**: Displays a list of all reservations in a simple interface.
- **Update Reservation**: Allows users to update the details of an existing reservation.
- **Delete Reservation**: Lets users delete a reservation from the system.

## Installation

### Prerequisites

Ensure you have the following installed:

- **Python 3.x**: Download from [python.org](https://www.python.org/)
- **SQLite3**: Comes pre-installed with Python, so no separate installation is required.

### Steps to run the project

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/shimaa972/flight_reservation_app.git
    ```

2. Navigate into the project directory:

    ```bash
    cd flight_reservation_app
    ```

3. Install the required dependencies:

    Create a virtual environment (optional but recommended):

    ```bash
    python -m venv .venv
    ```

    ثم تفعيل البيئة الافتراضية:

    - على Windows:
      ```bash
      .\.venv\Scripts\activate
      ```

    - على macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```

    ثم تثبيت المكتبات المطلوبة (في حال كانت موجودة في ملف `requirements.txt`):

    ```bash
    pip install -r requirements.txt
    ```

4. لتشغيل التطبيق، استخدم الأمر التالي:

    ```bash
    python main.py
    ```

## How to Use

1. After starting the application, the main window will appear with options:
   - **Book a Flight**: Opens the booking form to enter flight details.
   - **View Reservations**: Displays a list of all current reservations.
   - **Update Reservation**: Allows you to update an existing reservation.
   - **Delete Reservation**: Lets you delete a reservation by its ID.

2. Follow the on-screen instructions to interact with the system.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, feel free to reach out:

- **Email**: shimaaaa972@gmail.com
