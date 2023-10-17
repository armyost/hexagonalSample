from domain.repositories import DepartmentRepositoryInterface
from infrastructure.database import departments_table
from infrastructure.repositories import BaseRepository


class DepartmentRepository(BaseRepository, DepartmentRepositoryInterface):

    def insert(self, department):
        with self.db_connection.begin():
            self.db_connection.execute(
                departments_table.insert(),
                department.as_dict()
            )
