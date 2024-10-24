from flask import Flask
from app.router import login_bp,register_bp

application=Flask(__name__)
application.register_blueprint(login_bp)
application.register_blueprint(register_bp)