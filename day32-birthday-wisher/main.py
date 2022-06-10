import datetime as dt
import random
import smtplib

weekdays = [0, 1, 2, 3, 4, 5, 6]
now = dt.datetime.now()
day_of_week = now.weekday()


def random_quotes():
    with open("quotes.txt") as quotes:
        quote_list = quotes.readlines()
        random_quote = random.choice(quote_list)
        return random_quote


def send_email():
    my_email = "example@gmail.com"
    password = "piptsdsadukjhnaezi"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="example@hotmail.com",
                            msg=f"Subject:Quote of the day\n\n{random_quotes()}")


if day_of_week in weekdays:
    send_email()
