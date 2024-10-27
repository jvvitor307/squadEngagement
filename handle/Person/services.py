from sqlalchemy.orm import Session, joinedload
from database.database import Person
from handle.Person.models import PersonCreate


class PersonServices:

    def add(self, db: Session, obj: PersonCreate):
        try:
            novo = Person(
                first_name=obj.first_name,
                last_name=obj.last_name,
            )
            db.add(novo)
            db.commit()
            db.refresh(novo)
            return novo
        except:
            db.rollback()

    def get_by_id(self, db: Session, id: int):
        return db.query(Person).filter(Person.id == id).first()

    def get_all(self, db: Session, id: int):
        return db.query(Person).all()

    def update(self, db: Session, person: Person, PersonModel: PersonCreate):
        try:
            person.first_name = PersonModel.first_name
            person.last_name = PersonModel.last_name
            db.commit()
            db.refresh(person)
        except:
            db.rollback()

    def delete(self, db: Session, person: Person):
        try:
            db.delete(person)
            db.commit()
            db.refresh(person)
        except:
            db.rollback()



