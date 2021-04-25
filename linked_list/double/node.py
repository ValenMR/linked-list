from abc import ABC, abstractmethod
from typing import Any, Type, TypeVar, Optional, NoReturn

TypeBaseNode = TypeVar("BaseNode")


class BaseNode(ABC):
    @abstractmethod
    def __init__(
        self,
        *,
        value: Any,
        link_next: TypeBaseNode = None,
        link_above: TypeBaseNode = None,
    ) -> NoReturn:
        raise NotImplementedError

    @property
    @abstractmethod
    def link_next(self) -> TypeBaseNode:
        raise NotImplementedError

    @link_next.setter
    @abstractmethod
    def link_next(self, link_next: TypeBaseNode) -> NoReturn:
        raise NotImplementedError

    @property
    @abstractmethod
    def link_above(self) -> TypeBaseNode:
        raise NotImplementedError

    @link_above.setter
    @abstractmethod
    def link_above(self, link_above: TypeBaseNode) -> NoReturn:
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
        self,
        *,
        value: Any,
        link_next: Optional[Type[BaseNode]] = None,
        link_above: Optional[Type[BaseNode]] = None,
    ) -> NoReturn:
        self.__value = value
        self.__link_next = link_next
        self.__link_above = link_above

    @property
    def link_next(self) -> TypeBaseNode:
        return self.__link_next

    @link_next.setter
    def link_next(self, link_next: TypeBaseNode) -> NoReturn:
        self.__link_next = link_next

    @property
    def link_above(self) -> TypeBaseNode:
        return self.__link_above

    @link_above.setter
    def link_above(self, link_above: TypeBaseNode) -> NoReturn:
        self.__link_above = link_above

    @property
    def value(self) -> Any:
        return self.__value

    @value.setter
    def value(self, value: Any) -> NoReturn:
        self.__value = value

    def __str__(self) -> str:
        return self.__value.__str__()
