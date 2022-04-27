"""Notes:
Needs 'from abc import ABC, abstractmethod' see - week 6 content
for abstract base classes.
Probably also needs import TypeVAR, Generic for runtime type hints
and generic class types? Unsure, bit shaky on these concepts

So opening is imports, T = TypeVar('T') etc, then
class PokemonBase(ABC, Generic[T]) <- still have no real idea what generic does
then def __init__(self, int: hp, ???: poke_type): (what datatype is poke_type?)
etc

NOTES from assignemnt specs to follow:
Preconditions must be checked in abstract methods if possible.
The docstring for each method must contain best and worst-case complexity.
We must add at least 1 unit test for each method in a file named
test_pokemon_base.py, NOT adding to task1_tester.py (though won't be penalised
if we do)"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class PokemonBase(ABC, Generic[T]):
    def __init__(self, hp: int, poke_type: str) -> None:
        if hp < 0:
            raise Exception("hp must be greater than 0")
        self.hp = hp
        self.poke_type = poke_type
        self.level = 1

    def get_hp(self) -> int:
        return self.hp

    def get_level(self) -> int:
        return self.level

    def level_up(self) -> int:
        self.level = self.level + 1

    def set_hp(self, hp: int) -> None:
        self.hp = hp

    def set_level(self, level: int) -> None:
        self.level = level

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_speed(self) -> int:
        pass

    @abstractmethod
    def get_attack(self) -> int:
        pass

    def get_poke_type(self) -> str:
        return self.poke_type

    @abstractmethod
    def calculate_damage_taken(self, other: T) -> int:
        pass

    def __str__(self) -> str:
        name = self.get_name()
        return name + "'s HP = " + str(self.hp) + " and level = " + str(self.level)
