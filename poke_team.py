from pokemon import Charmander, Bulbasaur, Squirtle
from pokemon_base import PokemonBase
from stack_adt import ArrayStack


class PokeTeam:
    """
    Creates a team for a trainer with a maximum of 6 pokemon and sets the battle mode
    """

    def __init__(self, trainer_name):
        self.trainer_name = trainer_name
        # self.team = ArrayStack(6) #initialising team as an ArrayStack object and setting 6 as the max capacity
        self.battle_mode = 0  # default battle mode is 0
        self.team = None  # updated in choose_team

    def choose_team(self, battle_mode: int = 0, criterion: str = None) -> None:
        """
        Initialises the battle_mode and criterion through a user input and allows the program to engage with
        the user so that the user can select the layout of the team i.e how many types of pokemon in a team of 6.

        :param battle_mode: the battle mode of the battle between two teams
        :param criterion: Not being used right now
        return: None
        """
        # Set battle team
        if battle_mode > 2 or battle_mode < 0:
            raise ValueError("Battle mode can only be 0, 1 or 2")
        else:
            self.battle_mode = battle_mode

        choose_team_details = (f"Howdy {self.trainer_name}! Choose your team as C B S\n"
                               "where C is the number of Charmanders\n"
                               "      B is the number of Bulbasaurs\n"
                               "      S is the number of Squirtles\n")
        team = [0, 0, 0]    # updated below
        while True:
            try:
                team = list(map(int, input(choose_team_details).strip().split(" ")))
            except Exception as e:
                print(e)
                continue

            if sum(team) > 6:
                print("Your team can consist of a maximum of 6 pokemons")
                continue
            else:
                break

        self.assign_team(charm=team[0], bulb=team[1], squir=team[2])

    def assign_team(self, charm: int, bulb: int, squir: int) -> None:
        """
        Assigns the user's team with the inputted number of charmanders, bulbasaurs and squirtles.
        If the team has more than 6 pokemon, an exception is raised.

        :param charm: number of charmanders
        :param bulb: number of bulbasaurs
        :param squir: number of squirtles
        :return: None
        """
        if self.battle_mode == 0:
            self.team = ArrayStack(6)
        elif self.battle_mode == 1:
            pass
        elif self.battle_mode == 2:
            pass
        else:
            raise ValueError("Unexpected battle mode type")

        # for loop for pushing pokemons to self.team if team is not full
        [self.team.push(Squirtle()) for _ in range(squir) if not self.team.is_full()]
        [self.team.push(Bulbasaur()) for _ in range(bulb) if not self.team.is_full()]
        [self.team.push(Charmander()) for _ in range(charm) if not self.team.is_full()]

    def __str__(self) -> str:
        string = []
        # returning the user's team selection
        start_length = self.team.length  # Storing array length to restore later
        for i in range(len(self.team)):
            string.append(str(self.team.peek()))
            self.team.length -= 1  # get next element from the stack

        self.team.length = start_length  # reset the value of length for the stack
        # return ",".join(string)
        return ",\n".join(string) + "\n"

    def __len__(self) -> int:
        return self.team.length

    def pop(self) -> PokemonBase:
        if self.team.__class__.__name__ == "ArrayStack":
            return self.team.pop()
        else:
            raise Exception("Unknown data structure")

    def push(self, pokemon: PokemonBase) -> None:
        if self.team.__class__.__name__ == "ArrayStack":
            self.team.push(pokemon)
        else:
            raise Exception("Unknown data structure")

    def peek(self) -> PokemonBase:
        if self.team.__class__.__name__ == "ArrayStack":
            return self.team.peek()
        else:
            raise Exception("Unknown data structure")


if __name__ == "__main__":
    # ================= OUR TESTING =================
    poketeam = PokeTeam("Ash")
    poketeam.choose_team(1, None)
    print(poketeam)
    print(poketeam)

