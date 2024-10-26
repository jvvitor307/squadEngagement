from pydantic import BaseModel


class PersonCreate(BaseModel):
    first_name: str
    last_name: str

class PersonView(PersonCreate):
    id: int
