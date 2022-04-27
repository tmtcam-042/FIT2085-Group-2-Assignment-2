
# for loop for pushing pokemons to self.team if team is not full
        [self.team.push(Squirtle()) for _ in range(squir) if not self.team.is_full()]
        [self.team.push(Bulbasaur()) for _ in range(bulb) if not self.team.is_full()]
        [self.team.push(Charmander()) for _ in range(charm) if not self.team.is_full()]
        
class TestTask1(TesterBase):

    def test_charmander_string(self):
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            s = str(c)
            if s != "Charmander's HP = 7 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    ### ADD TESTS HERE

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask1)
    unittest.TextTestRunner(verbosity=0).run(suite)
