from random import shuffle
from diceClass import Dices
from boardClass import


def monopoly(No_of_rolls):
    dices = Dices()
    squares = []
    doubles = 0
    turns = 0

    while len(squares) < 40:
        squares.append(0)

    while True:
        community_chest = [0, 1, 10, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]
        shuffle(community_chest)

        chance = [40, 40, 40, 40, 40, 40, 40, 40, 40, 39, 24, 15, 11, 10, 0, 'B']
        shuffle(chance)

        position = 0
        while turns < No_of_rolls:
            dice_values = dices.roll()
            d1, d2 = dice_values
            dice_total = d1 + d2

            if d1 == d2:
                doubles += 1
            else:
                doubles = 0
            if doubles >= 3:
                position = 10
            else:
                position = (position + dice_total) % 40
                if position in [7, 22, 36]:
                    chance_card = chance.pop(0)
                    chance.insert(len(chance), chance_card)

                    if chance_card != 40:
                        if isinstance(chance_card, int):
                            position = chance_card
                        elif chance_card == 'B':
                            position = position - 3

                elif position in [2, 17, 33]:  # Community Chest
                    chest_card = community_chest.pop(0)
                    community_chest.insert(len(community_chest), chest_card)

                    if chest_card != 40:
                        position = chest_card
            if position == 30:
                position = 10
            squares.insert(position, (squares.pop(position) + 1))
            turns += 1
            print(turns)
        return squares


my_int = 100000000
rep = monopoly(my_int)
probabilities = [x / my_int*100 for x in rep]

print(probabilities)
