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

# user routes

@app.route("/users")
def user_list():
    return "Users Page"

@app.route("/users/<int:id>")
def user_single(id):
    return "User Single Page"

# shop routes

@app.route("/shop")
def shop_list():
    return "Shop List Page"

@app.route("/shop/<int:id>")
def shop_single(id):
    return "Shop Single Page"

@app.route("/shop/cart")
def shop_cart():
    return "Shop Cart Page"

@app.route("/shop/checkout")
def shop_checkout():
    return "Shop Checkout Page"

