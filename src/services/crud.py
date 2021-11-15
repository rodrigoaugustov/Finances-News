from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from src.services import DATABASE_URI

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