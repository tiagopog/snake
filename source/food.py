import arcade
import random

from .game import GameObject


class Food(GameObject):
    """
    TODO
    """

    BODY_WIDTH = 10
    BODY_HEIGHT = 10

    MAX_X = 800 - BODY_WIDTH
    MAX_Y = 600 - BODY_HEIGHT

    def __init__(self, range_x=None, range_y=None):
        super().__init__(width=self.BODY_WIDTH, height=self.BODY_HEIGHT)

        (min_x, max_x) = range_x or (0, self.MAX_X)
        self.range_x = (round(min_x), round(max_x))

        (min_y, max_y) = range_y or (0, self.MAX_Y)
        self.range_y = (round(min_y), round(max_y))

        self.reset_position()

    def reset_position(self):
        self.x = random.randint(*self.range_x)
        self.y = random.randint(*self.range_y)

    def draw(self):
        arcade.create_rectangle_filled(
            center_x=self.x,
            center_y=self.y,
            width=self.width,
            height=self.height,
            color=arcade.color.GREEN,
        ).draw()
