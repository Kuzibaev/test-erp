from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:1@localhost/test_db"

engine = create_engine(
    os.getenv("DB_URL", SQLALCHEMY_DATABASE_URL)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
