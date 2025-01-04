import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send OTP
def send_otp(name, email):
    otp = random.randint(1111, 9999)
    subject = "OTP For Verification"
    body = f"Hello {name},\nYour OTP for verification is: {otp}"

    msg = MIMEMultipart()
    msg['From'] = "kalyan123sai@gmail.com"
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Configure the email server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("kalyan123sai@gmail.com", "ytve bicj lpfw rjcr")
    server.send_message(msg)
    server.quit()

    return otp

class person:
    def __init__(self, rollno, name, email):
        self.name = name
        self.rollno = rollno
        self.email = email

class student(person):
    def __init__(self, srollno, sname, semail, branch):
        super().__init__(srollno, sname, semail)
        self.branch = branch

class teacher(person):
    def __init__(self, trollno, tname, temail, subject):
        super().__init__(trollno, tname, temail)
        self.subject = subject

class college:
    def __init__(self, cid, cname):
        self.cid = cid
        self.cname = cname
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

colleges = []
while True:
    print("Choose your Option")
    print("1. Add College ")
    print("2. Add Student ")
    print("3. Add Teacher ")
    print("4. Display Student Details ")
    print("5. Display Teacher Details ")
    print("6. Exit ")
    ip = int(input("Enter Your Option: "))
    
    if ip == 1:
        cname = input("Enter college Name: ")
        cid = input("Enter College Id: ")
        if any(clg.cid == cid for clg in colleges):
            print("College Already Exists!")
        else:
            colleges.append(college(cid, cname))
            print("College Created Successfully!")

    elif ip == 2:
        cid = input("Enter College id: ")
        clg = next((c for c in colleges if c.cid == cid), None)
        if clg:
            name = input("Enter Student Name: ")
            roll = input("Enter Student Roll number: ")
            email = input("Enter Student Email: ")
            branch = input("Enter Student Branch: ")
            
            otp = send_otp(name, email)
            user_input = input("Enter the OTP sent to your email: ")
            if user_input == str(otp):
                clg.add_student(student(roll, name, email, branch))
                print("Student added successfully!")
            else:
                print("OTP Verification Failed!")
        else:
            print("College Does Not Exist!")

    elif ip == 3:
        cid = input("Enter College id: ")
        clg = next((c for c in colleges if c.cid == cid), None)
        if clg:
            name = input("Enter Teacher Name: ")
            roll = input("Enter Teacher Roll number: ")
            email = input("Enter Teacher Email: ")
            subject = input("Enter Teacher Subject: ")
            
            otp = send_otp(name, email)
            user_input = input("Enter the OTP sent to your email: ")
            if user_input == str(otp):
                clg.add_teacher(teacher(roll, name, email, subject))
                print("Teacher added successfully!")
            else:
                print("OTP Verification Failed!")
        else:
            print("College Does Not Exist!")

    elif ip == 4:
        cid = input("Enter College id: ")
        clg = next((c for c in colleges if c.cid == cid), None)
        if clg:
            print(f"Student Details of {clg.cname}:")
            for student in clg.students:
                print(f"Roll No: {student.rollno}, Name: {student.name}, Email: {student.email}, Branch: {student.branch}")
        else:
            print("College Does Not Exist!")

    elif ip == 5:
        cid = input("Enter College id: ")
        clg = next((c for c in colleges if c.cid == cid), None)
        if clg:
            print(f"Teacher Details of {clg.cname}:")
            for teacher in clg.teachers:
                print(f"Roll No: {teacher.rollno}, Name: {teacher.name}, Email: {teacher.email}, Subject: {teacher.subject}")
        else:
            print("College Does Not Exist!")

    else:
        print("Thanks! Visit Again")
        break
