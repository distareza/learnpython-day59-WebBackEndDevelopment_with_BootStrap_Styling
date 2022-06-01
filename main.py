from flask import Flask, render_template
from datetime import date
app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route("/<string:page>")
def page(page: str):
    year = str(date.today().year)
    return render_template(page, year=year)

if __name__ == "__main__":
    app.run(debug=True)