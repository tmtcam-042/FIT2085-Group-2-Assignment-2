"""
Game Driver file, used to run the entire application.
Every file for Assignment_2's functionality will be run by calling this file,
enabling a user to play the entire game.
Performs pre-condition checking of criterion and is therefore important to
proper game execution.
"""
__author__ = "Kisara Batugedara, Rishi Bidani, Neth Botheju, Thomas Cameron"
__docformat__ = "reStructuredText"

from battle import Battle

team1_name = input("Enter team 1 name: ")
team2_name = input("Enter team 2 name: ")
battle_mode = int(input("Input the preferred battle mode (0/1/2): "))

battle = Battle(team1_name, team2_name)

if battle_mode == 0:
    print(battle.team1)
    print("Winner: " + battle.set_mode_battle())

elif battle_mode == 1:
    print("Winner: " + battle.rotating_mode_battle())

elif battle_mode == 2:
    criterion1 = None
    criterion2 = None

    # Checking pre-conditions for optimised battle mode
    while criterion1 not in ["lvl", "hp", "attack", "defence", "speed"]:
        criterion1 = input(f"Input {team1_name}'s criteria: lvl, hp, attack, defence, speed: ").lower()

    while criterion2 not in ["lvl", "hp", "attack", "defence", "speed"]:
        criterion2 = input(f"Input {team2_name}'s criteria: lvl, hp, attack, defence, speed: ").lower()

    print("Winner: " + battle.optimised_mode_battle(criterion1, criterion2))


