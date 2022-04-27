"""
    SortedList ADT and an aray implementation.

    Defines a generic abstract sorted list with the standard methods, and
    implements a sorted list using arrays and Insertion sort.
    Items to store should be of type ListItem.

    TODO: CHANGE NOTE BELOW
    note to team: Insertion sort picked for stability and incrementability to
    support MissingNo, and since it uses Insertion which is a method setup
    in the abstract class, it seems appropriate.
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from referential_array import ArrayR
T = TypeVar('T')
K = TypeVar('K')

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev and Thomas Cameron'
__docformat__ = 'reStructuredText'

class ListItem(Generic[T, K]):
    """ Items to be stored in a list, including the value and the key used for sorting. """
    def __init__(self, value: T, key: int):
        self.value = value
        self.key = key

    def __str__(self) -> str:
        return '({0}, {1})'.format(self.value, self.key)

    def get_value(self) -> T:
        return self.value

    def get_key(self) -> int:
        return self.key


class SortedList(ABC, Generic[T]):
    """ Abstract class for a generic SortedList. """
    def __init__(self) -> None:
        """ Basic SortedList object initialiser. """
        self.length = 0

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        pass

    @abstractmethod
    def __setitem__(self, index: int, item: ListItem) -> None:
        """ Magic method. Insert the item at a given position,
            if possible (!). Shift the following elements to the right.
        """
        pass

    def __len__(self) -> int:
        """ Return the size of the list. """
        return self.length

    def __str__(self) -> str:
        """ Magic method constructing a string representation of the list object. """
        result = '['
        for i in range(len(self)):
            if i > 0:
                result += ', '
            result += str(self[i]) if type(self[i]) != str else "'{0}'".format(self[i])
        result += ']'
        return result

    @abstractmethod
    def delete_at_index(self, index: int) -> ListItem:
        """ Delete item at a given position. """
        pass

    @abstractmethod
    def index(self, item: ListItem) -> int:
        """ Find the position of a given item in the list. """
        pass

    def remove(self, item: T) -> None:
        """ Remove an item from the list. """
        index = self.index(item)
        self.delete_at_index(index)

    def is_empty(self) -> bool:
        """ Check if the list of empty. """
        return len(self) == 0

    def clear(self) -> None:
        """ Clear the list. """
        self.length = 0

    @abstractmethod
    def add(self, item: ListItem) -> None:
        """ Add new element to the list. """
        pass


class ArraySortedList(SortedList[T]):
    """ Implementation of a sorted list with arrays.
        Note that the key of key-value pairs in the list
        is based on the criterion defined when constructing the list

    Attributes:
        length (int): number of elements in the list (inherited)
        array (ArrayR[T]): array storing the elements of the list

    ArrayR cannot create empty arrays. So MIN_CAPACITY is used to avoid this.
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """Inititalises the length and the array with the given capacity.
            If max_capacity is 0, the array is created with MIN_CAPACITY.
        """
        SortedList.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position.
            :raises Exception: if index is outside of bounds
         """
        try:
            return self.array[index]
        except Exception as e:
            print(e)

    def __setitem__(self, index: int, item: ListItem) -> None:
        """ Magic method. Insert the item at a given position,
            if possible (!). Shift the folllowing elements to the right.
            :pre: list is not full
            :raises Exception: if index is outside of bounds, if list is full
            """
        if self.is_full():
            raise Exception("List is full")
        try:
            mark = max(len(self) - 1, 0)  # stores index of final element in list. Max is used for case when list is empty
            while True:
                self.array[mark + 1] = self.array[mark]
                if mark == index:
                    self.array[mark] = item
                    break
                else:
                    mark -= 1
            self.length += 1
        except Exception as e:
            print(e)

    def delete_at_index(self, index: int) -> ListItem:
        """ Delete item at a given position. Shift the following elements
            to the left.
            :pre: list is not empty
            :raises Exception: if index is out of bounds or list is not empty
            :return: Item deleted
            """
        if self.is_empty():
            raise Exception("List is empty")
        try:
            temp = self.array[index]
            for mark in range(index, len(self) - 1):
                self.array[mark] = self.array[mark + 1]
            self.length -= 1
            return temp
        except Exception as e:
            print(e)

    def index(self, item: ListItem) -> int:
        """ Find the position of a given item in the List.
            :raises Exception: if item is not in the List
        """
        for index in range(0, len(self)):
            if self.array[index] == item:
                return index

        raise Exception("Item is not in the List")  # Only reached if item not found in List

    def add(self, item: ListItem) -> None:
        """ Add new element to the List.
            :pre: List is not full
            :raises Exception: if List is full
        """
        if self.is_full():
            raise Exception("List is full")
        else:
            self.array[len(self)] = item
            self.length += 1

    def is_full(self) -> bool:
        """ True if the list is full and no element can be inserted"""
        return len(self) == len(self.array)

    def sort(self) -> None:
        """ Sorts the list by key in non-increasing order.
            Algorithm used: Insertion sort
        """
        n = self.length
        for mark in range(1,n):
            temp = self.array[mark]
            i = mark - 1
            while i >= 0 and self.array[i].get_key() < temp.get_key():
                self.array[i+1] = self.array[i]
                i -= 1
            self.array[i+1] = temp



if __name__ == "__main__":
    from poke_team import PokeTeam
    team = PokeTeam("Ash")
    team.choose_team()
    print(team)

    s_list = ArraySortedList(len(team) + 1)
    for _ in range(len(team)):
        p = team.pop()
        item = ListItem(p, p.get_hp())
        s_list.add(item)
    print(s_list)
    print("\nTesting error cases:")
    potato = ListItem("Potato", 3)
    s_list.add(potato)
    print(s_list)
    print(f"List length: {len(s_list)} after adding an item")
    s_list.delete_at_index(1)
    print(s_list)
    print(f"List length: {len(s_list)} after deleting an item at index 1")
    s_list[2] = ListItem("AAAAAAAAAAAAAAAAAA", 3)
    print(s_list)
    print(f"List length: {len(s_list)} after setting an item at index 2")
    s_list.sort()
    print(s_list)
    print(f"List length: {len(s_list)} after sorting")
    s_list.remove(potato)
    print(s_list)
    print(f"List length: {len(s_list)} after removing potato")

