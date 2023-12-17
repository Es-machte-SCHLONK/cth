import random
from random import randrange, choice
import datetime

from cth.lib import nodes as nd
import pygame as pyg


class Mapgenerator:
    now = float(datetime.datetime.now().timestamp())
    random.seed(now)
    nodeList = []

    def __init__(self, total_node_count):
        return 0




