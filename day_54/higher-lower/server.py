from flask import Flask
from random import randint

app = Flask(__name__)
secret_number = randint(0, 9)
links = (
    "<br><br><br>"
    '<a href="/0">0</a><br>'
    '<a href="/1">1</a><br>'
    '<a href="/2">2</a><br>'
    '<a href="/3">3</a><br>'
    '<a href="/4">4</a><br>'
    '<a href="/5">5</a><br>'
    '<a href="/6">6</a><br>'
    '<a href="/7">7</a><br>'
    '<a href="/8">8</a><br>'
    '<a href="/9">9</a><br>'
)


def check_correct():
    pass


def too_low():
    return "<h1 style='color:red'>Too Low!</h1>" \
        f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=300>+{links}"


def too_high():
    return "<h1 style='color:purple'>Too High!</h1>" \
        f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=300>+{links}"


def correct():
    return "<h1 style='color:green'>That's Correct!</h1>" \
        f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=300>+{links}"


@app.route("/")
def greet():
    return "<h1>Guess a number between 0 and 9</h1>" \
        f"<img src='https://i.giphy.com/l378khQxt68syiWJy.webp' width=300> + {links}"


@app.route("/<int:number>")
def check_number(number):
    number = int(number)
    if number < secret_number:
        return too_low()
    elif number > secret_number:
        return too_high()
    else:
        return correct()


if __name__ == "__main__":
    app.run(debug=True)
