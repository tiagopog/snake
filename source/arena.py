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

    def __init__(self, screen_width, screen_height):
        super().__init__()

        self.width = screen_width - 2 * self.BORDER_SIZE
        self.height = screen_height - 2 * self.BORDER_SIZE

        self.left_border = ArenaBorder(
            x=self.BORDER_SIZE / 2,
            y=screen_height / 2,
            width=self.BORDER_SIZE,
            height=screen_height,
        )

        self.right_border = ArenaBorder(
            x=screen_width - self.BORDER_SIZE / 2,
            y=screen_height / 2,
            width=self.BORDER_SIZE,
            height=screen_height,
        )

        self.top_border = ArenaBorder(
            x=screen_width / 2,
            y=screen_height - self.BORDER_SIZE / 2,
            width=screen_width,
            height=self.BORDER_SIZE,
        )

        self.bottom_border = ArenaBorder(
            x=screen_width / 2,
            y=self.BORDER_SIZE / 2,
            width=screen_width,
            height=self.BORDER_SIZE,
        )

        self.borders = (
            self.left_border,
            self.right_border,
            self.top_border,
            self.bottom_border,
        )

        self.min_x = self.left_border.right_x
        self.max_x = self.right_border.left_x

        self.min_y = self.bottom_border.top_y
        self.max_y = self.top_border.bottom_y

    @property
    def range_x(self):
        return (self.min_x, self.max_x)

    @property
    def range_y(self):
        return (self.min_y, self.max_y)

    def draw(self):
        for border in self.borders:
            border.draw()
