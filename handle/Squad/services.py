from sqlalchemy.orm import Session, joinedload
from database.database import Squad, Person
from handle.Squad.models import SquadCreate


class SquadServices:

    def add(self, db: Session, obj: SquadCreate):
        try:
            novo = Squad(
                squad_name = obj.squad_name
            )
            db.add(novo)
            db.commit()
            db.refresh(novo)
            return novo
        except:
            db.rollback()

    def get_by_id(self, db: Session, id: int):
        return db.query(Squad).filter(Squad.id == id).first()

    def get_all(self, db: Session):
        return db.query(Squad).all()

    def update(self, db: Session, squad: Squad, SquadModel: SquadCreate):
        try:
            squad.squad_name = SquadModel.squad_name
            db.commit()
            db.refresh(squad)
        except:
            db.rollback()


    def delete(self, db: Session, squad: Squad):
        try:
            db.delete(squad)
            db.commit()
            db.refresh(squad)
        except:
            db.rollback()






