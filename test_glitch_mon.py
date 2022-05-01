import unittest
from tester_base import TesterBase, captured_output
from glitch_mon import GlitchMon

class GlitchMonTester(TesterBase):

    def test_glitch_mon(self):
        from glitch_mon import GlitchMon
        try:
            MissingNo = GlitchMon()
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 0 0 2\n1 1 1 1") as (inp, out, err):
                # 0 0 0 2 should fail. Too many missingos.
                # So 1 1 1 1 should be the correct team.
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()
        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask4)
    unittest.TextTestRunner(verbosity=0).run(suite)