from sqlalchemy.orm import Session, joinedload
from database.database import Person
from handle.Person.models import PersonCreate


class PersonServices:

    def add(self, db: Session, person_data: PersonCreate):
        print("-")
        novo = Person(
            first_name=person_data.first_name,
            last_name=person_data.last_name)
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo


    def get_by_id(self, db: Session, id: int):
        return db.query(Person).filter(Person.id == id).first()

    def get_all(self, db: Session):
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


person_service = PersonServices()
