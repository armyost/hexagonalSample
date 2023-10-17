class Department:

    def __init__(self, deptId, description, deptName):
        self.deptId = deptId
        self.description = description
        self.deptName = deptName

    def __repr__(self):
        return f'<Department {self.deptId}>'

    def as_dict(self):
        return {
            'deptId': self.deptId,
            'description': self.description,
            'deptName': self.deptName
        }