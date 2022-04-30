#send Email Using Python

import os
import random
import smtplib


def automatic_email():
    user = input("Enter Your Name >>: ")
    email = input("Enter Your Email >>: ")
    message = (f"Dear {user}, Welcome to the Email...This email is sent by the chetan... ")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("chetanppatil998@gmail.com", "gjzhfathddconots")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent!") 
    
automatic_email()
