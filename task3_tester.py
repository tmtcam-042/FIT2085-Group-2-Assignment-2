import unittest

from tester_base import TesterBase, captured_output

class TestTask3(TesterBase):

    def test_battle_example(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 0\n1 0 0") as (inp, out, err):
                # Here, Ash gets a Bulbasaur, and Misty gets a Charmander.
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Misty"
        except AssertionError:
            self.verificationErrors.append(f"Misty should win: {result}.")

        pokemon.set_hp(5)
        try:
            assert pokemon.hp == 5
        execept 



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask3)
    unittest.TextTestRunner(verbosity=0).run(suite)
