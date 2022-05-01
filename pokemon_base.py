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

""" Base class for Glitch Mon

Defines an abstract class that inherits another generic abstract class, PokemonBase
to create a glitch mon.
"""
__author__ = "Thomas Cameron, Neth Botheju"
__docformat__ = 'reStructuredText'

class PokemonBase(ABC, Generic[T]):
    """ abstract base class to create Pokemon and their associated methods """
    def __init__(self, hp: int, poke_type: str) -> None:
        """ Uses Pokemon's hp and type to instantise itself
        :complexity: O(length) for best/worst case to initialise to None
        :param: hp: the health points of the pokemon being created
        :param: poke_type: the type of the pokemon being created
        :pre: hp < 0
        """
        if hp < 0:
            raise Exception("hp must be greater than 0")
        self.hp = hp
        self.poke_type = poke_type
        self.level = 1

    def get_hp(self) -> int:
        """ Gets the pokemon's HP
        :return: the HP integer """
        return self.hp

    def get_level(self) -> int:
        """ Gets the pokemon's level
        :return: the level integer """
        return self.level

    def level_up(self) -> int:
        """ increments the pokemon's level by 1 """
        self.level = self.level + 1

    def set_hp(self, hp: int) -> None:
        """ sets the Pokémon's HP to any value
        :param: hp: the value for the Hp """
        self.hp = int(hp)

    def set_level(self, level: int) -> None:
        """ sets the Pokémon's level to any value
        :param: level: the value for the level """
        self.level = level

    @abstractmethod
    def get_name(self) -> str:
        """ gets the name of the pokemon """
        pass

    @abstractmethod
    def get_speed(self) -> int:
        """ gets the speed of the pokemon """
        pass

    @abstractmethod
    def get_attack(self) -> int:
        """ gets the attack value of the pokemon """
        pass

    def get_poke_type(self) -> str:
        """ gets the type of the pokemon """
        return self.poke_type

    def get_criterion(self, criterion: str) -> int:
        """
        :pre: criterion is one of lvl, hp, attack, defence, speed. Checked in Battle.optimised_mode_battle
        :param criterion: string containing one of Level, HP, Attack, Defence, Speed
        :return: relevant criterion from Pokemon object
        """
        if criterion == "lvl":
            return self.level
        elif criterion == "hp":
            return self.hp
        elif criterion == "attack":
            return self.attack
        elif criterion == "defence":
            return self.defence
        elif criterion == "speed":
            return self.speed
        else:
            raise Exception("Invalid criterion")

    @abstractmethod
    def calculate_damage_taken(self, other: T) -> int:
        """ calculates the damage inflicted by the opponent
        :param: other: the opponent"""
        pass

    def got_hurt_by(self, other_pokemon: T) -> None:
        """ calculates the HP after the pokemon has sustained damage
        :param: other_pokemon: the opponent"""
        self.set_hp(self.hp - self.calculate_damage_taken(other_pokemon))

    def __str__(self) -> str:
        """  Magic method constructing a string representation the pokemon's name, HP and level """
        name = self.get_name()
        return name + "'s HP = " + str(self.hp) + " and level = " + str(self.level)
