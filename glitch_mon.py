import random
from abc import abstractmethod

from pokemon_base import PokemonBase

""" Base class for Glitch Mon

Defines an abstract class that inherits another generic abstract class, PokemonBase
to create a glitch mon.
"""
__author__ = "Neth Botheju"
__docformat__ = 'reStructuredText'

class GlitchMon(PokemonBase):
    """ Abstract class for Missing No Pokémon """
    def __init__(self, hp: int, poke_type: str):
        """ initalises the arguments from PokemonBase """
        PokemonBase.__init__(self, hp, poke_type)

    @abstractmethod
    def increaseHp(self) -> int:
        """ abstract method that increases the HP integer
        of the pokemon """
        pass

    def superPower(self) -> str:
        """ uses a random integer generator (25% chance) to
        determine if Glitchmon should level up, increase HP or both

        return: the string that indicates which powerup MissingNo has used
        """
        num = random.randint(0, 2)
        if num == 0:
            self.level_up()
            output = self.get_name() + " leveled up!"
            return output
        elif num == 1:
            self.increaseHp()
            output = self.get_name() + " increased HP!"
            return output

        else:
            self.level_up()
            self.increaseHp()
            output = self.get_name() + " leveled up and increased HP!"
            return output


