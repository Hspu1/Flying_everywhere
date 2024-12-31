from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED

from app.api_v1.aircraft_api.routers_code import create_aircraft_code
from app.api_v1.aircraft_api.schemas import SAircraft
from app.core import Aircraft

(
    create_aircraft, get_all_aircraft, get_aircraft_by_name,
    update_aircraft_name, delete_aircraft
) = (
    APIRouter(tags=["aircraft"]), APIRouter(tags=["aircraft"]),
    APIRouter(tags=["aircraft"]), APIRouter(tags=["aircraft"]),
    APIRouter(tags=["aircraft"])
)


@create_aircraft.post(path="/create_aircraft", status_code=HTTP_201_CREATED)
async def create_aircraft_view(aircraft: Annotated[SAircraft, Depends()]):
    new_aircraft = Aircraft(
        name=aircraft.name, weight=aircraft.weight, length=aircraft.length
    )

    return await create_aircraft_code(new_aircraft=new_aircraft)
