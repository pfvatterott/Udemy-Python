from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, currentYear=current_year)

@app.route("/blog/<num>")
def get_blog(num):
    get_blog_response = requests.get("https://api.npoint.io/fe3256db6ec2406e3102")
    get_blog_response.raise_for_status()
    blog_data = get_blog_response.json()
    return render_template("blog.html", posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)