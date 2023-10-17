from abc import (
    ABCMeta,
    abstractmethod
)

class UserRepositoryInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, user):
        pass

    @abstractmethod
    def selectWithDeptInfo(self, userId):
        pass

    