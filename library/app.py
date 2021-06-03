from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.form:
        print(request.form)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

