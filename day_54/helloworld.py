from flask import Flask

app = Flask(__name__)

# print(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_italic(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route("/")
@make_bold
@make_italic
@make_underline
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello_user(name):
    return f"<h1 style='text-align: center'>Hello, {name + '12'}</h1>" \
        "<p>This is a paragraph.</p>" \
        "<img src='https://offroadium.com/wp-content/uploads/vehicles/subaru/forester/subaru-forester-2019-white-1.jpg' width=300>"


if __name__ == "__main__":
    app.run(debug=True)
