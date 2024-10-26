from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    task_points = Column(Integer, nullable=False)
    meet_points = Column(Integer, nullable=False)
    squad_id = Column(Integer, ForeignKey('squad.id'), nullable=False)

    squad = relationship("Squad")

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
    squad_points = Column(Integer, nullable=False)

    people = relationship("Person", back_populates="squad")

    created_at = Column(
        DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
