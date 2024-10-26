from pydantic import BaseModel
from handle.Person.models import PersonCreate
from typing import List, Optional


class SquadCreate(BaseModel):
    squad_name: str
    members: Optional[List[PersonCreate]] = []

class SquadView(SquadCreate):
    id: int
