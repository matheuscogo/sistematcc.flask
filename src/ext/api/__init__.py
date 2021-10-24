from .routes import bp_controller

def init_app(app):
    app.register_blueprint(bp_controller)