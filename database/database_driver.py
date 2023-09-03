from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models.base_model import Base
from database.models.tweet import Tweet
from database.models.twitter_user import TwitterUser


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autoflush=True, bind=engine)



Base.metadata.create_all(bind=engine)
table_objects = [TwitterUser.__table__, Tweet.__table__]
Base.metadata.create_all(engine, tables=table_objects)

db_session = SessionLocal()

# Dependency
def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()