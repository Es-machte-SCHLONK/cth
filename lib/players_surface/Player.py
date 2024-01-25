# class for Player Information
import pygame as pyg


class Player:
    def __init__(self, name, color=(255, 255, 255)):
        self._name = name
        self._color = color
        self._current_position = 0
        self._yellow = 10
        self._green = 5
        self._red = 3
        self._on_turn = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, value):
        self._green = value

    @property
    def current_position(self):
        return self._current_position

    @current_position.setter
    def current_position(self, value):
        self._current_position = value

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        self._red = value

    @property
    def yellow(self):
        return self._yellow

    @yellow.setter
    def yellow(self, value):
        self._yellow = value

    @property
    def on_turn(self):
        return self._on_turn

    @on_turn.setter
    def on_turn(self, is_on_turn):
        self._on_turn = is_on_turn
