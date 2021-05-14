from domain.academics.model import Class, Grade
from service_layer.academics import abstract
from service_layer.academics import handler
from domain.academics import command
from adapters.academics.repository import (
    ClassRepository,
    GradeRepository,
    SectionRepository,
)
import uuid


def add_section(validated_data: abstract.AddSection) -> None:
    """
    takes validated_date from abstract and add the section domain model to Section repo
    """
    section = handler.add_section(
        command.AddSection(name=validated_data.name, school=validated_data.school)
    )
    repo = SectionRepository()
    repo.add(section)


def add_grade(validated_data: abstract.AddGrade) -> None:
    grade = handler.add_section(
        command.AddGrade(name=validated_data.name, school=validated_data.school)
    )
    repo = GradeRepository()
    repo.add(grade)


def add_class(validated_data: abstract.AddClass) -> None:
    academic_class = handler.add_class(
        command.AddClass(
            grade=validated_data.grade,
            sections=validated_data.sections,
            school=validated_data.school,
        )
    )
    repo = ClassRepository()
    repo.add(academic_class)


def update_class_section(
    id_: uuid.UUID, validated_data: abstract.UpdateClassSection
) -> None:
    repo = ClassRepository()
    class_ = repo.get(id_)
    class_ = handler.update_class_section(
        cmd=command.UpdateClassSection(model=class_, sections=validated_data.sections)
    )
    repo.update(class_)
