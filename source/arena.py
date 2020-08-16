import arcade


class Arena:
    """
    TODO
    """

    START_X = 0
    START_Y = 0

    BORDER_WIDTH = 22

    def __init__(self):
        from main import SCREEN_WIDTH, SCREEN_HEIGHT

        self.width = SCREEN_WIDTH - 2 * self.BORDER_WIDTH
        self.height = SCREEN_HEIGHT - 2 * self.BORDER_WIDTH

        self.x = self.BORDER_WIDTH + self.START_X + self.width / 2
        self.y = self.BORDER_WIDTH + self.START_Y + self.height / 2

    def draw(self):
        arcade.create_rectangle_outline(
            width=self.width,
            height=self.height,
            center_x=self.x,
            center_y=self.y,
            border_width=self.BORDER_WIDTH,
            color=arcade.color.WHITE,
        ).draw()
