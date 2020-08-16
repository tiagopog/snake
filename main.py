import arcade

from source.game import Game
from source.arena import Arena
from source.score import Score
from source.snake import Snake
from source.food import Food

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        TODO
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)
        self.debug = False

    def setup(self):
        """
        TODO
        """
        self.game = Game()
        self.arena = Arena()
        self.score = Score()
        self.snake = Snake()
        self.food = Food()

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        self.arena.draw()
        self.score.draw(score=self.game.score)
        self.food.draw()
        self.snake.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            self.snake.turn_up()
        elif key == arcade.key.DOWN:
            self.snake.turn_down()
        elif key == arcade.key.LEFT:
            self.snake.turn_left()
        elif key == arcade.key.RIGHT:
            self.snake.turn_right()
        elif key == arcade.key.D:
            self.debug = True

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        pass

    def on_collision(self):
        self.food.reset_position()
        self.snake.grow()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        self.check_debug()
        self.snake.move()
        self.game.check_collision_between(
            source=self.snake.head, target=self.food, on_collision=self.on_collision
        )

    def check_debug(self):
        """
        Just a simple debug helper.
        """
        if self.debug:
            pass
            # import pdb; pdb.set_trace()


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
