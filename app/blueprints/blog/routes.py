from flask import current_app as app, render_template, request, redirect, url_for, flash
from .models import User, Post
from flask_login import current_user, login_user, logout_user
from app import db

@app.route("/users")
def user_list():
    return render_template('users/list.html')

@app.route("/users/<int:id>")
def user_single(id):
    return "User Single Page"

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_data = request.form
        user = User.query.filter_by(email=form_data.get('email')).first()
        
        if user is None or not user.check_password(form_data.get('password')):
            flash('Either that email address or password is incorrect. Please try again.', 'warning')
            return redirect(url_for('login'))

        login_user(user, remember=form_data.get('remember_me'))
        flash('You have logged in successfully', 'success')
        return redirect(url_for('home'))
    return render_template('users/login.html')

@app.route('/users/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form_data = request.form

        email = User.query.filter_by(email=form_data.get('email')).first()
        if email is not None:
            flash('That email address is already in use. Please try another one', 'warning')
            return(redirect(url_for('register')))

        if form_data.get('password') == form_data.get('confirm_password'):
            user = User(
                first_name=form_data.get('first_name'),
                last_name=form_data.get('last_name'),
                email=form_data.get('email')
            )
            user.generate_password(form_data.get('password'))
            db.session.add(user)
            db.session.commit()

            login_user(user, remember=True)
            flash('You have registered successfully', 'success')
            return redirect(url_for('home'))
        else: 
            flash("Your passwords don't match. Please try again", 'warning')
            return redirect(url_for('register'))
    return render_template('users/register.html')

@app.route('/users/logout')
def logout():
    logout_user()
    flash('You have logged out successfully', 'primary')
    return redirect(url_for('login'))

@app.route('/blog/update', methods=['POST'])
def blog_profile():
    if request.method == 'POST':
        data = request.form.get('blog_post')
        p = Post(body=data, author=current_user.get_id())
        db.session.add(p)
        db.session.commit()

        flash('You have created a new post', 'info')
        return redirect(url_for('profile'))

