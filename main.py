import arcade

from source import game
from source.snake import Snake
from source.food import Food

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.snake = None
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.snake = Snake()
        self.food = Food()

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        self.snake.draw()
        self.food.draw()

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

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        # pass
        # if key == arcade.key.UP:
        #     self.snake.change_y = 0


    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        self.snake.move()
        if game.has_collision_between(self.snake.head, self.food):
            print("Snake has eaten the food!")


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
