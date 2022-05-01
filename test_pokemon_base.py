from pokemon import Charmander, Bulbasaur, Squirtle
from tester_base import TesterBase
import unittest

class TestPokemonBase(TesterBase):

    def test_init(self):
        pass

    def test_get_hp(self) -> int:
        # instantises each pokemon's get_hp method and checks for errors
        try:
            c = Charmander().get_hp()
            b = Bulbasaur().get_hp()
            s = Squirtle().get_hp()
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return

        # checks if the output values are the ones intended and raises a verification error else
        try:
            if c != 7:
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b != 9:
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s != 8:
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_get_level(self) -> int:
        # instantises each pokemon's get_level method and checks for errors
        try:
            c = Charmander().get_level()
            b = Bulbasaur().get_level()
            s = Squirtle().get_level()
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        # checks if the output values are the ones intended and raises a verification error else
        try:
            if c != 1:
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b != 1:
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s != 1:
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_level_up(self) -> int:
        try:
            c = Charmander()
            c.level_up()
            b = Bulbasaur()
            b.level_up()
            s = Squirtle()
            s.level_up()
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return

        try:
            if c.get_level() != 2:
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b.get_level() != 2:
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s.get_level() != 2:
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_set_hp(self) -> None:
        try:
            c = Charmander()
            c.set_hp(10)
            b = Bulbasaur()
            b.set_hp(10)
            s = Squirtle()
            s.set_hp(10)
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            if c.get_hp() != 10:
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b.get_hp() != 10:
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s.get_hp() != 10:
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_set_level(self) -> None:
        try:
            c = Charmander()
            c.set_level(5)
            b = Bulbasaur()
            b.set_level(5)
            s = Squirtle()
            s.set_level(5)
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            if c.get_level() != 5:
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b.get_level() != 5:
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s.get_level() != 5:
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_get_name(self) -> str:
        pass

    def test_get_speed(self) -> int:
        pass

    def test_get_attack(self) -> int:
        pass

    def test_get_poke_type(self) -> str:
        try:
            c = Charmander().get_poke_type()
            b = Bulbasaur().get_poke_type()
            s = Squirtle().get_poke_type()
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return

        try:
            if c != "Fire":
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b != "Grass":
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s != "Water":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_get_criterion(self) -> int:
        try:
            c = Charmander().get_criterion("lvl")
            b = Bulbasaur().get_criterion("hp")
            s = Squirtle().get_criterion("attack")
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            if c != 1:
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b != 9:
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s != 4:
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_calculate_damage_taken(self) -> int:
        pass

    def test_got_hurt_by(self) -> None:
        try:
            c = Charmander()
            c.got_hurt_by(Charmander())
            b = Bulbasaur()
            b.got_hurt_by(Charmander())
            s = Squirtle()
            s.got_hurt_by(Charmander())
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return

        try:
            if c.get_hp() != 0:
                self.verificationErrors.append(f"String method did not return correct string: {c}")
            if b.get_hp() != -5:
                self.verificationErrors.append(f"String method did not return correct string: {b}")
            if s.get_hp() != 7:
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)
