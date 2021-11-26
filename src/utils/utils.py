from src.services.crud import Session
from src.entities.news import New

def already_exists(url):
    session = Session()
    if session.query(New).filter(New.url == url).first():
        session.close()
        return True
    else:
        session.close()
        return False
