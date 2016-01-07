from flask import Flask, request, session, current_app
from config import Configuration
from flask.ext.babel import Babel

app = Flask("demo")
app.config.from_object(Configuration)
app.template_folder = Configuration.APP_ROOT + "/templates"

app.debug = True

app.config['SECRET_KEY'] = Configuration.SECRET_KEY
app.config['BABEL_DEFAULT_LOCALE'] = 'en_US'
babel = Babel(app)

LANGUAGES = Configuration.LANGUAGES


@babel.localeselector
def get_locale():
    lang_req = request.args.get('lang', None)
    lang_list = current_app.config['LANGUAGES']
    if lang_req is None or (lang_req not in lang_list):
        lang_session = session.get('lang', None)
        return lang_session if lang_session else \
            request.accept_languages.best_match(lang_list.keys())
    else:
        session['lang'] = lang_req
        return lang_req
