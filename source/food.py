import arcade
import random

BODY_WIDTH = 10
BODY_HEIGHT = 10

MAX_X = 800 - BODY_WIDTH
MAX_Y = 600 - BODY_HEIGHT


class Food:
    """
    TODO
    """

    def __init__(self):
        self.reset_position()

    @property
    def width(self):
        return BODY_WIDTH

    @property
    def height(self):
        return BODY_HEIGHT

    def reset_position(self):
        self.x = random.randint(0, MAX_X)
        self.y = random.randint(0, MAX_Y)

    def draw(self):
        arcade.create_rectangle_filled(
            center_x=self.x,
            center_y=self.y,
            width=BODY_WIDTH,
            height=BODY_HEIGHT,
            color=arcade.color.GREEN
        ).draw()
