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

@app.route("/guess/<name>") 
def guess(name):
    get_age_response = requests.get(url=f"https://api.agify.io?name={name}")
    get_age_response.raise_for_status()
    age_data = get_age_response.json()
    
    get_gender_response = requests.get(url=f"https://api.agify.io?name={name}")
    get_gender_response.raise_for_status()
    gender_data = get_age_response.json()
    
    
    
    
    return render_template("index.html", age=age_data["age"], gender=gender_data["gender"], name=name)
    

if __name__ == "__main__":
    app.run(debug=True)