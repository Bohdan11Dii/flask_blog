from flask import Blueprint, render_template, request
from blog.models.post import Post

main_bp = Blueprint("main", __name__)


@main_bp.route('/')
def home():  # put application's code here
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_post.desc()).paginate(page=page, per_page=6)
    return render_template("home/index.html", posts=posts, subtitle="This is my Blog")


@main_bp.route('/about/')
def about():  # put application's code here
    return render_template("about/about.html")
