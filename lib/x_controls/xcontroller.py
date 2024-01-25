import random


def estimate_move(player_positions, neighbor):
    # get neighbor nodes of actual position --> Muss in Main passieren
    # get position muss vorher passieren
    # check if occupied by players
    for point in neighbor:
        if point in player_positions:
            neighbor.remove(point)
    # random move
    rnd_turn = random.randint(0, len(neighbor))

    # publish move
    return neighbor[rnd_turn]

