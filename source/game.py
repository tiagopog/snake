class BoundingBox:
    """
    Base definition for delimiting things that can be placed in the
    game's Cartesian plane.
    """

    def __init__(self, x=None, y=None, width=None, height=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def center_x(self):
        return self.x

    @property
    def center_y(self):
        return self.y

    @property
    def left_x(self):
        return self.x - self.width / 2

    @property
    def right_x(self):
        return self.x + self.width / 2

    @property
    def top_y(self):
        return self.y + self.height / 2

    @property
    def bottom_y(self):
        return self.y - self.height / 2


class GameObject(BoundingBox):
    """
    Defines the base data and API for drawable game objects.
    """

    def draw(self):
        raise NotImplementedError


class Scene:
    """
    Abstract class to define the main public API for the game scenes.
    """

    def setup(self):
        """
        Initial setup of the scene's objects.
        """
        raise NotImplementedError

    def draw(self):
        """
        Render the scene screen.
        """
        raise NotImplementedError

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        raise NotImplementedError

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        raise NotImplementedError

    def update(self, delta_time):
        """
        All the logic to run the game simulation goes here.
        """
        raise NotImplementedError


class Game:
    """
    TODO
    """

    def __init__(self):
        self.score = 0

    def increase_score(self):
        """
        TODO
        """
        self.score += 1

    def check_collision_between(self, source, targets, on_collision):
        """
        TODO
        """
        has_collision, obj = self.has_collision_between(source, targets)

        if has_collision:
            self.increase_score()
            on_collision(obj)

    def has_collision_between(self, source, targets):
        """
        Helper function to check the overlap between rectangular areas.
        """
        result = (False, None)

        for target in targets:
            overlap_x = (
                source.left_x <= target.right_x and source.right_x >= target.left_x
            )
            overlap_y = (
                source.top_y >= target.bottom_y and source.bottom_y <= target.top_y
            )

            if overlap_x and overlap_y:
                result = (True, target)
                break

        return result
