from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
<<<<<<< HEAD
from dspBossAdmin_config import SQLALCHEMY_DATABASE_URI


connection_string = SQLALCHEMY_DATABASE_URI
=======
from dspBossAdmin.settings import Config


connection_string = f'{Config.SQLALCHEMY_DATABASE_URI}'
>>>>>>> d29c36829f781153b651d297daf7d9af31302f4e
engine = create_engine(connection_string)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
<<<<<<< HEAD
    # they will be registered properly on the metadata.
=======
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
>>>>>>> d29c36829f781153b651d297daf7d9af31302f4e
    import dspBossAdmin.models.system
    Base.metadata.create_all(bind=engine)

