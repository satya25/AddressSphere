from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import and register blueprints
    from .routes import address_bp
    app.register_blueprint(address_bp, url_prefix='/api')
    
    return app
