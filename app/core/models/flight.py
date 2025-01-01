from sqlalchemy import (
    Column, Integer, String, DateTime, func, ForeignKey
)

from app.core import Base


class Flight(Base):
    __tablename__ = "flight"

    flight_id = Column(type_=Integer, primary_key=True, autoincrement=True)
    flight_name = Column(
        type_=String(30), nullable=False, unique=True, index=True
    )

    departure_country = Column(type_=String(50), nullable=False)
    departure_city = Column(type_=String(50), nullable=False)
    departure_date_time = Column(
        type_=DateTime, nullable=False,
        comment="format -> YYYY-MM-DD HH:MI:SS"
    )

    arrival_country = Column(type_=String(50), nullable=False)
    arrival_city = Column(type_=String(50), nullable=False)
    arrival_date_time = Column(
        type_=DateTime, nullable=False,
        comment="format -> YYYY-MM-DD HH:MI:SS"
    )

    aircraft_name = Column(
        String, ForeignKey("aircraft.name")
    )
    ticket_cost = Column(type_=Integer, nullable=False)

    created_or_updated_at = Column(
        type_=DateTime(timezone=True),
        server_default=func.now(), onupdate=func.now(),
    )
