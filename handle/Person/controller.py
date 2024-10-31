from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from handle.Person.models import PersonCreate, PersonView
from handle.Person.services import person_service as service
from database.utils import get_db

router = APIRouter(prefix="/app/person", tags=["Person"])

exception_nao_encontado = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Não encontrado"
)


@router.get("/", response_model=List[PersonView])
def get_all(db: Session = Depends(get_db)):
    return service.get_all(db=db)


@router.get("/{id}", response_model=PersonView)
def get_by_id(id: int, db: Session = Depends(get_db)):
    obj = service.get_by_id(db, id)
    if not obj:
        raise exception_nao_encontado

    return obj



@router.post("/", response_model=PersonView, status_code=status.HTTP_201_CREATED)
def create(person: PersonCreate, db: Session = Depends(get_db)):
    novo = service.add(db, person)
    return novo


@router.put("/{id}", response_model=PersonView)
def update(id: int, obj: PersonCreate, db: Session = Depends(get_db)):
    obj_to_update = service.get_by_id(db, id)
    if not obj_to_update:
        raise exception_nao_encontado

    service.update(db, obj_to_update, obj)
    return obj_to_update


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    obj_to_delete = service.get_by_id(db, id)
    if not obj_to_delete:
        raise exception_nao_encontado

    service.delete(db, obj_to_delete)
    return obj_to_delete