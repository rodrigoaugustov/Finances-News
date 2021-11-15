from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text

Base = declarative_base()

class New(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    published = Column(DateTime)
    
    def __repr__(self):
        return "<News(title='{}', content='{}', published={})>"\
                .format(self.title, self.content, self.published)