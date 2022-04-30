from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text

Base = declarative_base()


class New(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    content = Column(Text)
    published = Column(DateTime)
    created = Column(DateTime)
    url = Column(Text)
    source = Column(String(50))

    def __repr__(self):
        return f"<News(\
            title='{self.title}', \
            content='{self.content}', \
            url='{self.url}', \
            published={self.published}, \
            created={self.created}, \
            source='{self.source}')>"
