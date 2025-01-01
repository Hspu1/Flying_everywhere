from fastapi import HTTPException


def cannot_create_new_object():
    raise HTTPException(
        status_code=409,
        detail="Самолёт с таким названием уже существует"
    )


def no_data():
    raise HTTPException(
        status_code=404,
        detail="В базе данных пока нет ни одного самолёта"
    )


def no_object():
    raise HTTPException(
        status_code=404,
        detail="В базе данных пока нет самолёта с таким названием"
    )
