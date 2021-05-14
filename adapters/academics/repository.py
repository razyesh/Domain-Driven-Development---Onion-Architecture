import abc
import uuid
from domain.academics.model import Section, Grade, Class


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, id_):
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, model):
        raise NotImplementedError


class SectionRepository(AbstractRepository):
    def list(self) -> Section:
        return Section

    def get(self, id_):
        sections = []
        for section in sections:
            if section["id"] == id_:
                return section
        return "Not Found"

    def add(self, model: Section):
        data = {"id_": model.id_, "name": model.name, "school": model.school}
        with open("section.json", "a+") as f:
            f.write(f"{data}\n")


class GradeRepository(AbstractRepository):
    def list(self) -> Grade:
        return Grade

    def get(self, id_):
        grades = []
        for grade in grades:
            if grade["id"] == id_:
                return grade
        return "Not Found"

    def add(self, model: Section):
        data = {"id_": model.id_, "name": model.name, "school": model.school}
        with open("grade.json", "a+") as f:
            f.write(f"{data}\n")


class ClassRepository(AbstractRepository):
    def list(self) -> Class:
        return Class

    def get(self, id_):
        classes = []
        for academic_class in classes:
            if academic_class["id"] == id_:
                return academic_class
        return "Not Found"

    def add(self, model: Class):
        data = {
            "id_": model.id_,
            "sections": model.sections,
            "grade": model.grade,
            "school": model.school,
        }
        with open("class.json", "a+") as f:
            f.write(f"{data}\n")

    def update(self, model: Class):
        data = {
            "id_": model.id_,
            "sections": model.sections,
            "grade": model.grade,
            "school": model.school,
        }
        with open("class.json", "a+") as f:
            f.write(f"{data}\n")
        return True
