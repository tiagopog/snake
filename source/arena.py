import arcade

from .game import GameObject


class ArenaBorder(GameObject):
    """
    TODO
    """

    def draw(self):
        arcade.create_rectangle_filled(
            width=self.width,
            height=self.height,
            center_x=self.x,
            center_y=self.y,
            color=arcade.color.GRAY,
        ).draw()


class Arena(GameObject):
    """
    TODO
    """

    BORDER_SIZE = 15

    def __init__(self, parent):
        super().__init__()

        self.width = parent.width - 2 * self.BORDER_SIZE
        self.height = parent.height - 2 * self.BORDER_SIZE

        self.left_border = ArenaBorder(
            x=self.BORDER_SIZE / 2,
            y=parent.height / 2,
            width=self.BORDER_SIZE,
            height=parent.height,
        )

        self.right_border = ArenaBorder(
            x=parent.width - self.BORDER_SIZE / 2,
            y=parent.height / 2,
            width=self.BORDER_SIZE,
            height=parent.height,
        )

        self.top_border = ArenaBorder(
            x=parent.width / 2,
            y=parent.height - self.BORDER_SIZE / 2,
            width=parent.width,
            height=self.BORDER_SIZE,
        )

        self.bottom_border = ArenaBorder(
            x=parent.width / 2,
            y=self.BORDER_SIZE / 2,
            width=parent.width,
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
