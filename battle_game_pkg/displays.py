import time


def show_home_screen():
    """ Display Home Screen and Options """
    print("""
          ==_==_==  Are you ready to Battle?!  ==_==_==
        -------------------------------------------------
        [-|             1. Start Game                 |-]
        [-|             2. Display Cards              |-]
        [-|             3. Rules                      |-]
        [-|             4. Quit Game                  |-]
        -------------------------------------------------
        """)


def ruleset():
    """ Display the ruleset to the player """
    print("""
    The rules of game are rather simple...
    
    Be the last to run out of cards and win the game.

    How do you do this?
    """)
    time.sleep(4)
    print("""
    You will be assigned a shuffled deck of 15 cards.
    
    3 cards will be in your hand at a time.

    A coin toss will decide who is the first to play a card.

    Whoever is first plays a card to the field.
    """)
    time.sleep(5)
    print("""
    Your goal is to put your stronger card against that card and WIN!

    Each card has an Attack, Defence, and Health value.

    Once health reaches 0, that card is destroyed.
    """)
    time.sleep(5)
    print("""
    The winning card is left on the field.

    Be the last player with cards, and win the game!
    """)


def display_cards(computerlist, playerlist):
    """ Display the list of cards for the user to see"""
    user_selection = int(input("""
    Which deck would you like to see?
    1) Your deck
    2) Computer deck
    3) Main Menu
    """))
    if user_selection == 1:
        for obj in playerlist:
            print(
                f"Name: {obj.name} Attack: {obj.attack} Defence Rating: {obj.defence} Health Points: {obj.health}\n")
    elif user_selection == 2:
        for obj in computerlist:
            print(
                f"Name: {obj.name} Attack: {obj.attack} Defence Rating: {obj.defence} Health Points: {obj.health}\n")
    elif user_selection == 3:
        show_home_screen()
    else:
        print("Invalid input")
