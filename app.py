from blog import create_app, db
from blog.models.user import User
from blog.models.post import Post


if __name__ == '__main__':

    create_app.run(debug=True)
