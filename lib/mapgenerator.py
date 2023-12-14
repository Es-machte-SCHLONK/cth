import random
import datetime
from Nodes import Node


class Mapgenerator:
    now = float(datetime.datetime.now().timestamp())
    random.seed()
    totalNodeCount = 0
    greenNodeCount = 0
    redNodeCount = 0
    blackNodeCount = 0
    randomInt = 0
    nodeList = []

    # Additional Information, based on official Scotland Yard lib:
    #   every 3.333 nodes, a GREEN node.    >> 30 per 100  >> 300 per 1000
    #   every 13.333 nodes, a RED node.     >> 7,5 per 100 >> 75 per 1000
    #   every 40 nodes, a BLACK node.       >> 2,5 per 100 >> 25 per 1000
    #   Every RED node is also GREEN and YELLOW node.
    #   Black nodes are special.
    def __init__(self, total_node_count):
        now = float(datetime.datetime.now().timestamp())
        random.seed(now)
        self.totalNodeCount = int(total_node_count)
        # Statistical distribution of green, red and black nodes.
        for i in range(total_node_count):

            self.randomInt = random.randint(1, 1000)
            if self.randomInt <= 75:
                green = True
                red = True
                self.greenNodeCount += 1
                self.redNodeCount += 1
            elif self.randomInt <= 300:
                green = True
                red = False
                self.greenNodeCount += 1
            else:
                green = False
                red = False

            if random.randint(1, 1000) <= 25:
                black = True
                self.blackNodeCount += 1
            else:
                black = False

            new_node = Node(i, True, green, red, black)
            self.nodeList.append(new_node)

    def print_nodes(self):
        print("Node Nr.\t\tYellow\tGreen\tRed \tBlack")
        for node in self.nodeList:
            print(
                str(node.id) + "\t\t\t\t" +
                str(node.yellow) + "\t" +
                str(node.green) + "\t" +
                str(node.red) + " \t" +
                str(node.black)
            )
        print(
            "\nGesamt:\t\t\t" +
            str(self.totalNodeCount) + "\n\tYellow:\t\t" +
            str(self.greenNodeCount) + "\n\tGreen:\t\t" +
            str(self.redNodeCount) + "\n\tBlack:\t\t" +
            str(self.blackNodeCount)
        )


my_map = Mapgenerator(200)
my_map.print_nodes()