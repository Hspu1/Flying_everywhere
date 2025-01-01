from datetime import datetime

from pydantic import BaseModel, Field


class SFlight(BaseModel):
    flight_name: str = Field(
        max_length=30, default="Название полёта (до 30 символов)"
    )

    departure_country: str = Field(
        max_length=50, default="Страна вылета (до 50 символов)")
    departure_city: str = Field(
        max_length=50, default="Город вылета (до 50 символов)")
    departure_date_time: datetime = Field(
        default="YYYY-MM-DD HH:MM:SS or YYYY-MM-DD")

    arrival_country: str = Field(
        max_length=50, default="Страна прилёта (до 50 символов)")
    arrival_city: str = Field(
        max_length=50, default="Город прилёта (до 50 символов)")
    arrival_date_time: datetime = Field(
        default="YYYY-MM-DD HH:MM:SS or YYYY-MM-DD")

    aircraft_name: str = Field(
        max_length=20, default="Название самолёта (до 20 символов)")
    ticket_cost_in_usd: int = Field(
        ge=1, le=100_000_000, default="Цена в долларах США (целое число)")
