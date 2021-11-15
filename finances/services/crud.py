from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from finances.services import DATABASE_URI

from finances.entities.news import New, Base


engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

@contextmanager
def create_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()