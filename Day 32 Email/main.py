# Sending an email using python
import datetime as dt
import random as r 
import smtplib
PASSWORD = 'derpdwarjxweyhcw'
EMAIL = "mypythontest27@gmail.com"
# with smtplib.SMTP('smtp.gmail.com', port = 587) as connection:

#     connection.starttls()
#     connection.login(user=EMAIL, password=PASSWORD)
#     connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg = "Subject:Testing Email w/ Python\n\nIt works!")

#----------------------------MOTIVATIONAL EMAIL------------------------------------#
# with open ('Intermediate/Day 32 Email/quotes.txt', 'r') as file:
#     quotes = file.readlines()
#     line = r.choice(quotes)

# with smtplib.SMTP('smtp.gmail.com', port = 587) as connection:

#     connection.starttls()
#     connection.login(user=EMAIL, password=PASSWORD)
#     connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg =f"Subject:Motivational Email\n\n{line}")
                        


