from sqlalchemy import Column, Integer, String

from app.core import Base


class Aircraft(Base):
    __tablename__ = "aircraft"

    aircraft_id = Column(type_=Integer, primary_key=True, autoincrement=True)
    aircraft_name = Column(type_=String(20), nullable=False, index=True)
    aircraft_weight = Column(type_=Integer, nullable=False)
    aircraft_length = Column(type_=Integer, nullable=False)
