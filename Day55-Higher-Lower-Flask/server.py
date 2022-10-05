from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src =" https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

computer_number = random.randint(0, 9)
print(computer_number)

@app.route('/<int:random_number>')
def guess_number(random_number):
    if random_number < computer_number:
        return "<h1>Too low. Guess again.</h1><img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif random_number > computer_number:
        return "<h1>Too high. Guess again</h1><imr src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return f"<h1>You're right! {random_number} is the number</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)