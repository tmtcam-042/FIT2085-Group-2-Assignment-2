import unittest
from tester_base import TesterBase

class GlitchMonTester(TesterBase):

    def test_superpower(self):
        # tests if superpower method is functional
        from missing_no import MissingNo
        # initialise missing No's superpower method
        try:
            result = MissingNo().superpower()
        except Exception as e:
            self.verificationErrors.append(f"Superpower method failed to execute: {str(e)}.")
            return
        # calls the function to test the return statements that can be given
        try:
            assert result == "MissingNo leveled up and increased HP!" or result == "MissingNo leveled up!" or result == "MissingNo increased HP!"
        except AssertionError:
            self.verificationErrors.append(f"Output is not printed correctly: {str(result)}.")
            return

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GlitchMonTester)
    unittest.TextTestRunner(verbosity=0).run(suite)
