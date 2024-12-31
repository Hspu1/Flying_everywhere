from app.api_v1.aircraft_api.error_messages import no_aircraft
from app.core import async_session_maker


async def get_aircraft_code(select_query):
    async with async_session_maker() as session:
        result = await session.execute(select_query)
        response = result.scalars().first()

        return response if response else no_aircraft()
