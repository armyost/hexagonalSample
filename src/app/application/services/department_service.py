from domain.models import Department

class DepartmentService:

    def addDepartment(deptId, description, deptName, repository):
        department = Department(
            deptId = deptId,
            description = description,
            deptName = deptName
        )
        repository.insert(department)

        return {
            'deptId': department.deptId,
            'description': department.description,
            'deptName': department.deptName
        }