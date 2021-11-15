from src.services.crud import Session
from src.entities.news import New


def already_exists(url):
    s = Session()
    if s.query(New).filter(New.url == url).first():
        s.close()
        return True
    else:
        s.close()
        return False
