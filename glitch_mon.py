import random
from abc import abstractmethod

from pokemon_base import PokemonBase


class GlitchMon(PokemonBase):
    def __init__(self, hp: int, poke_type: str):
        PokemonBase.__init__(self, hp, poke_type)

    @abstractmethod
    def increaseHp(self) -> int:
        pass

    def superPower(self) -> str:
        num = random.randint(0, 2)
        if num == 0:
            self.level_up()
            output = self.get_name() + " leveled up!"
            return output
            print(output)
        elif num == 1:
            self.increaseHp()
            output = self.get_name() + " increased HP!"
            return output
            print(output)

        else:
            self.level_up()
            self.increaseHp()
            output = self.get_name() + " leveled up and increased HP!"
            return output
            print(output)
