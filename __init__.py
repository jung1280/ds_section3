from flask import Flask


def create_app():

    app = Flask(__name__)

    from routes1 import base

    app.register_blueprint(base.bp1)

    return app

if __name__ == '__main__':

    app = create_app()
    app.run(debug=True, threaded=True)