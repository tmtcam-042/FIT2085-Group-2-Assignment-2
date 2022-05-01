from pokemon import Charmander, Bulbasaur, Squirtle
import unittest

from pokemon_base import PokemonBase
from tester_base import TesterBase, captured_output

class TestPokemon(TesterBase):
    def test_init(self):
        try:
            charm = Charmander()
            bulb = Bulbasaur()
            squir = Squirtle()
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
        try:
            c = Charmander().get_attack()
            b = Bulbasaur().get_attack()
            s = Squirtle().get_attack()
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            if c != 7:
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b != 5:
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s != 4:
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_get_defence(self) -> int:
        try:
            c = Charmander().get_defence()
            b = Bulbasaur().get_defence()
            s = Squirtle().get_defence()
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            if c != 4:
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b != 5:
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s != 7:
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_get_speed(self) -> int:
        try:
            c = Charmander().get_speed()
            b = Bulbasaur().get_speed()
            s = Squirtle().get_speed()
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            if c != 8:
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b != 7:
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s != 7:
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_calculate_damage_taken(self) -> int:
        try:
            opponent = Charmander()
            c = Charmander().calculate_damage_taken(opponent)
            b = Bulbasaur().calculate_damage_taken(opponent)
            s = Squirtle().calculate_damage_taken(opponent)
        except Exception as e:
            self.verificationErrors.append(f"Calculate Damage method failed to execute: {str(e)}.")
            return
        try:
            if c != 7:
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b != 14:
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s != 1:
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)
