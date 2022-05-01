from glitch_mon import GlitchMon
from pokemon import Charmander, Bulbasaur, Squirtle
from pokemon_base import PokemonBase

""" Class for Missing No pokemon

A class that inherhits GlitchMon base class which 
allows to instantiate the Missing No
"""
__author__ = "Neth Botheju"
__docformat__ = 'reStructuredText'

class MissingNo(GlitchMon):
    """ Class that defines Missing No pokemon and all its methods """
    def __init__(self):
        averageHp = int((Charmander().get_hp() + Bulbasaur().get_hp() + Squirtle().get_hp()) / 3)
        GlitchMon.__init__(self, averageHp, "Unknown")
        self.name = 'MissingNo'
        self.attack = int((Charmander().get_hp() + Bulbasaur().get_hp() + Squirtle().get_hp()) / 3)
        self.defence = int((Charmander().get_hp() + Bulbasaur().get_hp() + Squirtle().get_hp()) / 3)
        self.speed = int((Charmander().get_hp() + Bulbasaur().get_hp() + Squirtle().get_hp()) / 3)

    def increaseHp(self) -> int:
        """ Increases the pokemon's HP by one increment """
        self.set_hp(self.get_hp() + 1)

    def get_name(self) -> str:
        """ gets the pokemon's name

         return: string of name"""
        return self.name

    def get_attack(self) -> int:
        """ gets the attack value of the Pokemon
        depending on its level. It increases depending
        on the level of the pokemon

        return: integer of the attack value"""
        return self.attack + (self.level - 1)

    def get_defence(self) -> int:
        """ gets the defence value of the Pokemon
        depending on its level. It increases depending
        on the level of the pokemon

        return: integer of the defence value"""
        return self.defence + (self.level - 1)

    def get_speed(self) -> int:
        """ gets the speed value of the Pokemon
        depending on its level. It increases depending
        on the level of the pokemon

        return: integer of the speed value"""
        return self.speed + (self.level - 1)

    def calculate_damage_taken(self, opponent: PokemonBase) -> int:
        """ calculates the damage sustained by the pokemon.

        :param opponent: which other pokemon it is fighting against
        return: integer of the damage taken value"""
        effective_damage = opponent.get_attack() * 1
        if effective_damage > self.get_defence():
            return effective_damage
        else:
            return effective_damage // 2

if __name__ == "__main__":
    charm = Charmander()
    print(MissingNo())