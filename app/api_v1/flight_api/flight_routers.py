from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED

from app.api_v1.flight_api.routers_code import create_flight_code
from app.api_v1.flight_api.schemas import SFlight
from app.core import Flight

create_flight = APIRouter(tags=["flight"])


@create_flight.post(path="/create_flight", status_code=HTTP_201_CREATED)
async def create_flight_view(flight: Annotated[SFlight, Depends()]):
    new_flight = Flight(
        flight_name=flight.flight_name,
        departure_country=flight.departure_country,
        departure_city=flight.departure_city,
        departure_date_time=flight.departure_date_time,
        arrival_country=flight.arrival_country,
        arrival_city=flight.arrival_city,
        arrival_date_time=flight.arrival_date_time,
        aircraft_name=flight.aircraft_name,
        ticket_cost_in_usd=flight.ticket_cost_in_usd
    )

    return await create_flight_code(new_flight=new_flight)
