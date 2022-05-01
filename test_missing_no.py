import unittest

from missing_no import MissingNo
from tester_base import TesterBase, captured_output

class MissingNoTester(TesterBase):

    def test_init(self):
        try:
            missN = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            s = str(missN)
            if s != "MissingNo's HP = 8 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_increaseHp(self):
        try:
            missN = MissingNo()
            missN.increaseHp()
            hp = missN.get_hp()
        except Exception as e:
            self.verificationErrors.append(f"increaseHp method failed to execute: {str(e)}.")
            return
        try:
            assert hp == 9
        except AssertionError:
            self.verificationErrors.append(f"HP is not printed correctly: {hp}.")
            return

    def test_get_name(self):
        try:
            name = MissingNo().get_name()
        except Exception as e:
            self.verificationErrors.append(f"Name method failed to execute: {str(e)}.")
            return
        try:
            assert name == "MissingNo"
        except AssertionError:
            self.verificationErrors.append(f"Name is not printed correctly: {name}.")
            return

    def test_get_attack(self):
        try:
            attack = MissingNo().get_attack()
        except Exception as e:
            self.verificationErrors.append(f"getAttack method failed to execute: {str(e)}.")
            return
        try:
            assert attack == 8
        except AssertionError:
            self.verificationErrors.append(f"Attack is not printed correctly: {attack}.")
            return

    def test_get_defence(self):
        try:
            defence = MissingNo().get_attack()
        except Exception as e:
            self.verificationErrors.append(f"getDefence method failed to execute: {str(e)}.")
            return
        try:
            assert defence == 8
        except AssertionError:
            self.verificationErrors.append(f"Defence is not printed correctly: {defence}.")
            return

    def test_get_speed(self):
        try:
            speed = MissingNo().get_speed()
        except Exception as e:
            self.verificationErrors.append(f"getSpeed method failed to execute: {str(e)}.")
            return
        try:
            assert speed == 8
        except AssertionError:
            self.verificationErrors.append(f"Speed is not printed correctly: {str(speed)}.")
            return

    def test_calculate_damage_taken(self):
        from pokemon import Charmander
        try:
            missN = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output(str(Charmander())) as (inp, out, err):
                result = missN.calculate_damage_taken(Charmander())
        except Exception as e:
            self.verificationErrors.append(f"Calculate Damage method failed to execute: {str(e)}.")
            return
        try:
            assert result == 3
        except AssertionError:
            self.verificationErrors.append(f"Damage taken is not printed correctly: {str(result)}.")
            return


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MissingNoTester)
    unittest.TextTestRunner(verbosity=0).run(suite)
