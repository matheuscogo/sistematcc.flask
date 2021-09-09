def init_app(app):
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///sistemaTCC.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False