import random
from pokemon_base import PokemonBase

class GlitchMon(PokemonBase):

    def __init__(self, hp: int, poke_type: str):
        PokemonBase.__init__(self, hp, poke_type)

    def increaseHp(self, amount: int):
        increase = self.get_hp() + amount
        self.set_hp(increase)

    # TODO: discuss with team about putting increase level in superpower method
    def increaseLvl(self, amount: int):
        increase = self.get_level + amount
        self.set_level(increase)

    def superpower(self):
        num = random.randint(0, 2)
        if num == 0:
            self.increaseLvl(1)

        elif num == 1:
            self.increaseHp(1)

        else:
            self.increaseLvl(1)
            self.increaseHp(1)
