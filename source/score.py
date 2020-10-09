import arcade

from .game import GameObject


class Score(GameObject):
    """
    Represents the game score presented at screen's upper border.
    """

    SCORE_TEXT = "SCORE: {}"

    def __init__(self, window):
        x = window.width / 2 - 30
        y = window.height - 16
        super().__init__(x, y)

    def draw(self, score):
        arcade.draw_text(
            text=self.SCORE_TEXT.format(score),
            start_x=self.x,
            start_y=self.y,
            color=arcade.color.BLACK,
        )
