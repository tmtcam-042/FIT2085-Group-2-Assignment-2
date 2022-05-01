from missing_no import MissingNo
from pokemon import Charmander, Bulbasaur, Squirtle
from pokemon_base import PokemonBase
from stack_adt import ArrayStack
from queue_adt import CircularQueue
from sorted_list import ListItem
from array_sorted_list import ArraySortedList

class PokeTeam:
    """
    Creates a team for a trainer with a maximum of 6 pokemon and sets the battle mode
    """

    def __init__(self, trainer_name):
        self.trainer_name = trainer_name
        self.battle_mode = 0  # default battle mode is 0
        self.team = None  # updated in choose_team

    def choose_team(self, battle_mode: int = 0, criterion: str = None) -> None:
        """
        Initialises the battle_mode and criterion through a user input and allows the program to engage with
        the user so that the user can select the layout of the team i.e how many types of pokemon in a team of 6.

        :param battle_mode: the battle mode of the battle between two teams
        :param criterion: Used in optimised battle mode to determine criterion to sort by
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
                               "      S is the number of Squirtles\n"
                               "      M is the number of Unknown Pokémon\n")
        team = [0, 0, 0]  # updated below

        while True:
            try:
                team = list(map(int, input(choose_team_details).strip().split(" ")))
            except Exception as e:
                print(e)
                continue
            if sum(team) > 6:
                print("Your team can only consist of a maximum of 6 pokemons")
                continue
            elif team[3] > 1:
                print("Your team can only consist of a maximum of 1 missing pokemon")
                continue
            else:
                break

        # Extending team to hold 4 values so that criterion can be directly passed
        while len(team) < 4:
            team.append(0)
        self.assign_team(*team, criterion=criterion)

    def assign_team(self, charm: int = 0, bulb: int = 0, squir: int = 0, missN: int = 0, criterion: str = None) -> None:
        """
        Assigns the user's team with the inputted number of charmanders, bulbasaurs and squirtles.
        If the team has more than 6 pokemon, an exception is raised.

        :param charm: number of charmanders
        :param bulb: number of bulbasaurs
        :param squir: number of squirtles
        :return: None
        """
        if self.battle_mode == 0:

            self.assign_set_mode_battle(charm, bulb, squir, missN)

        elif self.battle_mode == 1:

            self.assign_rotating_mode_battle(charm, bulb, squir, missN)

        elif self.battle_mode == 2:

            self.assign_optimised_mode_battle(charm, bulb, squir, missN, criterion)
        else:
            raise ValueError("Unexpected battle mode type")

    def assign_set_mode_battle(self, charm: int, bulb: int, squir: int, missN: int) -> None:
        """
        Assigns the user's team with the desired number of pokemon in set mode battle format(Using a stack ADT)

        :param charm: number of charmanders
        :param bulb: number of bulbasaurs
        :param squir: number of squirtles
        :return: None
        """

        self.team = ArrayStack(6)
        [self.team.push(MissingNo()) for _ in range(missN) if not self.team.is_full()]
        # for loop for pushing pokemons to self.team(Stack ADT) if team is not full
        [self.team.push(Squirtle()) for _ in range(squir) if not self.team.is_full()]
        [self.team.push(Bulbasaur()) for _ in range(bulb) if not self.team.is_full()]
        [self.team.push(Charmander()) for _ in range(charm) if not self.team.is_full()]

    def assign_rotating_mode_battle(self, charm: int, bulb: int, squir: int, missN: int) -> None:
        """
        Assigns the user's team with the desired number of pokemon in rotating mode battle format(Using a CircularQueue ADT)

        :param charm: number of charmanders
        :param bulb: number of bulbasaurs
        :param squir: number of squirtles
        :return: None
        """
        self.team = CircularQueue(6)
        # for loop for pushing pokemons to self.team(CircularQueue ADT) if team is not full
        [self.team.append(MissingNo()) for _ in range(missN) if not self.team.is_full()]
        [self.team.append(Charmander()) for _ in range(charm) if not self.team.is_full()]
        [self.team.append(Bulbasaur()) for _ in range(bulb) if not self.team.is_full()]
        [self.team.append(Squirtle()) for _ in range(squir) if not self.team.is_full()]

    def assign_optimised_mode_battle(self, charm: int, bulb: int, squir: int, missN: int, criterion: str) -> None:
        """
        Assigns the user's team with the desired number of pokemon in optimised mode battle format(Using a SortedList ADT)

        :pre: criterion is a valid string. Checked in Battle.optimised_mode_battle
        :param charm: number of charmanders
        :param bulb: number of bulbasaurs
        :param squir: number of squirtles
        :return: None
        :raise Exception: if criterion is invalid
        """
        self.team = ArraySortedList(6)
        # for loop for pushing pokemons to self.team(CircularQueue ADT) if team is not full
        [self.team.add(ListItem(Charmander(), Charmander().get_criterion(criterion))) for _ in range(charm)]
        [self.team.add(ListItem(Bulbasaur(), Bulbasaur().get_criterion(criterion))) for _ in range(bulb)]
        [self.team.add(ListItem(Squirtle(), Squirtle().get_criterion(criterion))) for _ in range(squir)]

        # add MissingNo here. By giving it a key value of zero, we ensure that it will always act after 
        # every other pokemon has fought at least once.
        [self.team.add(ListItem(MissingNo(), 0)) for _ in range(missN)]

    def __str__(self) -> str:
        string = []
        # returning the user's team selection

        if self.team.__class__.__name__ == "ArrayStack":
            initial_length = self.team.length
            for i in range(len(self)):
                string.append(str(self.team.peek()))
                self.team.length -= 1
            self.team.length = initial_length

        elif self.team.__class__.__name__ == "CircularQueue":
            for i in range(len(self)):
                item = self.team.serve()
                string.append(str(item))
                self.team.append(item)

        elif self.team.__class__.__name__ == "ArraySortedList":
            for i in range(len(self.team) - 1, -1, -1):
                string.append(str(self.team[i].value))

        return ", ".join(string)

    def __len__(self) -> int:
        return self.team.length

    def remove(self) -> PokemonBase:
        if self.team.__class__.__name__ == "ArrayStack":
            return self.team.pop()
        elif self.team.__class__.__name__ == "CircularQueue":
            return self.team.serve() 
        elif self.team.__class__.__name__ == "ArraySortedList":
            return self.team.delete_at_index(0).value
        else:
            raise Exception("Unknown data structure")

    def push(self, pokemon: PokemonBase, criterion: str = None) -> None:
        if self.team.__class__.__name__ == "ArrayStack":
            self.team.push(pokemon)
        elif self.team.__class__.__name__ == "CircularQueue":
            return self.team.append(pokemon)
        elif self.team.__class__.__name__ == "ArraySortedList":
            self.team.add(ListItem(pokemon, pokemon.get_criterion(criterion)))
        else:
            raise Exception("Unknown data structure")

