from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED

from app.core import async_session_maker

create_flight_router = APIRouter(tags=["flight"])


@create_flight_router.post(path="/create_flight", status_code=HTTP_201_CREATED)
async def create_flight(flight_data: Annotated[FlightData, Depends()]):

