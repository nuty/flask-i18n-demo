from flask.ext.script import Server, Manager
from demo.app import app
from demo import *
from flask.ext.babel import gettext
manager = Manager(app)

manager.add_command("runserver", Server('0.0.0.0', port=5000))


if __name__ == "__main__":
    manager.run()
