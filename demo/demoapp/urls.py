from demo.demoapp.views import index, lang
from demo.app import app

app.add_url_rule('/', view_func=index, methods=['GET'])
app.add_url_rule('/lang', view_func=lang, methods=['GET'])
