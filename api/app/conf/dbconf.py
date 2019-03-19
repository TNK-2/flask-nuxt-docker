from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

ENGINE = create_engine(
    'mysql+pymysql://root:password@wisnote-mysql/wisnote?charset=utf8',
    encoding = "utf-8",
    echo=True # Trueだと実行のたびにSQLが出力される
)

if not database_exists(ENGINE.url):
    create_database(ENGINE.url)

dbsession = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

Base = declarative_base()
Base.query = dbsession.query_property()