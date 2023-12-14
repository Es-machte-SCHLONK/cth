class Node:
    yellow = True
    green = False
    red = False
    black = False
    id = 0

    def __init__(self, no, yellow, green, red):
        self.id = int(no)
        self.yellow = bool(yellow)
        self.green = bool(green)
        self.red = bool(red)
        self.black = False

    def __init__(self, no, yellow, green, red, black):
        self.id = int(no)
        self.yellow = bool(yellow)
        self.green = bool(green)
        self.red = bool(red)
        self.black = bool(black)