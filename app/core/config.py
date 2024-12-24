from os import getenv

from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession
)
from sqlalchemy.orm import DeclarativeBase


db_user, db_password, db_host, db_port, db_name = (
    getenv("DB_USER"), getenv("DB_PASSWORD"), getenv("DB_HOST"),
    getenv("DB_PORT"), getenv("DB_NAME")
)
db_url = (f"postgresql+asyncpg://"
          f"{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

engine = create_async_engine(db_url)
async_session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass
