from dataclasses import dataclass
from pydantic import BaseModel
from typing import List, Set, Dict, Any
import uuid


class Section(BaseModel):
    id_: uuid.UUID
    name: str
    school: uuid.UUID

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "Section"


class Grade(BaseModel):
    id_: uuid.UUID
    name: str
    school: uuid.UUID

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "Grade"


class Class(BaseModel):
    id_: uuid.UUID
    grade: uuid.UUID
    sections: Set[uuid.UUID]
    school: uuid.UUID

    class Config:
        extra = "forbid"
        allow_mutations = False
        title = "Class"

    def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)

    # immutable
    # return copy
    def update_sections(self, sections: Set[uuid.UUID]):
        sections_ = self.sections
        self.sections = sections
        return self.copy()


def section_factory(name: str, school: int) -> Section:
    return Section(id_=uuid.uuid1(), name=name, school=school)


def grade_factory(name: str, school: int) -> Grade:
    return Grade(id_=uuid.uuid1(), name=name, school=school)


def class_factory(grade: int, sections: Set[int], school: int) -> Class:
    return Class(id_=uuid.uuid1(), grade=grade, sections=sections, school=school)
