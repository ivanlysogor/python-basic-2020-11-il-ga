from flask import Flask, request, render_template

from views.flats import flat_app


app = Flask(__name__)

app.register_blueprint(flat_app, url_prefix="/flats")


@app.route("/")
def hello_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
