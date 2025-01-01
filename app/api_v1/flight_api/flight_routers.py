from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED

create_flight = APIRouter(tags=["flight"])


@create_flight.post(path="/create_flight", status_code=HTTP_201_CREATED)
async def create_flight_view(flight: Annotated[SFlight, Depends()]):

