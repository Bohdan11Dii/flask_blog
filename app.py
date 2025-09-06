from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
