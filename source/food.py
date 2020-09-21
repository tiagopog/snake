import arcade
import random

from .game import GameObject
from .arena import Arena


class Food(GameObject):
    """
    TODO
    """

    BODY_SIZE = 10

    def __init__(self, parent):
        super().__init__(width=self.BODY_SIZE, height=self.BODY_SIZE)
        self.min_x = Arena.BORDER_SIZE + self.BODY_SIZE / 2
        self.max_x = parent.width - Arena.BORDER_SIZE - self.BODY_SIZE / 2

        self.min_y = Arena.BORDER_SIZE + self.BODY_SIZE / 2
        self.max_y = parent.height - Arena.BORDER_SIZE - self.BODY_SIZE / 2

        self.reset_position()

    def reset_position(self):
        self.x = random.randint(self.min_x, self.max_x)
        self.y = random.randint(self.min_y, self.max_y)

    def draw(self):
        arcade.create_rectangle_filled(
            center_x=self.x,
            center_y=self.y,
            width=self.width,
            height=self.height,
            color=arcade.color.GREEN,
        ).draw()
