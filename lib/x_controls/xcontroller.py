import random


def estimate_move(player_positions, neighbours):
    # get position muss vorher passieren
    # check if occupied by players
    newNeighbours = []
    for n in neighbours:
        print("neighbour: " + str(n.position) + ": " + str(n.number))
    for point in neighbours:
        if point.position not in player_positions:
            newNeighbours.append(point)
            print("point number" + str(point.number) + " added")
    print(str(newNeighbours))
    for n in newNeighbours:
        print("neighour after deletion: "+str(n.position) + ": " + str(n.number))
    if len(newNeighbours) != 0:
        # random move
        rnd_turn = random.randint(0, len(newNeighbours) - 1)
        # publish move
        return newNeighbours[rnd_turn].position
    else:
        return False
