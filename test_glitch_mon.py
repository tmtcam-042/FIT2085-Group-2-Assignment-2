import unittest
from tester_base import TesterBase

class GlitchMonTester(TesterBase):

    def test_innit(self):
        pass

    def test_increaseHp(self):
        pass

    def test_superpower(self):
        from missing_no import MissingNo
        try:
            result = MissingNo().superPower()
        except Exception as e:
            self.verificationErrors.append(f"Superpower method failed to execute: {str(e)}.")
            return
        try:
            assert result == "MissingNo leveled up and increased HP!" or result == "MissingNo leveled up!" or result == "MissingNo increased HP!"
        except AssertionError:
            self.verificationErrors.append(f"Output is not printed correctly: {str(result)}.")
            return


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GlitchMonTester)
    unittest.TextTestRunner(verbosity=0).run(suite)
