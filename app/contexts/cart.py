from flask import current_app as app
from flask_login import current_user
import stripe
from app.blueprints.shop.models import Cart

@app.context_processor
def cart_context():
    cart_dict={}
    if current_user.is_anonymous:
        {
            'cart_items': cart_dict,
            'cart_size': 5,
            'cart_subtotal': 0,
            'cart_grandtotal': 0, 
        }
    cart = Cart.query.filter_by(user_id=current_user.get_id()).all()
    return {
            'cart_items': cart_dict,
            'cart_size': sum([product.quantity for product in cart]),
            'cart_subtotal': 0,
            'cart_grandtotal': 0, 
        }