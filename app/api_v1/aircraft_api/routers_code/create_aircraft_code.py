from app.core import async_session_maker


async def create_aircraft_code(new_aircraft):
    async with async_session_maker() as session:
        async with session.begin():
            session.add(new_aircraft)
