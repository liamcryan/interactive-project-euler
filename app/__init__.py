import io
import json

from flask import Flask, jsonify, request, send_file, make_response, render_template
from ieuler.client import Client, BadCaptcha, LoginUnsuccessful


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
    def index():
        return render_template('index.html')

    @app.route('/captcha')
    def captcha():
        client = Client()
        captcha_raw = client.get_captcha_raw()
        response = make_response(send_file(io.BytesIO(captcha_raw),
                                           mimetype='image/jpeg', ))
        response.headers['Authorization'] = json.dumps(client.session.cookies.get_dict())
        return response

    @app.route('/login', methods=['POST'])
    def login():
        client = Client()
        try:
            cookies = json.loads(request.headers['Authorization'])
        except KeyError:
            return jsonify({})

        client.session.cookies.update(cookies)

        username = request.json['username']
        password = request.json['password']
        _captcha = request.json['captcha']
        for _ in (username, password, _captcha):
            if not _:
                return jsonify({'message': 'username, password, and captcha must be valid'}), 400
        try:
            client.login(username=username,
                         password=password,
                         captcha=_captcha)
        except (BadCaptcha, LoginUnsuccessful) as e:
            return jsonify(e.args), 401

        cookies = client.session.cookies.get_dict()

        return jsonify(cookies)

    return app
