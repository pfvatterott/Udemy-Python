from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    get_blog_response = requests.get("https://api.npoint.io/fe3256db6ec2406e3102")
    get_blog_response.raise_for_status()
    blog_data = get_blog_response.json()
    return render_template("index.html", posts=blog_data)

@app.route("/blog/<id>")
def get_blog(id):
    print(id)
    get_blog_response = requests.get("https://api.npoint.io/fe3256db6ec2406e3102")
    get_blog_response.raise_for_status()
    blog_data = get_blog_response.json()
    for blog in blog_data:
        if blog["id"] == int(id):
            return render_template("post.html", id=id, post=blog)
    


if __name__ == "__main__":
    app.run(debug=True)
