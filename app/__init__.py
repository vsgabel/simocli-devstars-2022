from flask import Flask
from config import config

# mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    if not app.config['API_KEY']:
        raise Exception("API Key not found")

    # mail.init_app(app)

    from app.auth import auth as auth_bp
    from app.main import main as main_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, prefix='/auth')

    return app