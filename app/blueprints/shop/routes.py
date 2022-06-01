from flask import current_app as app, render_template

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
