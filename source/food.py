import arcade
import random


class Food:
    """
    TODO
    """

    BODY_WIDTH = 10
    BODY_HEIGHT = 10

    MAX_X = 800 - BODY_WIDTH
    MAX_Y = 600 - BODY_HEIGHT

    def __init__(self):
        self.reset_position()

    @property
    def width(self):
        return self.BODY_WIDTH

    @property
    def height(self):
        return self.BODY_HEIGHT

    def reset_position(self, range_x=None, range_y=None):
        range_x = range_x or (0, self.MAX_X)
        range_x = map(lambda e: round(e), range_x)

        range_y = range_y or (0, self.MAX_Y)
        range_y = map(lambda e: round(e), range_y)

        self.x = random.randint(*range_x)
        self.y = random.randint(*range_y)

    def draw(self):
        arcade.create_rectangle_filled(
            center_x=self.x,
            center_y=self.y,
            width=self.BODY_WIDTH,
            height=self.BODY_HEIGHT,
            color=arcade.color.GREEN,
        ).draw()
