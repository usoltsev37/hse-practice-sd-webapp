from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException

from fake_db import data

router = APIRouter(prefix="/person", tags=["person"])
routerStudent = APIRouter(prefix="/student", tags=["student"])
routerTeacher = APIRouter(prefix="/teacher", tags=["teacher"])


@router.get("/id/{person_id}")
async def get_by_id(person_id: Optional[int] = None):
    if person_id not in data:
        raise HTTPException(status_code=400, detail="Id does not exist")
    return data[person_id]

@router.get("/id/{person_id}/type")
async def get_type_by_id(person_id: Optional[int] = None):
    if person_id not in data:
        raise HTTPException(status_code=400, detail="Id does not exist")
    return data[person_id].type