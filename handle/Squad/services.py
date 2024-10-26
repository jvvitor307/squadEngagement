from sqlalchemy.orm import Session, joinedload
from database.database import Squad, Person
from handle.Squad.models import SquadCreate


class SquadServices:

    def add(self, db: Session, obj: SquadCreate):
        novo = Squad(
            squad_name = obj.squad_name
        )
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo

    def get_by_id(self, db: Session, id: int):
        return db.query(Squad).filter(Squad.id == id).first()

    def get_all(self, db: Session, id: int):
        return db.query(Squad).all()

    def update(self, db: Session, squad: Squad, SquadModel: SquadCreate):
        squad.squad_name = SquadModel.squad_name
        db.commit()
        db.refresh(squad)

    def delete(self, db: Session, squad: Squad):
        db.delete(squad)
        db.commit()
        db.refresh(squad)

    def addPessoas(self, db: Session, squad: Squad, person: Person):




