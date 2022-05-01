import unittest

from tester_base import TesterBase, captured_output
from poke_team import PokeTeam

class TestPokeTeam(TesterBase):

    def test_choose_team(self):
        try:
           team = PokeTeam("Gary")
        except Exception as e:
            self.verificationErrors.append(f"Gary's team could not be instantiated: {str(e)}.")
        try:
            with captured_output("3 4 1\n2 2 2") as (inp, out, err):
                # 3 4 1 should fail, since it is too many pokemon.
                # So 2 2 2 should be the correct team.
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Gary's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    def test_assign_team(self):
        team = PokeTeam("Ash")
        try:
            team.battle_mode = 0
            team.assign_team(3, 2, 0, 0, "lvl")
            assert team.team.__class__.__name__ == "ArrayStack"
        except AssertionError as e:
            self.verificationErrors.append(f"Incorrect ADT, expected ArrayStack got {team.team.__class__.__name__}")

        try:
            team.battle_mode = 1
            team.assign_team(3, 2, 0, 0, "lvl")
            assert team.team.__class__.__name__ == "CircularQueue"
        except AssertionError as e:
            self.verificationErrors.append(f"Incorrect ADT, expected CircularQueue got {team.team.__class__.__name__}")

        try:
            team.battle_mode = 2
            team.assign_team(3, 2, 0, 0, "lvl")
            assert team.team.__class__.__name__ == "ArraySortedList"
        except AssertionError as e:
            self.verificationErrors.append(
                f"Incorrect ADT, expected ArraySortedList got {team.team.__class__.__name__}")

    def test_assign_set_mode_battle(self):
        team = PokeTeam("Ash")
        to_be_found = None
        last_pokemon = None
        try:
            pokemons = 3, 2, 1, 0
            team.assign_set_mode_battle(*pokemons)

            to_be_found = "Charmander"
            for i in range(pokemons[0]):
                last_pokemon = team.remove().__class__.__name__
                assert last_pokemon == "Charmander"

            to_be_found = "Bulbasaur"
            for i in range(pokemons[1]):
                last_pokemon = team.remove().__class__.__name__
                assert last_pokemon == "Bulbasaur"

            to_be_found = "Squirtle"
            for i in range(pokemons[2]):
                last_pokemon = team.remove().__class__.__name__
                assert last_pokemon == "Squirtle"

        except AssertionError as e:
            self.verificationErrors.append(f"Incorrect pokemon found. Expected: {to_be_found}, Got: {last_pokemon}")

    def test_assign_rotating_mode_battle(self):
        poketeam = PokeTeam("Ash")
        try:
            pokemons = 2, 2, 1, 1
            poketeam.assign_rotating_mode_battle(*pokemons)
        except Exception as e:
            self.verificationErrors.append(f"Team failed to assign: {str(e)}.")
            return
        try:
            # Check that MissingNo is first pokemon in the list
            pokemons = 2, 2, 1, 1
            poketeam.assign_rotating_mode_battle(*pokemons)
            get_pokemon = poketeam.team.serve()
            assert get_pokemon.__class__.__name__ == "MissingNo"
        except AssertionError as e:
            self.verificationErrors.append(f"MissingNo not first pokemon in list: {str(e)}.")
        try:
            # Check that Charmander is second pokemon in the list
            pokemons = 2, 2, 1, 1
            poketeam.assign_rotating_mode_battle(*pokemons)
            get_pokemon = poketeam.team.serve()
            assert get_pokemon.__class__.__name__ == "Charmander"
        except AssertionError as e:
            self.verificationErrors.append(f"Charmander not second pokemon in list: {str(e)}.")
        try:
            # Check that Bulbasaur is third pokemon in the list
            get_pokemon = poketeam.team.serve()
            assert get_pokemon.__class__.__name__ == "Bulbasaur"
        except AssertionError as e:
            self.verificationErrors.append(f"Bulbasaur not third pokemon in list: {str(e)}.")
        try:
            # Check that Squirtle is last in the list
            get_pokemon = poketeam.team.serve()
            assert get_pokemon.__class__.__name__ == "Squirtle"
        except AssertionError as e:
            self.verificationErrors.append(f"Squirtle not fourth pokemon in list: {str(e)}.")
        try:
            # Check that order of list is 2 M, 2 C, 1 B, 1 S
            assert str(poketeam) == "MissingNo's HP = 8 and level = 1, MissingNo's HP = 8 and level = 1, Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError as e:
            self.verificationErrors.append(f"Team is not correct after assignment: {str(e)}.")


    def test_assign_optimised_mode_battle(self):
        poketeam = PokeTeam("Ash")
        try:
            pokemons = 1, 1, 1, 1
            criterion = "hp"
            poketeam.assign_optimised_mode_battle(*pokemons, criterion)
        except Exception as e:
            self.verificationErrors.append(f"Team failed to assign: {str(e)}.")
            return
        try:
            # Check that MissingNo is final pokemon
            assert poketeam.team[0].value.name == "MissingNo"
        except AssertionError as e:
            self.verificationErrors.append(f"MissingNo not final pokemon in list: {str(e)}.")
        try:
            # Check that pokemon with greatest initial hp, bulbasaur, is at head of list
            assert poketeam.team[3].value.name == "Bulbasaur"
        except AssertionError as e:
            self.verificationErrors.append(f"Bulbasaur not first pokemon in list: {str(e)}.")
        try:
            # Check that pokemon with second greatest initial hp, Squirtle, is second in list
            assert poketeam.team[2].value.name == "Squirtle"
        except AssertionError as e:
            self.verificationErrors.append(f"Squirtle not second pokemon in list: {str(e)}.")
        try:
            # Check that pokemon with lowest initial hp, Charmander, is third in list
            assert poketeam.team[1].value.name == "Charmander"
        except AssertionError as e:
            self.verificationErrors.append(f"Charmander not third pokemon in list: {str(e)}.")

        try:
           criterion = "lvl"
           poketeam.assign_optimised_mode_battle(*pokemons, criterion)
        except Exception as e:
            self.verificationErrors.append(f"Team failed to assign: {str(e)}.")
            return
        try:
            # Check that order of list is C, B, S, M if starting sorting value is all the same
            assert str(poketeam) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError as e:
            self.verificationErrors.append(f"Team is not correct after assignment: {str(e)}.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokeTeam)
    unittest.TextTestRunner(verbosity=0).run(suite)
