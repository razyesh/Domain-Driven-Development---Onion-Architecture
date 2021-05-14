"""
#command handler
handlers takes command as argument, and performs what the command aims to do

"""

from domain.academics import command
from domain.academics import model


def add_section(cmd: command.AddSection) -> model.Section:
    return model.section_factory(name=cmd.name, school=cmd.school)


def add_grade(cmd: command.AddGrade) -> model.Grade:
    return model.grade_factory(name=cmd.name, school=cmd.school)


def add_class(cmd: command.AddClass) -> model.Class:
    return model.class_factory(
        grade=cmd.grade, sections=cmd.sections, school=cmd.school
    )


def update_class_section(cmd: command.UpdateClassSection) -> model.Class:
    print("called")
    return cmd.model.update_sections(cmd.sections)  # update_sections
