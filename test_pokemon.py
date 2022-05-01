from pokemon import Charmander, Bulbasaur, Squirtle
import unittest

from pokemon_base import PokemonBase
from tester_base import TesterBase, captured_output

class TestPokemon(TesterBase):

    def test_init(self):
        try:
            charm = Charmander()
            bulb = Bulbasaur()
            squir = Squirtle
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            c = str(charm)
            b = str(bulb)
            s = str(squir)

            if c != "Charmander's HP = 7 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b != "Bulbasaur's HP = 9 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s != "Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")

        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_get_name(self) -> str:
        try:
            c = Charmander().get_name()
            b = Bulbasaur().get_name()
            s = Squirtle().get_name()
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            if c != "Charmander":
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b != "Bulbasaur":
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s != "Squirtle":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_get_attack(self) -> int:
        pass

    def test_get_defence(self) -> int:
        pass

    def test_get_speed(self) -> int:
        pass

    def test_calculate_damage_taken(self, opponent: PokemonBase) -> int:
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)
