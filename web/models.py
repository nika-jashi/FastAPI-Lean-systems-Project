from sqlalchemy import Column, Integer, String, DateTime
from web.database import Base


class Posts(Base):
    __tablename__ = 'web'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    category = Column(String)
    author = Column(String)
    date_posted = Column(DateTime)
    view_count = Column(Integer, default=0)

    def __repr__(self):
        return self.title
