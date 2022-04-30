import unittest

from tester_base import TesterBase, captured_output


class TestBattle(TesterBase):

    def test_init(self):
        pass

    def test_set_battle_mode_to(self):
        pass

    def test_set_mode_battle(self):
        pass

    def test_rotating_mode_battle(self):
        pass

    def test_optimised_mode_battle(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Gary")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1\n 0 2 1") as (inp, out, err):
                result = b.optimised_mode_battle("hp", "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Ash"
        except AssertionError:
            self.verificationErrors.append(f"Ash should win: {result}.")
        try:
            assert str(b.team1) == "Bulbasaur's HP = 6 and level = 1, Bulbasaur's HP = 5 and level = 2, Squirtle's HP = 2 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}.")

    def test_fight(self):
        from battle import Battle
        from pokemon import Charmander, Squirtle
        try:
            b = Battle("Ash", "Gary")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            p1 = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"pokemon1 could not be instantiated: {str(e)}.")
            return
        try:
            p2 = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"pokemon2 could not be instantiated: {str(e)}.")
            return
        try:
            b.fight(p1, p2)
        except Exception as e:
            self.verificationErrors.append(f"Fight failed to execute: {str(e)}.")
            return
        try:
            assert p1.hp == -1
        except AssertionError:
            self.verificationErrors.append(f"Charmander should have -1 hp: {str(p1.hp)}.")
        try:
            assert p2.hp == 7
        except AssertionError:
            self.verificationErrors.append(f"Squirtle should have 7 hp: {str(p2.hp)}.")
        try:
            assert p2.level == 2
        except AssertionError:
            self.verificationErrors.append(f"Squirtle should be level 2: {str(p2.level)}.")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBattle)
    unittest.TextTestRunner(verbosity=0).run(suite)

