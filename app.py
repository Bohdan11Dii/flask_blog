from blog import app, db
from blog.models.user import User
from blog.models.post import Post


if __name__ == '__main__':

    app.run(debug=True)
