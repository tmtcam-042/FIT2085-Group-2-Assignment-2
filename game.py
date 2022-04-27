"""
Game Driver file
"""

from battle import Battle

team1_name = input("Enter team 1 name: ")
team2_name = input("Enter team 2 name: ")
battle_mode = int(input("Input the preferred battle mode (0/1/2): "))

battle = Battle(team1_name, team2_name)

if battle_mode == 0:
    print("Winner: " + battle.set_mode_battle())

elif battle_mode == 1:
    print("Winner: " + battle.rotating_mode_battle())

elif battle_mode == 2:
    criterion1 = None
    criterion2 = None

    while criterion1 not in ["lvl", "hp", "attack", "defence", "speed"]:
        criterion1 = input(f"Input {team1_name}'s criteria: lvl, hp, attack, defence, speed: ").lower()

    while criterion2 not in ["lvl", "hp", "attack", "defence", "speed"]:
        criterion2 = input(f"Input {team2_name}'s criteria: lvl, hp, attack, defence, speed: ").lower()

    print("Winner: " + battle.optimised_mode_battle(criterion1, criterion2))

