This Python script manages a simple system for adding and displaying details of colleges, students, and teachers. It allows the creation of colleges, and the addition of students and teachers with OTP-based email verification. Each entity (college, student, teacher) is modeled using Python classes, with relationships established between them.

Key Features:

College Management: Create colleges with unique IDs.

Student & Teacher Management: Add students and teachers to specific colleges.

OTP Verification: An OTP is sent to the email address of students and teachers for authentication during the addition process.

Display Details: View details of all students and teachers in a college.

The code uses the smtplib library to send OTP emails via Gmail's SMTP server and random for OTP generation.

Key Technologies:
Python
SMTP (Email)
Object-Oriented Programming (OOP)
This script is intended for educational purposes to demonstrate basic college management system functionality with a simple command-line interface.
