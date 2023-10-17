from abc import (
    ABCMeta,
    abstractmethod
)

class DepartmentRepositoryInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, department):
        pass