import arcade

from .game import GameObject


class ArenaBorder(GameObject):
    """
    Represents a border in the game arena.
    """

    def draw(self):
        arcade.create_rectangle_filled(
            width=self.width,
            height=self.height,
            center_x=self.x,
            center_y=self.y,
            color=arcade.color.WHITE,
        ).draw()


class Arena(GameObject):
    """
    Defines the arena boundaries through the usage of `ArenaBorder` objects.
    """

    BORDER_SIZE = 15

    def __init__(self, window):
        super().__init__()

        self.width = window.width - 2 * self.BORDER_SIZE
        self.height = window.height - 2 * self.BORDER_SIZE

        self.left_border = ArenaBorder(
            x=self.BORDER_SIZE / 2,
            y=window.height / 2,
            width=self.BORDER_SIZE,
            height=window.height,
        )

        self.right_border = ArenaBorder(
            x=window.width - self.BORDER_SIZE / 2,
            y=window.height / 2,
            width=self.BORDER_SIZE,
            height=window.height,
        )

        self.top_border = ArenaBorder(
            x=window.width / 2,
            y=window.height - self.BORDER_SIZE / 2,
            width=window.width,
            height=self.BORDER_SIZE,
        )

        self.bottom_border = ArenaBorder(
            x=window.width / 2,
            y=self.BORDER_SIZE / 2,
            width=window.width,
            height=self.BORDER_SIZE,
        )

        self.borders = (
            self.left_border,
            self.right_border,
            self.top_border,
            self.bottom_border,
        )

    def draw(self):
        for border in self.borders:
            border.draw()
