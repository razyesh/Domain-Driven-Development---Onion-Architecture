from pydantic import BaseModel
from domain.academics import model
from typing import Set
import uuid


class AddSection(BaseModel):
    name: str
    school: uuid.UUID


class AddGrade(BaseModel):
    name: str
    school: uuid.UUID


class AddClass(BaseModel):
    grade: uuid.UUID
    sections: Set[uuid.UUID]
    school: uuid.UUID


class UpdateClassSection(BaseModel):
    sections: Set[uuid.UUID]
