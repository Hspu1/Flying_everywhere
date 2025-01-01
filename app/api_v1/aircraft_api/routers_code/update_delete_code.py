from app.api_v1.aircraft_api.error_messages import no_aircraft
from app.api_v1.aircraft_api.schemas import aircraft_existence
from app.core import async_session_maker


async def update_delete_code(select_query, query):
    if await aircraft_existence(query=select_query):
        async with async_session_maker() as session:
            async with session.begin():
                return await session.execute(query)

    return no_aircraft()
