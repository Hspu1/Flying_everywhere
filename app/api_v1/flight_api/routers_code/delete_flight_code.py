from app.api_v1.error_messages import no_object
from app.api_v1.flight_api.schemas import flight_existence
from app.core import async_session_maker


async def delete_flight_code(select_query, query):
    if await flight_existence(query=select_query):
        async with async_session_maker() as session:
            async with session.begin():
                return await session.execute(query)

    return no_object(correction="полёта")
