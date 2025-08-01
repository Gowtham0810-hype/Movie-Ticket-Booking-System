# 🎬 Movie Ticket Booking System

A dynamic web-based application for booking movie tickets across multiple cities and theatres. Built using **Flask**, **MySQL**, and **HTML/CSS**, this system enables users to select movies, pick seats in real-time, confirm bookings with OTP-based email verification, and receive e-tickets via email.

---

## 🚀 Features

- ✅ User login and registration
- 🏙️ Multi-city and multi-theatre booking support
- 🕒 Multiple movie showtimes per theatre
- 💺 Real-time seat selection interface
  - 🟩 Green: Selected
  - 🟥 Red: Booked
  - ⬜ Grey: Available
- 💳 Payment form for completing the booking
- 🔐 OTP verification via email before finalizing the booking
- 📩 Email confirmation of tickets to the user

---

## 💻 Tech Stack

| Technology       | Purpose                         |
|------------------|----------------------------------|
| Flask            | Backend web framework           |
| MySQL            | Relational database             |
| Flask-Mail       | Sending OTP and ticket emails   |
| Flask-Admin      | Admin dashboard (optional)      |
| HTML/CSS         | Frontend UI                     |

---

## 🏗️ Project Structure
```bash
movie-booking-system/
├── app.py
├── static/
│   ├── styles.css
│   └── images/
├── templates/
│   ├── admin.html
│   ├── adminverification.html
│   ├── cancellation.html
│   ├── cancellationend.html
│   ├── cancellationlogin.html
│   ├── cities.html
│   ├── done.html
│   ├── home.html
│   ├── login.html
│   ├── movies.html
│   ├── otp.html
│   ├── payment.html
│   ├── seatavailability.html
│   ├── seats.html
│   ├── signup.html
│   ├── theatres.html
│   ├── timings.html
│   └── verification.html

```
## ⚙️ Setup Instructions

Follow these steps to set up and run the Movie Ticket Booking System locally:

### 1. 🔁 Clone the Repository

```bash
git clone https://github.com/yourusername/movie-booking-system.git
cd movie-booking-system
```
### 2.🐍 Create & Activate Virtual Environment (Recommended)
```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
### 3.📦 Install Dependencies
```bash
pip install Flask flask-mysqldb flask-mail flask-sqlalchemy flask-admin

```
### 4.🛢️ Set Up MySQL Database
- Install MySQL and create a database (e.g., moviebooking)
- Update the database credentials in app.py:
```bash
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'yourusername'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'moviebooking'

```
- Run the SQL schema you have (not provided here) to create necessary tables for users, bookings, etc.
### 5.📧 Configure Mail Settings for OTP
- Update the mail configuration in app.py with your email credentials:
```bash
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'youremail@gmail.com'
app.config['MAIL_PASSWORD'] = 'yourpassword'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

```
- Consider using environment variables or a .env file to avoid exposing credentials in code.
### 6.🚀 Run the Application
- Once everything is configured, run the app:
```bash
  python app.py

```
### 7. ✅ Access the App
- Visit http://127.0.0.1:5000

- Sign up or log in

- Select city, theatre, movie, and timing

- Book seats via an interactive UI

- Complete payment and OTP verification

- Receive booking confirmation via email
