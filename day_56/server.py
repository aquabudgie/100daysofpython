from flask import Flask, Response


app = Flask(__name__)

@app.route("/")
def greet():
    return "<h1>Hello World!</h1>" \
        f"<img src='https://i.giphy.com/l378khQxt68syiWJy.webp' width=300>"

@app.route("/health")
def get_health():
    """Simple health check endpoint"""
    return Response(status=200, mimetype="text/plain", response="OK")


if __name__ == "__main__":
    app.run(debug=True)
