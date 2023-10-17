import logging
from domain.models import User

class UserService:

    def addUser(id, description, userName, deptId, repository):
        user = User(
            userId = id,
            description = description,
            userName = userName,
            deptId = deptId
        )
        repository.insert(user)

        return {
            'userId': user.userId,
            'description': user.description,
            'userName': user.userName,
            'deptId': user.deptId
        }

    def detailUser(userId, repository):
        userDetailInfo = repository.selectWithDeptInfo(userId)
        logging.warn("!!! userDetailInfo : !!!" + str(userDetailInfo))
        return userDetailInfo