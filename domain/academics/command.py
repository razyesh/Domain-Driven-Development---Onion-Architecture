from pydantic import BaseModel
from typing import Set
from domain.academics.model import Class
import uuid
#fix import


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


class ClassCommand(BaseModel):
    model: Class


class UpdateClassSection(ClassCommand):
    sections: Set[uuid.UUID]
