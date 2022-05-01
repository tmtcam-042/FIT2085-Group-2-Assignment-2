import unittest

from missing_no import MissingNo
from tester_base import TesterBase, captured_output

class MissingNoTester(TesterBase):

    def test_init(self):
        try:
            # initialises missing no object and verifies if this can be executed
            missN = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            # Checks the output to see if it is as expected
            s = str(missN)
            if s != "MissingNo's HP = 8 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_increase_hp(self):
        try:
            # initialises missing no's increase_ and verifies if this can be executed
            missN = MissingNo()
            missN.increase_hp()
            hp = missN.get_hp()
        except Exception as e:
            self.verificationErrors.append(f"increaseHp method failed to execute: {str(e)}.")
            return
        try:
            # Checks the output to see if it is as expected
            assert hp == 9
        except AssertionError:
            self.verificationErrors.append(f"HP is not printed correctly: {hp}.")
            return

    def test_get_name(self):
        try:
            # initialises missing no's get_name method and verifies if this can be executed
            name = MissingNo().get_name()
        except Exception as e:
            self.verificationErrors.append(f"Name method failed to execute: {str(e)}.")
            return
        try:
            # Checks the output to see if it is as expected
            assert name == "MissingNo"
        except AssertionError:
            self.verificationErrors.append(f"Name is not printed correctly: {name}.")
            return

    def test_get_attack(self):
        try:
            # initialises missing no's get_attack method and verifies if this can be executed
            attack = MissingNo().get_attack()
        except Exception as e:
            self.verificationErrors.append(f"getAttack method failed to execute: {str(e)}.")
            return
        try:
            # Checks the output to see if it is as expected
            assert attack == 8
        except AssertionError:
            self.verificationErrors.append(f"Attack is not printed correctly: {attack}.")
            return

    def test_get_defence(self):
        try:
            # initialises missing no's get_defence method and verifies if this can be executed
            defence = MissingNo().get_attack()
        except Exception as e:
            self.verificationErrors.append(f"getDefence method failed to execute: {str(e)}.")
            return
        try:
            # Checks the output to see if it is as expected
            assert defence == 8
        except AssertionError:
            self.verificationErrors.append(f"Defence is not printed correctly: {defence}.")
            return

    def test_get_speed(self):
        try:
            # initialises missing no's get_speed method and verifies if this can be executed
            speed = MissingNo().get_speed()
        except Exception as e:
            self.verificationErrors.append(f"getSpeed method failed to execute: {str(e)}.")
            return
        try:
            # Checks the output to see if it is as expected
            assert speed == 8
        except AssertionError:
            self.verificationErrors.append(f"Speed is not printed correctly: {str(speed)}.")
            return

    def test_calculate_damage_taken(self):
        from pokemon import Charmander
        try:
            # initialises missing no's calculate_damage_taken method and verifies if this can be executed
            with captured_output(str(Charmander())) as (inp, out, err):
                result = MissingNo().calculate_damage_taken(Charmander())
        except Exception as e:
            self.verificationErrors.append(f"Calculate Damage method failed to execute: {str(e)}.")
            return
        try:
            # Checks the output to see if it is as expected
            assert result == 3
        except AssertionError:
            self.verificationErrors.append(f"Damage taken is not printed correctly: {str(result)}.")
            return


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MissingNoTester)
    unittest.TextTestRunner(verbosity=0).run(suite)
