from sqlalchemy import Column, Integer, String

from app.core import Base


class Aircraft(Base):
    __tablename__ = "aircraft"

    aircraft_id = Column(type_=Integer, primary_key=True, autoincrement=True)
    name = Column(type_=String(20), nullable=False, index=True)
    weight = Column(type_=Integer, nullable=False)
    length = Column(type_=Integer, nullable=False)
