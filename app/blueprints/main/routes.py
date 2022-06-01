from flask import render_template, current_app as app

@app.route("/")
def home():
    return render_template('main/home.html')

@app.route("/profile")
def profile():
    return render_template('main/profile.html')
    
@app.route("/contact")
def contact():
    return "Contact Page"
