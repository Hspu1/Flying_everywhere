from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select, delete, update
from starlette.status import (
    HTTP_201_CREATED, HTTP_200_OK, HTTP_202_ACCEPTED
)

from app.api_v1.aircraft_api.routers_code import (
    create_aircraft_code, get_all_aircrafts_code, get_aircraft_code,
    update_delete_code
)
from app.api_v1.aircraft_api.schemas import (
    SAircraft, SAircraftNames, SAircraftUpdate
)
from app.core import Aircraft

(
    create_aircraft, get_all_aircrafts, get_aircraft,
    update_aircraft_name, update_aircraft_data, delete_aircraft
) = (
    APIRouter(tags=["aircraft"]), APIRouter(tags=["aircraft"]),
    APIRouter(tags=["aircraft"]), APIRouter(tags=["aircraft"]),
    APIRouter(tags=["aircraft"]), APIRouter(tags=["aircraft"])
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
async def get_aircraft_view(name: str = Query(max_length=20)):
    query = select(Aircraft).where(Aircraft.name == name)
    return await get_aircraft_code(query=query)


@update_aircraft_name.patch(path="/update_aircraft_name", status_code=HTTP_202_ACCEPTED)
async def update_aircraft_name_view(names: Annotated[SAircraftNames, Depends()]):
    select_query = select(Aircraft).where(Aircraft.name == names.old_name)
    update_query = update(Aircraft).where(Aircraft.name == names.old_name).values(name=names.new_name)

    return await update_delete_code(
        select_query=select_query, query=update_query
    )


@update_aircraft_data.put(path="/update_all_aircraft_data", status_code=HTTP_202_ACCEPTED)
async def update_aircraft_data_view(new_data: Annotated[SAircraftUpdate, Depends()]):
    select_query = select(Aircraft).where(Aircraft.name == new_data.old_name)
    update_query = update(Aircraft).where(Aircraft.name == new_data.old_name
    ).values(
        name=new_data.new_name, weight_in_tons=new_data.weight_in_tons,
        length_in_meters=new_data.length_in_meters
    )

    return await update_delete_code(
        select_query=select_query, query=update_query
    )


@delete_aircraft.delete(path="/delete_aircraft", status_code=HTTP_202_ACCEPTED)
async def delete_aircraft_view(name: str = Query(max_length=20)):
    select_query = select(Aircraft).where(Aircraft.name == name)
    delete_query = delete(Aircraft).where(Aircraft.name == name)

    return await update_delete_code(
        select_query=select_query, query=delete_query
    )
