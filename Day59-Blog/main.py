from flask import Flask, render_template, request
import requests
import smtplib

my_email = "example@gmail.com"
password = "pw"
to_email = "example@hotmail.com"

app = Flask(__name__)

posts = requests.get(
    "https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw"
    "/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json").json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        phone = data["phone"]
        email = data["email"]
        message = data["message"]
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:Hello\n\nName: {name}\nEmail: {email}\nPhone: {phone}\n Message: {message}")
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html")


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
