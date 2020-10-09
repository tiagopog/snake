import arcade

from source.game import Scene
from source.arena import Arena
from source.score import Score
from source.snake import Snake
from source.food import Food

GAME_OVER_TEXT = "GAME OVER!"


class MainScene(Scene):
    """
    Manipulates and draws all the game objects related to the game's main scene
    i.e. the snake character trying to get the food.
    """

    def setup(self, game, window):
        self.game = game
        self.window = window

        self.snake = Snake()
        self.arena = Arena(window=window)
        self.score = Score(window=window)
        self.food = Food(window=window)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.UP:
            self.snake.turn_up()
        elif key == arcade.key.DOWN:
            self.snake.turn_down()
        elif key == arcade.key.LEFT:
            self.snake.turn_left()
        elif key == arcade.key.RIGHT:
            self.snake.turn_right()

    def on_collision(self, obj):
        if isinstance(obj, Food):
            self.snake.grow()
            self.food.reset_position()
        else:
            self.game.set_game_over()

    def update(self, _delta_time):
        if self.game.over:
            return

        self.snake.move()
        self.game.check_collision_between(
            source=self.snake.head,
            targets=[self.food, *self.arena.borders, *self.snake.segments[5:]],
            on_collision=self.on_collision,
        )

    def on_key_release(self, key, modifiers):
        pass

    def draw(self):
        self.arena.draw()
        self.score.draw(score=self.game.score)
        self.food.draw()
        self.snake.draw()

        if self.game.over:
            arcade.draw_text(
                text=GAME_OVER_TEXT,
                start_x=self.window.width / 2 - 30,
                start_y=self.window.height / 2,
                color=arcade.color.WHITE,
            )
