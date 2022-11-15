class Card:
    def __init__(self, name, attack, defence, health):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health


# Create Game Objects
villager = Card("Villager", 6, 2, 10)
barbarian = Card("Barbarian", 16, 1, 20)
knight = Card("Knight", 8, 5, 35)
archer = Card("Archer", 12, 2, 12)
wizard = Card("Wizard", 15, 1, 15)
goblin = Card("Goblin", 10, 3, 18)
orc = Card("Orc", 13, 4, 30)
siren = Card("Siren", 12, 2, 22)
fairy = Card("Fairy", 10, 5, 10)
yeti = Card("Yeti", 10, 4, 40)
troll = Card("Troll", 20, 1, 30)
vampire = Card("Vampire", 18, 1, 20)
werewolf = Card("Werewolf", 13, 3, 25)
zombie = Card("Zombie", 8, 2, 10)
centaur = Card("Centaur", 15, 3, 22)

ghost = Card("Ghost", 6, 2, 10)
banshee = Card("Banshee", 16, 1, 20)
hydra = Card("Hydra", 8, 5, 35)
chimera = Card("Chimera", 12, 2, 12)
bigfoot = Card("Bigfoot", 15, 1, 15)
dragon = Card("Dragon", 20, 1, 30)
unicorn = Card("Unicorn", 10, 3, 18)
basilisk = Card("Basilisk", 13, 4, 30)
phoenix = Card("Phoenix", 12, 2, 22)
griffin = Card("Griffin", 10, 5, 10)
lochness = Card("Loch Ness", 10, 4, 40)
fuans = Card("Fuans", 8, 2, 10)
minotaur = Card("Minotaur", 18, 1, 20)
scorpion = Card("Scorpion", 15, 3, 22)
gorgon = Card("Gorgon", 13, 3, 25)


player_deck_of_cards = [ghost, banshee, hydra, chimera, bigfoot, dragon, unicorn,
                        basilisk, phoenix, griffin, lochness, fuans, minotaur, scorpion, gorgon]

computer_deck_of_cards = [villager, barbarian, knight, archer, wizard, goblin,
                          orc, siren, fairy, yeti, troll, vampire, werewolf, zombie, centaur]
