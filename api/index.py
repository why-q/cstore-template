from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route("/")
def home():
    subfolders = [f.name for f in os.scandir("public") if f.is_dir()]
    return render_template("home.html", folders=subfolders)


@app.route("/<path:subpath>")
def serve_res(subpath):
    return send_from_directory("res", subpath)


if __name__ == "__main__":
    app.run()
