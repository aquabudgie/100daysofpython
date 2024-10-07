from flask import Flask, Response, render_template


app = Flask(__name__)

@app.route("/")
def greet():
    return render_template("index.html")

@app.route("/health")
def get_health():
    """Simple health check endpoint"""
    return Response(status=200, mimetype="text/plain", response="OK")


if __name__ == "__main__":
    app.run(debug=True)
