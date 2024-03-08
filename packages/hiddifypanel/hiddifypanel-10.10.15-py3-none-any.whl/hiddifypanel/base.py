from flask import request, g
# from hiddifypanel.cache import cache
from hiddifypanel.models import *

import flask_bootstrap
import hiddifypanel
from flask_babel import Babel
from flask_session import Session

import datetime

from dotenv import dotenv_values
import os
from apiflask import APIFlask
from werkzeug.middleware.proxy_fix import ProxyFix

from hiddifypanel.panel.init_db import init_db
from hiddifypanel.cache import redis_client
from hiddifypanel import auth
from hiddifypanel.panel import hiddify
from hiddifypanel import hutils


def create_app(*args, cli=False, **config):

    app = APIFlask(__name__, static_url_path="/<proxy_path>/static/", instance_relative_config=True, version='2.0.0', title="Hiddify API",
                   openapi_blueprint_url_prefix="/<proxy_path>/api", docs_ui='elements', json_errors=False, enable_openapi=True)
    # app = Flask(__name__, static_url_path="/<proxy_path>/static/", instance_relative_config=True)

    app.config["PREFERRED_URL_SCHEME"] = "https"
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1,
    )
    app.servers = {
        'name': 'current',
        'url': '',
    }  # type: ignore
    app.info = {
        'description': 'Hiddify is a free and open source software. It is as it is.',
        'termsOfService': 'https://hiddify.com',
        'contact': {
            'name': 'API Support',
            'url': 'https://www.hiddify.com/support',
            'email': 'panel@hiddify.com'
        },
        'license': {
            'name': 'Creative Commons Zero v1.0 Universal',
            'url': 'https://github.com/hiddify/Hiddify-Manager/blob/main/LICENSE'
        }
    }
    # setup flask server-side session
    # app.config['APPLICATION_ROOT'] = './'
    # app.config['SESSION_COOKIE_DOMAIN'] = '/'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redis_client
    app.config['SESSION_PERMANENT'] = True
    app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=10)
    Session(app)
    app.jinja_env.line_statement_prefix = '%'
    app.jinja_env.filters['b64encode'] = hutils.encode.do_base_64
    app.view_functions['admin.static'] = {}  # fix bug in apiflask
    flask_bootstrap.Bootstrap4(app)

    for c, v in dotenv_values(os.environ.get("HIDDIFY_CFG_PATH", 'app.cfg')).items():
        if v.isdecimal():
            v = int(v)
        else:
            v = True if v.lower() == "true" else (False if v.lower() == "false" else v)

        app.config[c] = v

    hiddifypanel.database.init_app(app)
    with app.app_context():
        init_db()
 # flaskbabel = FlaskBabel(app)

    # @babel.localeselector
    def get_locale():
        # Put your logic here. Application can store locale in
        # user profile, cookie, session, etc.
        from hiddifypanel.models import ConfigEnum, hconfig
        if "admin" in request.base_url:
            g.locale = auth.current_account.lang or hconfig(ConfigEnum.admin_lang) or 'fa'
        else:
            g.locale = auth.current_account.lang or hconfig(ConfigEnum.lang) or 'fa'
        return g.locale
    babel = Babel(app, locale_selector=get_locale)

    hiddifypanel.panel.common.init_app(app)
    hiddifypanel.panel.common_bp.init_app(app)

    from hiddifypanel.panel import user, commercial, admin
    admin.init_app(app)
    user.init_app(app)
    commercial.init_app(app)

    app.config.update(config)  # Override with passed config
    # app.config['WTF_CSRF_CHECK_DEFAULT'] = False
    app.config['WTF_CSRF_ENABLED'] = False
    # app.config['BABEL_TRANSLATION_DIRECTORIES'] = '/workspace/Hiddify-Server/hiddify-panel/src/translations.i18n'

    # from flask_wtf.csrf import CSRFProtect

    # csrf = CSRFProtect(app)

    # @app.before_request
    # def check_csrf():
    # if "/admin/user/" in request.base_url:
    #     return
    # if "/admin/domain/" in request.base_url:
    #     return
    # if "/admin/actions/" in request.base_url:
    #     return
    # if "/api/" in request.base_url:
    #     return
    # csrf.protect()

    app.jinja_env.globals['get_locale'] = get_locale

    hiddifypanel.panel.cli.init_app(app)
    return app


def create_app_wsgi(*args, **kwargs):
    # workaround for Flask issue
    # that doesn't allow **config
    # to be passed to create_app
    # https://github.com/pallets/flask/issues/4170
    app = create_app()
    return app


# def create_cli_app(*args, **kwargs):
#     #     # workaround for Flask issue
#     #     # that doesn't allow **config
#     #     # to be passed to create_app
#     #     # https://github.com/pallets/flask/issues/4170
#     # print(kwargs)
#     app = create_app(*args, cli=True, **kwargs)
#     return app
