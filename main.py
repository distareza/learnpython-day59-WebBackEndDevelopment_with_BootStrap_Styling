from flask import Flask, render_template
from datetime import date
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

year = str(date.today().year)

def get_blog_content():
    #return requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    return requests.get("https://api.npoint.io/c4fd7d8696262debee56")


@app.route('/')
@app.route('/index.html')
def home():
    blog_content = get_blog_content().json()
    return render_template("index.html", year=year, blog_content=blog_content)

@app.route("/<string:page>")
def page(page: str):
    return render_template(page, year=year)

@app.route("/post/<int:index>")
def show_post(index: int):
    blog_content = get_blog_content().json()
    for content in blog_content:
        if content["id"] == index:
            return render_template("post.html", request_post=content, year=year)
    return render_template("404.html", year=year)

if __name__ == "__main__":
    app.run(debug=True)