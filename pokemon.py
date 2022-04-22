"""
Each of these classes inherits PokemonBase, so needs line
from pokemon_base import PokemonBase, T <- just going off wk6 example
Each class has to also init PokemonBase, so init looks like:
def __init__(self, etc) -> None:
    PokemonBase.__init__(self, etcetc)
"""
from typing import TypeVar, Generic
from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    def __init__(self):
        PokemonBase.__init__(self, 7, 'Fire')
        self.name = 'Charmander'
        self.attack = 6 + self.level
        self.defence = 4
        self.speed = 7 + self.level

    def get_name(self) -> str:
        return self.name

    def get_attack(self) -> int:
        self.attack = 6 + self.level
        return self.attack

    def get_defence(self) -> int:
        self.defence = 4
        return self.defence

    def get_speed(self) -> int:
        self.speed = 7 + self.level
        return self.speed

    def calculate_damage_taken(self, opponent: PokemonBase) -> int:
        if opponent.get_poke_type() == "Fire":
            effective_damage = opponent.get_attack()
        elif opponent.get_poke_type() == "Water":
            effective_damage = opponent.get_attack() * 2
        elif opponent.get_poke_type() == "Grass":
            effective_damage = opponent.get_attack() * 0.5
        else:
            raise Exception("Attacker type is not Fire, Water or Grass")

        if effective_damage > self.get_defence():
            return effective_damage
        else:
            return effective_damage // 2


class Bulbasaur(PokemonBase):
    def __init__(self):
        PokemonBase.__init__(self, 9, 'Grass')
        self.name = 'Bulbasaur'
        self.attack = 5
        self.defence = 5
        self.speed = 7

    def get_name(self) -> str:
        return self.name

    def get_attack(self) -> int:
        return self.attack

    def get_defence(self) -> int:
        self.defence = 5
        return self.defence

    def get_speed(self) -> int:
        return self.speed + self.level // 2

    def calculate_damage_taken(self, opponent: PokemonBase) -> int:
        if opponent.get_poke_type() == "Fire":
            effective_damage = opponent.get_attack() * 2
        elif opponent.get_poke_type() == "Water":
            effective_damage = opponent.get_attack() * 0.5
        elif opponent.get_poke_type() == "Grass":
            effective_damage = opponent.get_attack()
        else:
            raise Exception("Attacker type is not Fire, Water or Grass")

        if effective_damage > self.get_defence() + 5:
            return effective_damage
        else:
            return effective_damage // 2


class Squirtle(PokemonBase):
    def __init__(self):
        PokemonBase.__init__(self, 8, 'Water')
        self.name = 'Squirtle'
        self.attack = 4
        self.defence = 6
        self.speed = 7

    def get_name(self) -> str:
        return self.name

    def get_attack(self) -> int:
        return self.attack + self.level // 2

    def get_defence(self) -> int:
        return self.defence + self.level

    def get_speed(self) -> int:
        return self.speed

    def calculate_damage_taken(self, opponent: PokemonBase) -> int:
        if opponent.get_poke_type() == 'Fire':
            effective_damage = opponent.get_attack() * 0.5
        elif opponent.get_poke_type() == 'Water':
            effective_damage = opponent.get_attack()
        elif opponent.get_poke_type() == 'Grass':
            effective_damage = opponent.get_attack() * 2
        else:
            raise Exception("Attacker type is not of Fire, Water or Grass type")

        if effective_damage > self.get_defence() * 2:
            return effective_damage
        else:
            return effective_damage // 2


if __name__ == '__main__':
    pass