from flask import Flask
from random import randint

app = Flask(__name__)


def random_number():
    return randint(0, 9)


def check_correct():
    pass


def too_low():
    return (
        "<h1 style='color:red'>Too Low!</h1>"
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=300>"
    )


def too_high():
    return (
        "<h1 style='color:purple'>Too High!</h1>"
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=300>"
    )


def correct():
    return (
        "<h1 style='color:green'>That's Correct!</h1>"
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=300>"
    )


@app.route("/")
def index():
    print(random_number())
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://i.giphy.com/l378khQxt68syiWJy.webp' width=300>"
    )


@app.route("/<number>")
def check_number(number):
    number = int(number)
    if number < secret_number:
        return too_low()
    elif number > secret_number:
        return too_high()
    else:
        return correct()


if __name__ == "__main__":
    secret_number = random_number()
    print(secret_number)
    app.run(debug=True)
