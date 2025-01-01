from fastapi import HTTPException


def cannot_create_new_object(correction: str):
    raise HTTPException(
        status_code=409,
        detail=f"{correction} с таким названием уже существует"
    )


def no_data(correction: str):
    raise HTTPException(
        status_code=404,
        detail=f"В базе данных пока нет ни одного {correction}"
    )


def no_object(correction: str):
    raise HTTPException(
        status_code=404,
        detail=f"В базе данных пока нет {correction} с таким названием"
    )


def cannot_create_flight():
    raise HTTPException(
        status_code=409,
        detail="В базе данных уже есть полёт с таким названием "
               "или/и в базе данных пока нет самолёта с таким названием"
    )
