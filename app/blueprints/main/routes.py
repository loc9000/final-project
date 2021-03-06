from webbrowser import get
from flask import render_template, current_app as app, request, redirect, url_for, flash
from datetime import datetime as dt
from app.blueprints.blog.models import Post, User
from app import db
from flask_login import current_user, login_required
import requests

@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        data = request.form.get('blog_post')
        p = Post(body=data, author=current_user.get_id())
        db.session.add(p)
        db.session.commit()
        flash('You have created a new post', 'info')
        return redirect(url_for('home'))
    
    return render_template('main/home.html', posts=[post.to_dict() for post in Post.query.order_by(Post.date_created.desc()).all()])

@app.route('/delete/<id>')
def delete_post(id):
    post_to_delete = Post.query.get(id)
    print(post_to_delete)

    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash('Post deleted', 'warning')
        return render_template('main/home.html', posts=[post.to_dict() for post in Post.query.order_by(Post.date_created.desc()).all()])
        
        
    except:
        flash('There was a problem deleting the post', 'warning')
        return render_template('main/home.html', posts=[post.to_dict() for post in Post.query.order_by(Post.date_created.desc()).all()])

@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():

    if request.method == 'POST':
        form_data = request.form
        user = User.query.get(current_user.get_id())

        user.first_name = form_data.get('first_name')
        user.last_name = form_data.get('last_name')
        user.email = form_data.get('email')

        if len(form_data.get('password')) == 0:
            pass
        elif form_data.get('password') == form_data.get('confirm_password'):
            user.generate_password(form_data.get('password'))
        else:
            flash('There was an error updating your password', 'danger')
            return redirect(url_for('profile'))

        db.session.commit()

        flash('You have updated your user information', 'success')
        return redirect(url_for('profile'))

    return render_template('main/profile.html', posts=[post.to_dict() for post in Post.query.filter_by(author=current_user.get_id()).order_by(Post.date_created.desc()).all()])
    
@app.route("/contact")
@login_required
def contact():
    return render_template('main/contact.html')



