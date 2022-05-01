from pokemon import Charmander, Bulbasaur, Squirtle
import unittest
from tester_base import TesterBase

class TestPokemon(TesterBase):
    def test_init(self):
        try:
            charm = Charmander()    # initialize Charmander
            bulb = Bulbasaur()      # initialize Bulbasaur
            squir = Squirtle()      # initialize Squirtle
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.") # if it can't be instantiated
            return
        try:
            c = str(charm)        # convert Charmander to string
            b = str(bulb)         # convert Bulbasaur to string
            s = str(squir)        # convert Squirtle to string

            # check if the string is correct
            if c != "Charmander's HP = 7 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {c}") # if it is not correct add to verificationErrors
            # check if the string is correct
            if b != "Bulbasaur's HP = 9 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {b}") # if it is not correct add to verificationErrors
            # check if the string is correct
            if s != "Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}") # if it is not correct add to verificationErrors

        # if it can't be instantiated
        except Exception as e:
            # add to verificationErrors
            self.verificationErrors.append(f"String method failed. {e}")

    def test_get_name(self) -> str:
        try:
            c = Charmander().get_name() # get name of Charmander
            b = Bulbasaur().get_name()  # get name of Bulbasaur
            s = Squirtle().get_name()   # get name of Squirtle
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.") # if it can't be instantiated -> add to verificationErrors
            return
        try:
            # check if the name is correct
            if c != "Charmander":
                self.verificationErrors.append(f"String method did not return correct string: {c}") # else add to verificationErrors
            # check if the name is correct
            if b != "Bulbasaur":
                self.verificationErrors.append(f"String method did not return correct string: {b}") # else add to verificationErrors
            # check if the name is correct
            if s != "Squirtle":
                self.verificationErrors.append(f"String method did not return correct string: {s}") # else add to verificationErrors
        except Exception as e:
            # add to verifications errors if something goes wrong
            self.verificationErrors.append(f"String method failed. {e}")

    def test_get_attack(self) -> int:
        try:
            c = Charmander().get_attack() # get attack of Charmander
            b = Bulbasaur().get_attack()  # get attack of Bulbasaur
            s = Squirtle().get_attack()   # get attack of Squirtle
        except Exception as e:
            # if it cannot get attack add to verificationErrors
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.")
            return
        try:
            # check if the attack is correct
            if c != 7:
                self.verificationErrors.append(f"String method did not return correct string: {c}") # if it is not correct add to verificationErrors
            # check if the attack is correct
            if b != 5:
                self.verificationErrors.append(f"String method did not return correct string: {b}") # if it is not correct add to verificationErrors
            # check if the attack is correct
            if s != 4:
                self.verificationErrors.append(f"String method did not return correct string: {s}") # if it is not correct add to verificationErrors
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_get_defence(self) -> int:
        try:
            c = Charmander().get_defence() # get defence of Charmander
            b = Bulbasaur().get_defence() # get defence of Bulbasaur
            s = Squirtle().get_defence() # get defence of Squirtle
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.") # if it can't be instantiated -> add to verificationErrors
            return
        try:
            # check if the defence is correct
            if c != 4:
                self.verificationErrors.append(f"String method did not return correct string: {c}") # if it is not correct add to verificationErrors
            # check if the defence is correct
            if b != 5:
                self.verificationErrors.append(f"String method did not return correct string: {b}") # if it is not correct add to verificationErrors
            # check if the defence is correct
            if s != 7:
                self.verificationErrors.append(f"String method did not return correct string: {s}") # if it is not correct add to verificationErrors
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_get_speed(self) -> int:
        try:
            c = Charmander().get_speed() # get speed of Charmander
            b = Bulbasaur().get_speed()  # get speed of Bulbasaur
            s = Squirtle().get_speed()   # get speed of Squirtle
        except Exception as e:
            self.verificationErrors.append(f"Missing No could not be instantiated: {str(e)}.") # if it can't be instantiated -> add to verificationErrors
            return
        try:
            # check if the speed is correct
            if c != 8:
                self.verificationErrors.append(f"String method did not return correct string: {c}") # if it is not correct add to verificationErrors
            # check if the speed is correct
            if b != 7:
                self.verificationErrors.append(f"String method did not return correct string: {b}") # if it is not correct add to verificationErrors
            # check if the speed is correct
            if s != 7:
                self.verificationErrors.append(f"String method did not return correct string: {s}") # if it is not correct add to verificationErrors
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_calculate_damage_taken(self) -> int:
        try:
            # create a new Charmander opponent
            opponent = Charmander()
            c = Charmander().calculate_damage_taken(opponent) # calculate damage taken by opponent
            b = Bulbasaur().calculate_damage_taken(opponent) # calculate damage taken by opponent
            s = Squirtle().calculate_damage_taken(opponent) # calculate damage taken by opponent
        except Exception as e:
            self.verificationErrors.append(f"Calculate Damage method failed to execute: {str(e)}.")
            return
        try:
            # check if the damage taken is correct
            if c != 7:
                self.verificationErrors.append(f"String method did not return correct string: {c}") # if it is not correct add to verificationErrors
            # check if the damage taken is correct
            if b != 14:
                self.verificationErrors.append(f"String method did not return correct string: {b}") # if it is not correct add to verificationErrors
            # check if the damage taken is correct
            if s != 1:
                self.verificationErrors.append(f"String method did not return correct string: {s}") # if it is not correct add to verificationErrors
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}") # if Exception raised -> add to verificationErrors


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)
