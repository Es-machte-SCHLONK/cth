import random


def estimate_move(player_positions, neighbours):
    # get neighbor nodes of actual position --> Muss in Main passieren
    # get position muss vorher passieren
    # check if occupied by players
    for n in neighbours:
        print("neighbour: " + str(n.position) + ": " + str(n.number))
    for point in neighbours:
        print(point.position)
        if point.position in player_positions:
            neighbours.remove(point)
    for n in neighbours:
        print("neighour after deletion: "+str(n.position) + ": " + str(n.number))
    if len(neighbours) != 0:
        # random move
        rnd_turn = random.randint(0, len(neighbours) - 1)
        # publish move
        return neighbours[rnd_turn].position
    else:
        return False
