import smtplib

my_email = "example@gmail.com"
password = "piptdfasfjklanaezi"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="example@hotmail.com",
                        msg="Subject:Hello\n\nthis is the body of my email.")




