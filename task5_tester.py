import unittest

from tester_base import TesterBase, captured_output

class TestTask4(TesterBase):

    def test_battle_example(self):
        from battle import Battle

        try:
            b = Battle("Cynthia", "Steven")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1\n0 2 1") as (inp, out, err):
                result = b.optimised_mode_battle("hp", "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            # Gen IV supremacy >:D
            assert result == "Cynthia"
        except AssertionError:
            self.verificationErrors.append(f"Cynthia should win: {result}.")
        try:
            assert str(b.team1) == "Bulbasaur's HP = 6 and level = 1, Bulbasaur's HP = 5 and level = 2, Squirtle's HP = 2 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

    ### ADD TESTS HERE

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask4)
    unittest.TextTestRunner(verbosity=0).run(suite)