from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

Base = declarative_base()

squad_person_association = Table(
   'squad_person', Base.metadata,
   Column('squad_id', Integer, ForeignKey('squad.id', ondelete="CASCADE"), primary_key=True),
   Column('person_id', Integer, ForeignKey('person.id', ondelete="CASCADE"), primary_key=True)
)

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True,)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    task_points = Column(Integer, default=0, nullable=True)
    meet_points = Column(Integer,default=0, nullable=True)
    squad = relationship("Squad", secondary=squad_person_association, back_populates="members"  )

    created_at = Column(
        DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

class Squad(Base):
    __tablename__ = 'squad'
    id = Column(Integer, primary_key=True)
    squad_name = Column(String(30), nullable=False)
    squad_points = Column(Integer, default=0, nullable=True)
    members = relationship("Person", secondary=squad_person_association, back_populates="squad")

    created_at = Column(
        DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
