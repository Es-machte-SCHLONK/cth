
class Node:

    def __init__(self, id, green, red):
        self.id = int(id)
        self.yellow = True
        self.green = bool(green)
        self.red = bool(red)
        self.black = False
        self.node_size = 15

    def set_black(self):
        self.black = True

    def __str__(self):
        return (
            f"Node {str(self.id)}\n"
            f"\tY:  {str(self.yellow)}\n"
            f"\tG:  {str(self.green)}\n"
            f"\tR:  {str(self.red)}\n"
            f"\tB:  {str(self.black)}\n"
            f"\txy:  {str(self.node_size)}"
        )
