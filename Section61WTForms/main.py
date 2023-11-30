from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4


app = Flask(__name__)
app.secret_key = "some secret string"
bootstrap = Bootstrap4(app)

class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")
    

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    # dont have to do an IF POST anymore, just validate since this is a boolean statement
    if login_form.validate_on_submit():
        print(login_form.email.data)
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
