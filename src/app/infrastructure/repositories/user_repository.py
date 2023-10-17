from domain.repositories import UserRepositoryInterface
from infrastructure.database import (users_table, departments_table)
from infrastructure.repositories import BaseRepository

from sqlalchemy import select

class UserRepository(BaseRepository, UserRepositoryInterface):

    def insert(self, user):
        with self.db_connection.begin():
            self.db_connection.execute(
                users_table.insert(),
                user.as_dict()
            )

    def selectWithDeptInfo(self, userId):
        with self.db_connection.begin():
            stmt = select(users_table, departments_table).outerjoin(departments_table, users_table.c.deptId == departments_table.c.deptId).where(users_table.c.userId == userId)
            row = self.db_connection.execute(stmt).fetchone()
            return {
                'userId' : row['userId'],
                'userName' : row['userName'],
                'deptName' : row['deptName']
            } if row else None