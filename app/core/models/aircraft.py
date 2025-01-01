from sqlalchemy import Column, Integer, String, DateTime, func

from app.core import Base


class Aircraft(Base):
    __tablename__ = "aircraft"

    aircraft_id = Column(type_=Integer, primary_key=True, autoincrement=True)
    name = Column(type_=String(20), nullable=False, unique=True, index=True)

    weight_in_tons = Column(type_=Integer, nullable=False)
    length_in_meters = Column(type_=Integer, nullable=False)

    created_or_updated_at = Column(
        type_=DateTime(timezone=True),
        server_default=func.now(), onupdate=func.now(),
    )
