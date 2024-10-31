from pydantic import BaseModel


class PersonCreate(BaseModel):
    first_name: str
    last_name: str
    task_points: int
    meet_points: int

class PersonView(PersonCreate):
    id: int
