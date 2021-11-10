from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>陳韋辰Python測試網頁</h1>"
    homepage += "<a href=/aboutme>MIS工作</a><br>"
    return homepage

@app.route("/aboutme")
def mis2b():
    return render_template("aboutme.html")

if __name__ == "__main__":
    app.run()
    