from pokemon_base import PokemonBase
from poke_team import PokeTeam


class Battle:
    def __init__(self, trainer_one_name: str, trainer_two_name: str):
        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)
        self.battle_mode = None

    def set_battle_mode_to(self, value: int) -> None:
        if 0 <= value <= 2:
            self.battle_mode = value
        else:
            raise Exception("Unexpected battle mode value")

    # Task 3, set_mode_battle is a battle mode just like rotating mode and optimised mode
    def set_mode_battle(self) -> str:
        self.set_battle_mode_to(0)
        self.team1.choose_team()
        print(self.team1)
        self.team2.choose_team()
        print(self.team2)

        # Pretend the matchup bit is working

        # This is all inside some sort of loop:
        #   NOTE: to get a pokemon from a stack, pop it off
        #   once fighting is finished, push it back
        #   Never leave it hanging in the scope

        # FIGHT
        while len(self.team1) > 0 and len(self.team2) > 0:
            pokemon1 = self.team1.pop()
            pokemon2 = self.team2.pop()
            self.fight(pokemon1, pokemon2)
            if pokemon1.get_hp() > 0:
                self.team1.push(pokemon1)
            if pokemon2.get_hp() > 0:
                self.team2.push(pokemon2)

        # Return winner or draw
        if self.team1.team.length > 0:
            return "TEAM 1"
        elif self.team2.team.length > 0:
            return "TEAM 2"
        else:
            return "DRAW"

    def rotating_mode_battle(self) -> str:  # Task 4
        self.set_battle_mode_to(1)
        return ""

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:  # Task 5
        self.set_battle_mode_to(2)
        return ""

    def fight(self, pokemon1: PokemonBase, pokemon2: PokemonBase) -> None:
        if pokemon1.get_speed() > pokemon2.get_speed():  # P1 fights P2 first, then P2 has chance to retaliate.
            print("P1 is faster than P2")
            pokemon2.set_hp(pokemon2.get_hp() - pokemon2.calculate_damage_taken(pokemon1))
            if pokemon2.get_hp() > 0:
                pokemon1.set_hp(pokemon1.get_hp() - pokemon1.calculate_damage_taken(pokemon2))
            else:
                # P2 removed from team. Don't know what this implementation looks like
                pokemon1.set_level(pokemon1.get_level() + 1)
                # P1 returned to team. Don't know what this implementation looks like

        elif pokemon1.get_speed() < pokemon2.get_speed():  # P2 fights P1 first, then P1 has chance to retaliate.
            print("P1 is slower than P2")
            pokemon1.set_hp(pokemon1.get_hp() - pokemon1.calculate_damage_taken(pokemon2))
            if pokemon1.get_hp() > 0:
                pokemon2.set_hp(pokemon2.get_hp() - pokemon2.calculate_damage_taken(pokemon1))
            else:
                # P1 removed from team. Don't know what this implementation looks like
                pokemon2.set_level(pokemon2.get_level() + 1)
                # P2 returned to team. Don't know what this implementation looks like

        else:  # Both fight at same time!
            print("Equal speeds!")
            pokemon1.set_hp(pokemon1.get_hp() - pokemon1.calculate_damage_taken(pokemon2))  # P1 takes damage
            pokemon2.set_hp(pokemon2.get_hp() - pokemon2.calculate_damage_taken(pokemon1))  # P2 takes damage
            # Check conditions.
            if pokemon1.get_hp() > 0 and pokemon2.get_hp() > 0:  # Did both survive mutual clash
                pokemon1.set_hp(pokemon1.get_hp() - 1)  # Both lose 1 hp for the sin of surviving
                pokemon2.set_hp(pokemon2.get_hp() - 1)
                if pokemon1.get_hp() > 0 and pokemon2.get_hp() > 0:
                    # Both returned to teams. Don't know what this implementation looks like.
                    pass
                elif pokemon1.get_hp() > 0:
                    # P2 removed from team. Don't know what this implementation looks like.
                    pokemon1.level_up()
                    # P1 returned to team. Don't know what this implementation looks like.
                else:
                    # P1 removed from team.
                    pokemon2.level_up()
                    # P2 returned to team.

            elif pokemon1.get_hp() > 0:  # P1 lived and P2 didn't
                # P2 removed from team. Don't know what this implementation looks like.
                pokemon1.level_up()
                # P1 returned to team. Don't know what this implementation looks like.
            else:  # P2 lived and P1 didn't
                # P1 removed from team.
                pokemon2.level_up()
                # P2 returned to team.

        print(f"{pokemon1.get_name()} hp: {str(pokemon1.get_hp())}")
        print(f"{pokemon2.get_name()} hp: {str(pokemon2.get_hp())}\n")


if __name__ == "__main__":
    # ================= EXAMPLE APP EXECUTION =================
    b = Battle("Ash", "Gary")
    print(b.set_mode_battle())

