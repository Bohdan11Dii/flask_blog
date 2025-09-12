from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import current_user, login_required
from blog import db
from blog.models.post import Post
from blog.forms.form_post import PostForm

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')


@posts_bp.route('/post/new/', methods=['GET', 'POST'])
@login_required
def new_post():
    subtitle = "Create New Post"
    form = PostForm()

    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", "success")
        return redirect(url_for("main.home"))

    return render_template(
        "post/create_post.html",
        subtitle=subtitle,
        form=form,
        legend="New Post",
    )


@posts_bp.route('/post/<int:post_id>/', methods=['GET', 'POST'])
def post(post_id):  # put application's code here
    post = Post.query.get_or_404(post_id)
    return render_template("post/post.html", subtitle=post.title, post=post)


@posts_bp.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    subtitle = f"Update Post {post.title}"
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated!", "success")
        return redirect(url_for("posts.post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template(
        "post/create_post.html",
        subtitle=subtitle,
        form=form,
        legend="Update Post",
    )


@posts_bp.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):  # put application's code here
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for("main.home"))
