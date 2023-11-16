import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.utils.dev.config import DB_URL, DB_HOSTNAME, DB_PORT, DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_CHARSET

engine = create_engine(url=DB_URL, echo=True)

SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = SessionLocal.query_property()


async def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise e


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def execute_query(query: str):
    conn = pymysql.connect(
        host=DB_HOSTNAME,
        port=DB_PORT,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        database=DB_DATABASE,
        charset=DB_CHARSET,
        autocommit=True,
    )
    curs = conn.cursor()
    curs.execute(query)
    curs.close()
    return curs.fetchall()
