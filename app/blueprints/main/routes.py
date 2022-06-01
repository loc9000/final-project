from webbrowser import get
from flask import render_template, current_app as app, request, redirect, url_for, flash
from datetime import datetime as dt
from app.blueprints.blog.models import Post
from app import db
from flask_login import current_user

@app.route("/", methods=['GET', 'POST', 'DELETE'])
def home():

    if request.method == 'POST':
        data = request.form.get('blog_post')

        p = Post(body=data, author=current_user.get_id())
        db.session.add(p)
        db.session.commit()

        flash('You have created a new post', 'info')
        return redirect(url_for('home'))

    if request.method == 'DELETE':
        post = Post.query.get(id)

        db.session.delete(post)
        db.session.commit()

        flash('Post deleted', 'danger')
        return redirect(url_for('home'))

    
    return render_template('main/home.html', posts=[post.to_dict() for post in Post.query.order_by(Post.date_created.desc()).all()])

@app.route("/profile")
def profile():
    return render_template('main/profile.html')
    
@app.route("/contact")
def contact():
    return "Contact Page"
