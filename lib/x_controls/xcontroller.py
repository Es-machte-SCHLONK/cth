import random


def estimate_move(player_positions, neighbours):
    # get neighbor nodes of actual position --> Muss in Main passieren
    # get position muss vorher passieren
    # check if occupied by players
    for point in neighbours:
        if point in player_positions:
            neighbours.remove(point)
    if len(neighbours) != 0:
        # random move
        rnd_turn = random.randint(0, len(neighbours)-1)
        # publish move
        return neighbours[rnd_turn].position
    else:
        return False

