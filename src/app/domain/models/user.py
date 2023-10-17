class User:

    def __init__(self, userId, description, userName, deptId):
        self.userId = userId
        self.description = description
        self.userName = userName
        self.deptId = deptId

    def __repr__(self):
        return f'<User {self.userId}>'

    def as_dict(self):
        return {
            'userId': self.userId,
            'description': self.description,
            'userName': self.userName,
            'deptId': self.deptId
        }