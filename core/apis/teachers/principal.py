from core.apis import decorators
from .schema import TeacherSchema
from core.models.teachers import Teacher
from core.apis.responses import APIResponse
from core.apis.assignments.principal import principle_assignments_resources


@principle_assignments_resources.route('/teacher', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    "Return list of teacher"
    teachers = Teacher.get_teachers()
    teacher_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teacher_dump)