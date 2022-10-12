from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


agify_api = "https://api.agify.io?name="
genderize_api = "https://api.genderize.io?name="


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, CURRENT_YEAR=current_year)


@app.route('/guess/<name>')
def guess_age_gender(name):
    agify_response = requests.get(url=agify_api + name)
    agify_data = agify_response.json()

    genderize_response = requests.get(url=genderize_api + name)
    genderize_data = genderize_response.json()
    age = agify_data["age"]
    gender = genderize_data["gender"]

    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(url=blog_url)
    blog_data = blog_response.json()
    return render_template("blog.html", posts=blog_data)

if __name__ == "__main__":
    app.run(debug=True)


