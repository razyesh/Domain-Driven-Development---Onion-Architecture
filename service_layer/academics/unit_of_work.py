from abc import ABC, abstractmethod
from adapters.academics import repository


class AbstractUnitOfWork(ABC):
    repos: repository.AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class ClassUnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        self.model = repository.ClassRepository()
        self.committed = False

    def __enter__(self):
        self.model = repository.ClassRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.close()

    def commit(self):
        self.committed = True

    def rollback(self):
        pass
