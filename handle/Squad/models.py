from pydantic import BaseModel

class SquadCreate(BaseModel):
    squad_name: str


class SquadView(SquadCreate):
    id: int
