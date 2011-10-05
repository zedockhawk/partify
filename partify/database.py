from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import DATABASE

# Sets up the SQLAlchemy db engine
# Currently using SQLite
engine = create_engine(DATABASE, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """Initializes the database from the models specified in models.py."""
    from models import User
    Base.metadata.create_all(bind=engine)

def clear_db():
    """Clears the database of all entities."""
    Base.metadata.drop_all(bind=engine)

def reset_db():
    """Clears and re-initializes the database."""
    clear_db()
    init_db()

if __name__ == "__main__":
    init_db()