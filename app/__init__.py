from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='static')

    with app.app_context():
        from . import routes
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .automotive import automotive as automotive_blueprint
    app.register_blueprint(automotive_blueprint, url_prefix='/automotive')

    from .military import military as military_blueprint
    app.register_blueprint(military_blueprint, url_prefix='/military')

    from .equipment import equipment as equipment_blueprint
    app.register_blueprint(equipment_blueprint, url_prefix='/equipment')

    from .software import software as software_blueprint
    app.register_blueprint(software_blueprint, url_prefix='/software')

    from .calculators import calculators as calculators_blueprint
    app.register_blueprint(calculators_blueprint, url_prefix='/calculators')
    
    return app
