import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from indralab_auth_tools.conf import get_indra_conf

logger = logging.getLogger(__name__)

try:
    db_config = get_indra_conf("INDRALAB_USERS_DB", missing_ok=False)
    # This is for handling empty strings set as the environmental variable
    if not db_config:
        raise KeyError()
    engine = create_engine(db_config)
    db_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    Base = declarative_base()
    Base.query = db_session.query_property()
except KeyError:
    engine = None

    class Base(object):
        pass

    logger.warning("Missing INDRLAB_USERS_DB var, cannot use database.")


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_user_db()
    import indralab_auth_tools.src.models as models

    Base.metadata.create_all(bind=engine)
