"""
Class that inherits PokemonBase class which allows to instantise each pokemon
with their respective attributes
"""
from pokemon_base import PokemonBase

class Charmander(PokemonBase):
    def __init__(self):
        """ Initialises Charmander using its HP and type
        :complexity: O(1)"""
        PokemonBase.__init__(self, 7, 'Fire')
        self.name = 'Charmander'
        self.attack = 6 + self.level
        self.defence = 4
        self.speed = 7 + self.level

    def get_name(self) -> str:
        """ Gets Charmander's name
        return: the name string
        :complexity: O(1)"""
        return self.name

    def get_attack(self) -> int:
        """ gets the attack value of Charmander which depends on its level
        return: attack integer
        :complexity: O(1)"""
        self.attack = 6 + self.level
        return self.attack

    def get_defence(self) -> int:
        """ gets the defence value of Charmander
        :return: defence integer
        :complexity: O(1) """
        self.defence = 4
        return self.defence

    def get_speed(self) -> int:
        """ gets the speed value of Charmander
        :return: speed integer
        :complexity: O(1) """
        self.speed = 7 + self.level
        return self.speed

    def calculate_damage_taken(self, opponent: PokemonBase) -> int:
        """ checks the type the opponent attacking and multiplies it by the effectiveness multiplier
        :raises Exception: if the opponent's type is not of the ones listed in the checking statements
        :return: the damage integer caused by the opponent
        :complexity: O(1) """
        if opponent.get_poke_type() == "Fire":
            effective_damage = opponent.get_attack()
        elif opponent.get_poke_type() == "Water":
            effective_damage = opponent.get_attack() * 2
        elif opponent.get_poke_type() == "Grass":
            effective_damage = opponent.get_attack() * 0.5
        elif opponent.get_poke_type() == "Unknown":
            effective_damage = opponent.get_attack()
        else:
            raise Exception("Attacker type is not Fire, Water or Grass or Unknown")

        if effective_damage > self.get_defence():
            return effective_damage
        else:
            return effective_damage // 2


class Bulbasaur(PokemonBase):
    def __init__(self):
        """ Initialises Bulbasaur using its HP and type
        :complexity: O(1)"""
        PokemonBase.__init__(self, 9, 'Grass')
        self.name = 'Bulbasaur'
        self.attack = 5
        self.defence = 5
        self.speed = 7

    def get_name(self) -> str:
        """ Gets Bulbasaur's name
        return: the name string
        :complexity: O(1) """
        return self.name

    def get_attack(self) -> int:
        """ gets the attack value of Bulbasur which depends on its level
        return: attack integer
        :complexity: O(1) """
        return self.attack

    def get_defence(self) -> int:
        """ gets the defence value of Bulbasaur
        return: defence integer
        :complexity: O(1) """
        self.defence = 5
        return self.defence

    def get_speed(self) -> int:
        """ gets the speed value of Bulbasaur
        return: speed integer
        :complexity: O(1) """
        return self.speed + self.level // 2


    def calculate_damage_taken(self, opponent: PokemonBase) -> int:
        """ checks the type the opponent attacking and multiplies it by the effectiveness multiplier
        :raises Exception: if the opponent's type is not of the ones listed in the checking statements
        return: the damage integer caused by the opponent
        :complexity: O(1) """
        if opponent.get_poke_type() == "Fire":
            effective_damage = opponent.get_attack() * 2
        elif opponent.get_poke_type() == "Water":
            effective_damage = opponent.get_attack() * 0.5
        elif opponent.get_poke_type() == "Grass":
            effective_damage = opponent.get_attack()
        elif opponent.get_poke_type() == "Unknown":
            effective_damage = opponent.get_attack()
        else:
            raise Exception("Attacker type is not Fire, Water or Grass or Unknown")

        if effective_damage > self.get_defence() + 5:
            return effective_damage
        else:
            return effective_damage // 2


class Squirtle(PokemonBase):
    def __init__(self):
        """ Initialises Squirtle using its HP and type
        :complexity: O(1)"""
        PokemonBase.__init__(self, 8, 'Water')
        self.name = 'Squirtle'
        self.attack = 4
        self.defence = 6
        self.speed = 7

    def get_name(self) -> str:
        """ Gets Squirtle's name
        return: the name string
        :complexity: O(1) """
        return self.name

    def get_attack(self) -> int:
        """ gets the attack value of Squirtle which depends on its level
        return: attack integer
        :complexity: O(1) """
        return self.attack + (self.level // 2)

    def get_defence(self) -> int:
        """ gets the defence value of Squirtle
        return: defence integer
        :complexity: O(1) """
        return self.defence + self.level

    def get_speed(self) -> int:
        """ gets the speed value of Squirtle
        return: speed integer
        :complexity: O(1) """
        return self.speed

    def calculate_damage_taken(self, opponent: PokemonBase) -> int:
        """ checks the type the opponent attacking and multiplies it by the effectiveness multiplier
        :raises Exception: if the opponent's type is not of the ones listed in the checking statements
        return: the damage integer caused by the opponent
        :complexity: O(1)"""
        if opponent.get_poke_type() == 'Fire':
            # 0.5 is the effect multiplier.
            effective_damage = opponent.get_attack() * 0.5
        elif opponent.get_poke_type() == 'Water':
            effective_damage = opponent.get_attack()
        elif opponent.get_poke_type() == 'Grass':
            # 2 is the effect multiplier.
            effective_damage = opponent.get_attack() * 2
        elif opponent.get_poke_type() == "Unknown":
            effective_damage = opponent.get_attack()
        else:
            raise Exception("Attacker type is not Fire, Water or Grass or Unknown")

        if effective_damage > self.get_defence() * 2:
            return effective_damage
        else:
            return effective_damage // 2


