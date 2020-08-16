import arcade


class Score:
    """
    TODO
    """

    SCORE_TEXT = "Score: {}"

    def __init__(self):
        from main import SCREEN_WIDTH, SCREEN_HEIGHT

        self.x = SCREEN_WIDTH / 2 - 30
        self.y = SCREEN_HEIGHT - 30

    def draw(self, score):
        arcade.draw_text(
            text=self.SCORE_TEXT.format(score),
            start_x=self.x,
            start_y=self.y,
            color=arcade.color.BLACK,
        )
