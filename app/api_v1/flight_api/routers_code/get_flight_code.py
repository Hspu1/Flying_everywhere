from app.api_v1.error_messages import no_object
from app.core import async_session_maker


async def get_flight_code(query):
    async with async_session_maker() as session:
        result = await session.execute(query)
        response = result.scalars().first()

        return response if response else no_object(correction="полёта")
