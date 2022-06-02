from flask import current_app as app, render_template, flash, redirect, url_for
from flask_login import current_user
import stripe
from .models import Cart
from app import db

stripe.api_key = app.config.get('STRIPE_SK')

@app.route("/shop")
def shop_list():
    products=[]
    for product in stripe.Product.list()['data']:
        price = stripe.Price.retrieve(product['default_price'])['unit_amount'] / 100
        product_dict ={
            'id': product['id'],
            'name': product['name'],
            'description': product['description'],
            'price': f"{price:,.2f}",
            'image': product['images'][0]
        }
        products.append(product_dict)
    return render_template('shop/list.html', products=products)

@app.route("/shop/<int:id>")
def shop_single(id):
    return "Shop Single Page"

@app.route("/shop/cart")
def shop_cart():
    return render_template('/shop/cart.html')

@app.route('/shop/cart/add/<product_id>')
def shop_cart_add(product_id):
    product = stripe.Product.retrieve(product_id)
    user_cart = Cart.query.filter_by(user_id=current_user.get_id())

    cart_product = user_cart.filter_by(product_id=product_id).first()

    if cart_product is None:
        cart = Cart(
            product_id=product_id, 
            user_id=current_user.get_id(),
            quantity=1
        )
        db.session.add(cart)
    
    else:
        cart_product.quantity += 1
    db.session.commit()

    flash('You have added that product successfully', 'primary')
    return redirect(url_for('shop_list'))

@app.route("/shop/checkout")
def shop_checkout():
    return "shop checkout"
    
