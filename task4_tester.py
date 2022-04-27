import unittest

from tester_base import TesterBase, captured_output

class TestTask4(TesterBase):

    def test_battle_example(self):
        from battle import Battle

        try:
            b = Battle("Brock", "Gary")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1\n0 2 1") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Brock"
        except AssertionError:
            self.verificationErrors.append(f"Brock should win: {result}.")
        try:
            assert str(b.team1) == "Squirtle's HP = 8 and level = 1, Charmander's HP = 7 and level = 2, Charmander's HP = 7 and level = 2, Bulbasaur's HP = 7 and level = 1, Bulbasaur's HP = 8 and level = 2"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

    ### ADD TESTS HERE

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask4)
    unittest.TextTestRunner(verbosity=0).run(suite)
