from battle_game_pkg.cards import *
from battle_game_pkg.displays import *
from battle_game_pkg.battle import *

player_hand = []
computer_hand = []
field_list = []

while True:
    show_home_screen()

    home_selection = int(input("Please select an option: "))

    if home_selection == 1:
        player_draw_cards(player_deck_of_cards, player_hand)
        computer_draw_cards(computer_deck_of_cards, computer_hand)
        player_play_card(player_hand, field_list)
        computer_play_card(computer_hand, field_list)
        battle_loop(field_list, computer_deck_of_cards,
                    computer_hand, player_deck_of_cards, player_hand)
    elif home_selection == 2:
        display_cards(computer_deck_of_cards, player_deck_of_cards)
    elif home_selection == 3:
        ruleset()
    elif home_selection == 4:
        print("\nThanks for playing!")
        exit()
    else:
        print("Invalid input. Please select a valid menu option.")
