from flask import Flask
from app.router import product_bp

application=Flask(__name__)
application.register_blueprint(product_bp)