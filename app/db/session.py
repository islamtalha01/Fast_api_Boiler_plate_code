from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core import config
from fastapi import Depends

engine = create_engine(
    # config.SQLALCHEMY_DATABASE_URI,
    "postgresql://postgres:727272@localhost:5432/ANWARSON DATA",
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
