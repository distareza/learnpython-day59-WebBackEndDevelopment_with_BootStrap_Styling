import smtplib

from flask import Flask, render_template, request
from datetime import date
import requests
import my_configuration
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

"""
    https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods
    https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object
"""
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    return f"User name : {username}, Password : {password}"



@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP(host=my_configuration.email_provider_smtp_address, port=my_configuration.email_port) as connection:
        connection.starttls()
        connection.login(my_configuration.email_sender, my_configuration.email_password)
        connection.sendmail(my_configuration.email_sender, my_configuration.email_sender, email_message)


if __name__ == "__main__":
    app.run(debug=True)