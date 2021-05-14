import uuid
from uuid import UUID
from service_layer.academics import service
from service_layer.academics import abstract

COMMON_SCHOOL = uuid.uuid1()

section = {"name": "A", "school": COMMON_SCHOOL}

grade = {"name": "1", "school": COMMON_SCHOOL}

academic_class = {
    "grade": uuid.uuid1(),
    "sections": [uuid.uuid1()],
    "school": COMMON_SCHOOL,
}


service.add_section(
    validated_data=abstract.AddSection(name=section["name"], school=section["school"])
)

service.add_grade(
    validated_data=abstract.AddGrade(name=grade["name"], school=grade["school"])
)

service.add_class(
    validated_data=abstract.AddClass(
        sections=academic_class["sections"],
        grade=academic_class["grade"],
        school=academic_class["school"],
    )
)

service.update_class_section(
    UUID("873f1126-b393-11eb-9b22-acde48001122"),
    validated_data=abstract.UpdateClassSection(sections=[uuid.uuid1()]),
)
