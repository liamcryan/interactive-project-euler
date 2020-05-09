import subprocess

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    @app.route('/')
    def env():
        subprocess.Popen(['ttyd', 'docker', 'run', '-it', '--rm', 'liamcryan/ieuler'])
        return render_template('index.html')

    return app
