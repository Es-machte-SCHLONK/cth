
class Node(object):
    yellow = True
    green = False
    red = False
    black = False
    id = 0
    connected = []
    node_size_xy = 15

    def __init__(self, no, yellow, green, red, black):
        self.id = int(no)
        self.yellow = bool(yellow)
        self.green = bool(green)
        self.red = bool(red)
        self.black = bool(black)


