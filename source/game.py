class BaseShape:
    """
    Base definition for shapes in the game.
    """

    def __init__(self, x=None, y=None, width=None, height=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class GameObject(BaseShape):
    """
    Defines the base data and API for drawable game objects.
    """

    def draw(self):
        raise NotImplementedError


class BoundingBox(BaseShape):
    """
    Invisble boxes to map trickier collision areas on game objects.
    """

    pass


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
                source.x + source.width >= target.x
                and source.x <= target.x + target.width
            )
            overlap_y = (
                source.y >= target.y - target.height
                and source.y - source.height <= target.y
            )

            if overlap_x and overlap_y:
                result = (True, target)
                break

        return result
