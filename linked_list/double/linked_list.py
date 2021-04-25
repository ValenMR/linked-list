from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Any, Type, TypeVar, Tuple, NoReturn

from pydantic import validate_arguments

from .node import BaseNode, Node

TypeBaseLinkedList = TypeVar("BaseLinkedList")


class BaseLinkedList(ABC):
    @abstractmethod
    def __init__(self, *args: BaseNode) -> NoReturn:
        raise NotImplementedError

    @property
    @abstractmethod
    def head(self) -> BaseNode:
        raise NotImplementedError

    @head.setter
    @abstractmethod
    def head(self, new_head: BaseNode) -> NoReturn:
        raise NotImplementedError

    def __get_lengths(self, *, other: TypeBaseLinkedList) -> Tuple[int, int]:
        raise NotImplementedError

    @abstractmethod
    def append(self, *, new_node: BaseNode) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    def insert(self, *, index: int, new_node: BaseNode) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    def index(self, *, value: Any) -> int:
        raise NotImplementedError

    @abstractmethod
    def pop(self) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    def __lt__(self, other: TypeBaseLinkedList) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other: TypeBaseLinkedList) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __gt__(self, other: TypeBaseLinkedList) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __le__(self, other: TypeBaseLinkedList) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __ge__(self, other: TypeBaseLinkedList) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __contains__(self, value: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __add__(self, other: Any) -> TypeBaseLinkedList:
        raise NotImplementedError

    @abstractmethod
    def __iadd__(self, other: Any) -> TypeBaseLinkedList:
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError


class LinkedList(BaseLinkedList):
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, *args: Node) -> NoReturn:
        self.__head = None
        [self.append(new_node=new_node) for new_node in args]

    @property
    def head(self) -> Node:
        return self.__head

    @head.setter
    def head(self, new_head: Node) -> NoReturn:
        if isinstance(new_head, Node) or not new_head:
            self.__head = new_head
        raise ValueError("The list can store only one node or null in its head")

    def __get_lengths(self, *, other: Type[BaseLinkedList]) -> Tuple[int, int]:
        return len(other), len(self)

    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def append(self, *, new_node: Node) -> NoReturn:
        if not self.__head:
            self.__head = new_node
        elif not self.__head.link_next:
            self.__head.link_next = new_node
        else:
            current_node = self.__head
            while current_node.link_next:
                current_node = current_node.link_next
            new_node.link_above = current_node
            current_node.link_next = new_node

    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def insert(self, *, index: int, new_node: Node) -> NoReturn:
        if index > 0:
            current_node = self.__head

            for _ in range(index - 1):
                if not current_node.link_next:
                    raise IndexError("The index goes out of range of the list")
                current_node = current_node.link_next
            if not current_node.link_next:
                current_node.link_next = new_node
                new_node.link_above = current_node
            else:
                new_node.link_next = current_node.link_next
                current_node.link_next.link_above = new_node
                current_node.link_next = new_node
                new_node.link_above = current_node.link_next
        elif index < 0:
            raise IndexError("Negative index is not allowed")
        else:
            new_node.link_next = self.__head
            self.__head.link_above = new_node
            self.__head = new_node

    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def index(self, *, value: Any) -> int:
        index = 0
        current_node = self.__head
        while True:
            if current_node and current_node.value == value:
                break
            elif not current_node or current_node.link_next is None:
                index = -1
                break
            current_node = current_node.link_next
            index += 1
        return index

    def pop(self) -> NoReturn:
        if self.__head:
            current_node = self.__head
            previous_node = None

            while current_node.link_next is not None:
                previous_node = current_node
                current_node = current_node.link_next

            if previous_node:
                previous_node.link_next = None
                del current_node
            else:
                self.__head = None
        else:
            raise ValueError("No nodes to remove")

    def clear(self) -> NoReturn:
        current_node = self.__head
        while current_node is not None:
            aux_node = current_node # NOQA
            current_node = current_node.link_next
            del aux_node

        self.__head = None

    def __lt__(self, other: Type[BaseLinkedList]) -> bool:
        other_name = other.__class__.__name__
        self_name = self.__class__.__name__
        if other_name == self_name:
            lenght_other, lenght_current = self.__get_lengths(other=other)
            return lenght_current < lenght_other
        else:
            raise TypeError(
                f"'<' not supported between instances of '{other_name}' and '{self_name}'"
            )

    def __eq__(self, other: Type[BaseLinkedList]) -> bool:
        other_name = other.__class__.__name__
        self_name = self.__class__.__name__
        if other_name == self_name:
            lenght_other, lenght_current = self.__get_lengths(other=other)
            return lenght_current == lenght_other
        else:
            raise TypeError(
                f"'==' not supported between instances of '{other_name}' and '{self_name}'"
            )

    def __gt__(self, other: Type[BaseLinkedList]) -> bool:
        other_name = other.__class__.__name__
        self_name = self.__class__.__name__
        if other_name == self_name:
            lenght_other, lenght_current = self.__get_lengths(other=other)
            return lenght_current > lenght_other
        else:
            raise TypeError(
                f"'>' not supported between instances of '{other_name}' and '{self_name}'"
            )

    def __le__(self, other: Type[BaseLinkedList]) -> bool:
        other_name = other.__class__.__name__
        self_name = self.__class__.__name__
        if other_name == self_name:
            lenght_other, lenght_current = self.__get_lengths(other=other)
            return lenght_current <= lenght_other
        else:
            raise TypeError(
                f"'<=' not supported between instances of '{other_name}' and '{self_name}'"
            )

    def __ge__(self, other: Type[BaseLinkedList]) -> bool:
        other_name = other.__class__.__name__
        self_name = self.__class__.__name__
        if other_name == self_name:
            lenght_other, lenght_current = self.__get_lengths(other=other)
            return lenght_current >= lenght_other
        else:
            raise TypeError(
                f"'>=' not supported between instances of '{other_name}' and '{self_name}'"
            )

    def __contains__(self, value: Any) -> bool:
        index = self.index(value=value)
        if index == -1:
            return False
        return True

    def __add__(self, other: Any) -> Type[BaseLinkedList]:
        linked_list_temporal = deepcopy(self)
        if other.__class__.__name__ == self.__class__.__name__:
            current_node = linked_list_temporal.__head
            while current_node.link_next is not None:
                current_node = current_node.link_next
            current_node.link_next = other.head
            other.head.link_above = current_node
        else:
            node = Node(value=other)
            linked_list_temporal.append(new_node=node)
        return linked_list_temporal

    def __iadd__(self, other: Any) -> Type[BaseLinkedList]:
        if other.__class__.__name__ == self.__class__.__name__:
            current_node = self.__head
            while current_node.link_next is not None:
                current_node = current_node.link_next
            current_node.link_next = other.head
            other.head.link_above = current_node
        else:
            node = Node(value=other)
            self.append(new_node=node)
        return self

    def __len__(self) -> int:
        count = 0
        current_node = self.__head
        while current_node is not None:
            current_node = current_node.link_next
            count += 1
        return count

    def __str__(self) -> str:
        message = "Head -> "
        current = self.__head

        while current is not None:
            message += f"[{str(current)}]"
            current = current.link_next

            if current:
                message += " <-> "

            current = current
        return message
