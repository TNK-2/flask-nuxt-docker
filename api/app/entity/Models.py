import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
sys.path.append('/app/conf')
from dbconf import ENGINE

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(200), unique=True)
    sessionid = Column('sessionid', String(100))

class Note(Base):
    __tablename__ = 'note'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    userid = Column('userid', Integer, ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'))
    title = Column('title', String(200))
    text = Column('text', String(2000))

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)