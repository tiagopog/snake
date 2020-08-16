import arcade

START_X = 10
START_Y = 570
SCORE_TEXT = "Score: {}"


class Score:
    """
    TODO
    """

    def __init__(self):
        self.x = START_X
        self.y = START_Y

    def draw(self, score):
        text = SCORE_TEXT.format(score)
        arcade.draw_text(
            text, start_x=START_X, start_y=START_Y, color=arcade.color.WHITE
        )
