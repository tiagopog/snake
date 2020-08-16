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

    def reset_position(self):
        self.x = random.randint(0, self.MAX_X)
        self.y = random.randint(0, self.MAX_Y)

    def draw(self):
        arcade.create_rectangle_filled(
            center_x=self.x,
            center_y=self.y,
            width=self.BODY_WIDTH,
            height=self.BODY_HEIGHT,
            color=arcade.color.GREEN,
        ).draw()
