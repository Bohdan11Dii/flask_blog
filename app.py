from flask import Flask, render_template, flash, redirect, url_for
from blog.forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f1933f4bb571854a19f6624cd7991ff1'

posts = [
    {
        'author': 'Bohdan Isaiovych',
        'title': 'My First Post',
        'content': 'My first post content',
        'date_posted': 'April 10, 1999',
    },
    {
        'author': 'James Adams',
        'title': 'My Second Post',
        'content': 'My second post content',
        'date_posted': 'April 29, 2000',
    }
]


@app.route('/')
def hello_world():  # put application's code here

    return render_template("home/index.html", posts=posts, subtitle="This is my Blog")


@app.route('/about/')
def about():  # put application's code here
    return render_template("about/about.html")


@app.route('/register/', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    subtitle = "Register"
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("hello_world"))
    return render_template("registration/register.html", subtitle=subtitle, form=form)


@app.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    subtitle = "Login"
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("Login successful", "success")
            return redirect(url_for("hello_world"))
        else:
            flash("Login unsuccessful", "danger")

    return render_template("registration/login.html", subtitle=subtitle, form=form)


if __name__ == '__main__':
    app.run(debug=True)
