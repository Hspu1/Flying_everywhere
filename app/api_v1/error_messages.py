from fastapi import HTTPException


def cannot_create_new_object(correction: str):
    raise HTTPException(
        status_code=409,
        detail=f"{correction} с таким названием уже существует"
    )


def no_data(correction: str):
    raise HTTPException(
        status_code=404,
        detail=f"В базе данных нет ни одного {correction}"
    )


def no_object(correction: str):
    raise HTTPException(
        status_code=404,
        detail=f"В базе данных нет {correction} с таким названием"
    )


def cannot_create_flight():
    raise HTTPException(
        status_code=409,
        detail="В базе данных уже есть полёт с таким названием "
               "или/и в базе данных нет самолёта с таким названием"
    )


def cannot_update_aircraft_data():
    raise HTTPException(
        status_code=409,
        detail="Самолёт уже выпустили и изменить его данные невозможно"
    )
