import arcade

from source.game import Game
from source.scenes import MainScene

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Handle the initialization of the game's window and scenes.
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)
        self.game = Game()
        self.current_scene = MainScene()

    def setup(self):
        """
        Set up scenes objects.
        """
        self.current_scene.setup(game=self.game, window=self)

    def on_draw(self):
        """
        Render the scene screen.
        """
        arcade.start_render()
        self.current_scene.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed. Delegates the handling of such
        event to the current scene.
        """
        self.current_scene.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key. Delegates the handling of such
        event to the current scene.
        """
        self.current_scene.on_key_release(key, modifiers)

    def update(self, delta_time):
        """
        All the logic to run the game simulation goes here.
        """
        self.current_scene.update(delta_time)


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
