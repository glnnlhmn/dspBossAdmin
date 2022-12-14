<<<<<<< HEAD
# dspBossAdmin/app.py
=======
# dspBossAdmin.py
>>>>>>> d29c36829f781153b651d297daf7d9af31302f4e

# flask imports
from flask import Flask

# flask security imports
from flask_security import Security, auth_required, hash_password, \
    SQLAlchemySessionUserDatastore

# flask_admin imports
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

<<<<<<< HEAD

from dspBossAdmin.database import db_session, init_db
from dspBossAdmin.models.system import User, Role


class MyView(BaseView):

    def index(self):
        return self.render('admin/index.html')


# Create app
app = Flask(__name__)
app.config.from_pyfile('dspBossAdmin_config.py')

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
app.security = Security(app, user_datastore)

admin = Admin(app, template_mode='bootstrap4')
admin.add_view(ModelView(User, db_session))
admin.add_view(ModelView(Role, db_session))


# Views
@app.route("/")
@auth_required()
def home():
    return '<p><a href="/admin/">Click me to get to Admin!</a></p>'


def create_super_user(rebuild: bool = True):

    if rebuild:
        init_db()

    with app.app_context(): # Uncomment this line to create initial database
        if not app.security.datastore.find_user(username="triton"):
            app.security.datastore.create_user(email="triton@dspBoss.com", username="triton",
                                               password=hash_password("password"))
        db_session.commit()


def main():
    create_super_user(True)
    app.run()


if __name__ == '__main__':
    main()

=======
# dspBossAdmin imports
from dspBossAdmin.settings import Config


from dspBossAdmin.database import db_session, init_db
from dspBossAdmin.models.system import User, Role


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


# Create app
app = Flask(__name__)
app.config['DEBUG'] = f"{Config.DEBUG}"

# Generate a nice key using secrets.token_urlsafe()
app.config['SECRET_KEY'] = f"{Config.SECRET_KEY}"
app.config['SQLALCHEMY_DATABASE_URI']=f"{Config.SQLALCHEMY_DATABASE_URI}"
# Bcrypt is set as default SECURITY_PASSWORD_HASH, which requires a salt
# Generate a good salt using: secrets.SystemRandom().getrandbits(128)
app.config['SECURITY_PASSWORD_SALT'] = f"{Config.SECURITY_PASSWORD_SALT}"

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
app.security = Security(app, user_datastore)

admin = Admin(app)
admin.add_view(ModelView(User, db_session))
admin.add_view(ModelView(Role, db_session))


# Views
@app.route("/")
@auth_required()
def home():
    return '<p><a href="/admin/">Click me to get to Admin!</a></p>'


def main():
    with app.app_context():
        init_db()     # Uncomment this line to create initial database
        if not app.security.datastore.find_user(username="triton"):
            app.security.datastore.create_user(email="test@me.com", username="triton", password=hash_password("password"))
        db_session.commit()
    app.run()


if __name__ == '__main__':
    main()

>>>>>>> d29c36829f781153b651d297daf7d9af31302f4e
