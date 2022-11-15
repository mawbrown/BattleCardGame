import random
import time


def who_goes_first():
    """ Decide who goes first based on a random number of 1 or 2 (coin toss)"""
    coin_toss = random.randint(1, 2)
    user_guess = int(input("Heads or tails (1 or 2)? "))
    while True:
        if coin_toss == 1 and user_guess == 1:
            print("\nHeads! You go first!\n")
            return True
        elif coin_toss == 1 and user_guess == 2:
            print("\nHeads! Computer goes first\n")
            return False
        elif coin_toss == 2 and user_guess == 1:
            print("\nTails! Computer goes first\n")
            return False
        elif coin_toss == 2 and user_guess == 2:
            print("\nTails! You go first!\n")
            return True
        else:
            print("\nInvalid input.\n")
            user_guess = int(input("Select either 1 or 2: "))


def shuffle_cards(list):
    """ Shuffles the deck of cards """
    return random.shuffle(list)


def player_draw_cards(list, playerhand):
    """ Player is assigned 3 cards from the shuffled list (deck) """
    shuffle_cards(list)
    max_hand = 3
    i = 0
    cardNum = 1
    if len(list) > 0:
        while len(playerhand) < max_hand:
            playerhand.append(list[i])
            list.pop(i)
            i += 1

        for obj in playerhand:
            print(
                f"Card {cardNum}\nName: {obj.name}\nAttack: {obj.attack}\nDefence Rating: {obj.defence}\nHealth Points: {obj.health}\n")
            cardNum += 1

    elif len(playerhand) == 0:
        print("You have lost... You have no more cards.")
        exit()

    else:
        print("\nYour deck has run out of cards!\nThe only cards left are in your hand!\n")
        for obj in playerhand:
            print(
                f"Card {cardNum}\nName: {obj.name}\nAttack: {obj.attack}\nDefence Rating: {obj.defence}\nHealth Points: {obj.health}\n")
            cardNum += 1


def computer_draw_cards(list, computerhand):
    """ Computer is assigned 3 cards from the shuffled list (deck) """
    shuffle_cards(list)
    max_hand = 3
    i = 0
    if len(list) > 0:
        while len(computerhand) < max_hand:
            computerhand.append(list[i])
            list.pop(i)
            i += 1
    elif len(computerhand) == 0:
        print("You have won! The computer has no more cards.")
        exit()
    else:
        print(
            "\nThe computer's deck has run out of cards.\nFinish off what's in their hand!\n")


def player_play_card(playerhand, fieldlist):
    """ Gets player input to select a card to go on the field """
    if playerhand != 0:
        player_choice = int(
            input("What card will you play from your hand (1, 2, 3)? ")) - 1
        fieldlist.insert(0, playerhand[player_choice])
        playerhand.pop(player_choice)
    else:
        print("You are out of cards")


def computer_play_card(computerhand, fieldlist):
    """ Computer plays a card to the field """
    if computerhand != 0:
        computer_choice = random.randint(0, (len(computerhand)-1))
        fieldlist.insert(1, computerhand[computer_choice])
        computerhand.pop(computer_choice)
    else:
        print("The computer is out of cards")

    # TESTING PURPOSES ONLY
    # for obj in fieldlist:
    #     print(
    #         f"Name: {obj.name} Attack: {obj.attack} Defence Rating: {obj.defence} Health Points: {obj.health}")


def battle_loop(fieldlist, computerlist, computerhand, playerlist, playerhand):
    """ Cards battle and determine winner based on attack, defense, and health values """
    # fieldlist[0] - players card
    # fieldlist[1] - computers card
    if who_goes_first() == True:
        while len(fieldlist) == 2:
            if fieldlist[0].health > 0:
                player_damage = fieldlist[0].attack - fieldlist[1].defence
                fieldlist[1].health -= player_damage
                print(f"""
                Your {fieldlist[0].name} damaged the opponent's {fieldlist[1].name} for {player_damage} damage.
                The opponent's cards remaining health is {fieldlist[1].health}hp.
                """)
                time.sleep(1)

            else:
                print("Your card was destroyed!\n")
                fieldlist.pop(0)
                player_draw_cards(playerlist, playerhand)
                player_play_card(playerhand, fieldlist)
                battle_loop(fieldlist, computerlist,
                            computerhand, playerlist, playerhand)

            if fieldlist[1].health > 0:
                computer_damage = fieldlist[1].attack - fieldlist[0].defence
                fieldlist[0].health -= computer_damage
                print(f"""
                The opponent's {fieldlist[1].name} damaged your {fieldlist[0].name} for {computer_damage} damage.
                Your cards remaining health is {fieldlist[0].health}hp.
                """)
                time.sleep(1)

            else:
                print("The opponent's card was destroyed!\n")
                fieldlist.pop(1)
                computer_draw_cards(computerlist, computerhand)
                computer_play_card(computerhand, fieldlist)
                battle_loop(fieldlist, computerlist,
                            computerhand, playerlist, playerhand)
    else:
        while len(fieldlist) == 2:
            if fieldlist[1].health > 0:
                computer_damage = fieldlist[1].attack - \
                    fieldlist[0].defence
                fieldlist[0].health -= computer_damage
                print(f"""
                The opponent's {fieldlist[1].name} damaged your {fieldlist[0].name} for {computer_damage} damage.
                Your cards remaining health is {fieldlist[0].health}hp.
                """)
                time.sleep(1)

            else:
                print("The opponent's card was destroyed!")
                fieldlist.pop(1)
                computer_draw_cards(computerlist, computerhand)
                computer_play_card(computerhand, fieldlist)
                battle_loop(fieldlist, computerlist,
                            computerhand, playerlist, playerhand)

            if fieldlist[0].health > 0:
                player_damage = fieldlist[0].attack - fieldlist[1].defence
                fieldlist[1].health -= player_damage
                print(f"""
                Your {fieldlist[0].name} damaged the opponent's {fieldlist[1].name} for {player_damage} damage.
                The opponent's cards remaining health is {fieldlist[1].health}hp.
                """)
                time.sleep(1)

            else:
                print("Your card was destroyed!")
                fieldlist.pop(0)
                player_draw_cards(playerlist, playerhand)
                player_play_card(playerhand, fieldlist)
                battle_loop(fieldlist, computerlist,
                            computerhand, playerlist, playerhand)


# def show_cards(computerlist, computerhand, playerlist, playerhand, fieldlist):
#     """
#         TESTING PURPOSES ONLY
#         Display the list of cards for the user to see
#     """
#     print("computer deck")
#     for obj in computerlist:
#         print(
#             f"Name: {obj.name} Attack: {obj.attack} Defence Rating: {obj.defence} Health Points: {obj.health}\n")
#     print("computer hand")
#     for obj in computerhand:
#         print(
#             f"Name: {obj.name} Attack: {obj.attack} Defence Rating: {obj.defence} Health Points: {obj.health}\n")
#     print("player deck")
#     for obj in playerlist:
#         print(
#             f"Name: {obj.name} Attack: {obj.attack} Defence Rating: {obj.defence} Health Points: {obj.health}\n")
#     print("player hand")
#     for obj in playerhand:
#         print(
#             f"Name: {obj.name} Attack: {obj.attack} Defence Rating: {obj.defence} Health Points: {obj.health}\n")
#     print("Field list")
#     for obj in fieldlist:
#         print(
#             f"Name: {obj.name} Attack: {obj.attack} Defence Rating: {obj.defence} Health Points: {obj.health}\n")
