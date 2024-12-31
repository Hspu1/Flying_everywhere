from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.api_v1.aircraft_api.routers_code import (
    create_aircraft_code, get_all_aircrafts_code, get_aircraft_code
)
from app.api_v1.aircraft_api.schemas import SAircraft
from app.core import Aircraft

(
    create_aircraft, get_all_aircrafts, get_aircraft,
    update_aircraft_name, delete_aircraft
) = (
    APIRouter(tags=["aircraft"]), APIRouter(tags=["aircraft"]),
    APIRouter(tags=["aircraft"]), APIRouter(tags=["aircraft"]),
    APIRouter(tags=["aircraft"])
)


@create_aircraft.post(path="/create_aircraft", status_code=HTTP_201_CREATED)
async def create_aircraft_view(aircraft: Annotated[SAircraft, Depends()]):
    new_aircraft = Aircraft(
        name=aircraft.name, weight_in_tons=aircraft.weight_in_tons,
        length_in_meters=aircraft.length_in_meters
    )
    return await create_aircraft_code(new_aircraft=new_aircraft)


@get_all_aircrafts.get(path="/get_all_aircrafts", status_code=HTTP_200_OK)
async def get_all_aircrafts_view():
    return await get_all_aircrafts_code()


@get_aircraft.get(path="/get_aircraft", status_code=HTTP_200_OK)
async def get_aircraft_view(aircraft_name: str = Query(max_length=20)):
    query = select(Aircraft).where(Aircraft.name == aircraft_name)
    return await get_aircraft_code(select_query=query)
