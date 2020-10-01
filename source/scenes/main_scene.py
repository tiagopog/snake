import arcade

from source.game import Game, Scene
from source.arena import Arena
from source.score import Score
from source.snake import Snake
from source.food import Food


class MainScene(Scene):
    def setup(self, parent):
        self.game = Game()
        self.snake = Snake()
        self.arena = Arena(parent=parent)
        self.score = Score(parent=parent)
        self.food = Food(parent=parent)

    def draw(self):
        self.arena.draw()
        self.score.draw(score=self.game.score)
        self.food.draw()
        self.snake.draw()

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
        """
        Called when the snake collides against other `obj` in the game.
        """
        if isinstance(obj, Food):
            self.snake.grow()
            self.food.reset_position()
        else:
            raise "Gave over!"

    def update(self, _delta_time):
        self.snake.move()
        self.game.check_collision_between(
            source=self.snake.head,
            targets=[self.food, *self.arena.borders, *self.snake.segments[5:]],
            on_collision=self.on_collision,
        )

    def on_key_release(self, key, modifiers):
        pass
