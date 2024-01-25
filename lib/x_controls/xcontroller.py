import random


def estimate_move(player_positions, neighbours):
    print("Lady X moving")
    # get neighbor nodes of actual position --> Muss in Main passieren
    # get position muss vorher passieren
    # check if occupied by players
    for point in neighbours:
        if point in player_positions:
            neighbours.remove(point)
    # random move
    print("Lady X moving")
    rnd_turn = random.randint(0, len(neighbours)-1)

    # publish move
    return neighbours[rnd_turn].position

