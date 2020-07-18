

class Game:
    """
    TODO
    """

    def __init__(self):
        self.score = 0
        self.in_collision_debounce = False

    def increase_score(self):
        """
        TODO
        """
        self.score += 1

    def toggle_collision_debounce(self):
        """
        TODO
        """
        self.in_collision_debounce = not self.in_collision_debounce

    def check_collision_between(self, source, target):
        """
        TODO
        """
        in_debounce = self.in_collision_debounce

        if in_debounce and not self.has_collision_between(source, target):
            self.toggle_collision_debounce()
        elif not in_debounce and self.has_collision_between(source, target):
            self.toggle_collision_debounce()
            self.increase_score()
            print(self.score)

    def has_collision_between(self, source, target):
        """
        Helper function to check the overlap between rectangular areas.
        """
        return (
            source.y >= target.y - target.height and
            source.y - source.height <= target.y and
            source.x + source.width >= target.x and
            source.x <= target.x + target.width
        )

