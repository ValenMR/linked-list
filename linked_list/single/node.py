from abc import ABC, abstractmethod
from typing import Any, Type, TypeVar, Optional, NoReturn

TypeBaseNode = TypeVar("BaseNode")


class BaseNode(ABC):
    @abstractmethod
    def __init__(
        self, *, value: Any, link: Optional[TypeBaseNode] = None
    ) -> NoReturn:
        raise NotImplementedError

    @property
    @abstractmethod
    def link(self) -> TypeBaseNode:
        raise NotImplementedError

    @link.setter
    @abstractmethod
    def link(self, link: TypeBaseNode) -> NoReturn:
        raise NotImplementedError

    @property
    @abstractmethod
    def value(self) -> Any:
        raise NotImplementedError

    @value.setter
    @abstractmethod
    def value(self, value: Any) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError


class Node(BaseNode):
    def __init__(
        self, *, value: Any, link: Optional[Type[BaseNode]] = None
    ) -> NoReturn:
        self.__value = value
        self.__link = link

    @property
    def link(self) -> Type[BaseNode]:
        return self.__link

    @link.setter
    def link(self, link: Type[BaseNode]) -> NoReturn:
        self.__link = link

    @property
    def value(self) -> Any:
        return self.__value

    @value.setter
    def value(self, value: Any) -> NoReturn:
        self.__value = value

    def __str__(self) -> str:
        return self.__value.__str__()
