import arcade


class Arena:
    """
    TODO
    """

    PADDING = 30
    TOTAL_BORDER_WIDTH = 15
    BORDER_WIDTH = TOTAL_BORDER_WIDTH / 2

    def __init__(self):
        from main import SCREEN_WIDTH, SCREEN_HEIGHT

        self.width = SCREEN_WIDTH - self.TOTAL_BORDER_WIDTH
        self.height = SCREEN_HEIGHT - self.TOTAL_BORDER_WIDTH

        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

        self.min_x = self.BORDER_WIDTH + self.PADDING
        self.max_x = self.min_x + self.width - 2 * self.PADDING

        self.min_y = self.BORDER_WIDTH + self.PADDING
        self.max_y = self.min_y + self.height - 2 * self.PADDING

    @property
    def range_x(self):
        return (self.min_x, self.max_x)

    @property
    def range_y(self):
        return (self.min_y, self.max_y)

    def draw(self):
        arcade.create_rectangle_outline(
            width=self.width,
            height=self.height,
            center_x=self.x,
            center_y=self.y,
            border_width=self.TOTAL_BORDER_WIDTH,
            color=arcade.color.WHITE,
        ).draw()
