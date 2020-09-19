import arcade

from .game import GameObject

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

POSITIVE_DIRECTION = 1
NEGATIVE_DIRECTION = -1
NEUTRAL_DIRECTION = 0

START_DIRECTION_X = POSITIVE_DIRECTION
START_DIRECTION_Y = NEUTRAL_DIRECTION


class SnakeTurningPoint(GameObject):
    """
    TODO
    """

    BODY_WIDTH = 10
    BODY_HEIGHT = 10

    def __init__(self, x, y, direction):
        super().__init__(x, y, self.BODY_WIDTH, self.BODY_HEIGHT)
        self.direction = direction

    @property
    def data(self):
        return self.x, self.y, self.direction

    def draw(self):
        arcade.create_rectangle_filled(
            center_x=self.x,
            center_y=self.y,
            width=self.width,
            height=self.height,
            color=arcade.color.WHITE,
        ).draw()


class SnakeBodySegment(GameObject):
    """
    TODO
    """

    BODY_WIDTH = 10
    BODY_HEIGHT = 10

    def __init__(self, x, y, direction_x, direction_y, speed):
        super().__init__(x, y, self.BODY_WIDTH, self.BODY_HEIGHT)

        self.direction_x = direction_x
        self.direction_y = direction_y

        self.speed = speed
        self.turning_point = None
        self.previous = None
        self.next = None

    @property
    def is_moving_up(self):
        return (
            self.direction_x == NEUTRAL_DIRECTION
            and self.direction_y == POSITIVE_DIRECTION
        )

    @property
    def is_moving_down(self):
        return (
            self.direction_x == NEUTRAL_DIRECTION
            and self.direction_y == NEGATIVE_DIRECTION
        )

    @property
    def is_moving_left(self):
        return (
            self.direction_x == NEGATIVE_DIRECTION
            and self.direction_y == NEUTRAL_DIRECTION
        )

    @property
    def is_moving_right(self):
        return (
            self.direction_x == POSITIVE_DIRECTION
            and self.direction_y == NEUTRAL_DIRECTION
        )

    @property
    def is_moving_vertically(self):
        return self.direction_x == NEUTRAL_DIRECTION

    @property
    def is_moving_horizontally(self):
        return self.direction_y == NEUTRAL_DIRECTION

    @property
    def can_turn_direction(self):
        return not self.next or not self.next.turning_point

    def move(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed
        self.check_turning_point()

    def turn_up(self):
        self.turn(UP)

    def turn_down(self):
        self.turn(DOWN)

    def turn_left(self):
        self.turn(LEFT)

    def turn_right(self):
        self.turn(RIGHT)

    def turn(self, direction, propagate_turning_point=True):
        """
        TODO
        """
        if direction not in (UP, DOWN, LEFT, RIGHT) or not self.can_turn_direction:
            return

        turned = False

        if direction == UP and self.is_moving_horizontally:
            self.direction_x = NEUTRAL_DIRECTION
            self.direction_y = POSITIVE_DIRECTION
            turned = True
        elif direction == DOWN and self.is_moving_horizontally:
            self.direction_x = NEUTRAL_DIRECTION
            self.direction_y = NEGATIVE_DIRECTION
            turned = True
        elif direction == LEFT and self.is_moving_vertically:
            self.direction_x = NEGATIVE_DIRECTION
            self.direction_y = NEUTRAL_DIRECTION
            turned = True
        elif direction == RIGHT and self.is_moving_vertically:
            self.direction_x = POSITIVE_DIRECTION
            self.direction_y = NEUTRAL_DIRECTION
            turned = True

        if turned and propagate_turning_point:
            self.propagate_turning_point(direction)

    def propagate_turning_point(self, direction, x=None, y=None):
        """
        Set to next body segment a Cartensian coordinate where it will turn to
        given `direction`.
        """
        if not self.next:
            return

        x = x or self.x
        y = y or self.y
        self.next.turning_point = SnakeTurningPoint(x, y, direction)

    def grow(self):
        """
        TODO
        """
        self.next = SnakeBodySegment(
            x=self.x,
            y=self.y,
            direction_x=self.direction_x,
            direction_y=self.direction_y,
            speed=self.speed,
        )
        self.next.previous = self
        self.next.fix_segment_positions(self.x, self.y)

    def check_turning_point(self):
        """
        Make sure to change a body segment's direction if it has reached a
        turning point.
        """
        if self.turning_point is None:
            return

        target_x, target_y, target_direction = self.turning_point.data
        reached_x = self._has_reached_target_x
        reached_y = self._has_reached_target_y
        reached = reached_x(target_x, target_direction) or reached_y(
            target_y, target_direction
        )

        if not reached:
            return

        self.fix_segment_positions(target_x, target_y)
        self.turn(target_direction, propagate_turning_point=False)
        self.propagate_turning_point(target_direction, target_x, target_y)
        self.turning_point = None

    def fix_segment_positions(self, target_x, target_y):
        """
        TODO
        """
        if self.previous is None:
            return
        elif self.previous.is_moving_horizontally:
            direction = -1 * self.previous.direction_x
            self.x = self.previous.x + direction * self.BODY_WIDTH
            self.y = target_y
        else:
            direction = -1 * self.previous.direction_y
            self.y = self.previous.y + direction * self.BODY_HEIGHT
            self.x = target_x

    def draw(self):
        """
        TODO
        """
        arcade.create_rectangle_filled(
            center_x=self.x,
            center_y=self.y,
            width=self.width,
            height=self.height,
            color=arcade.color.WHITE,
        ).draw()

        if self.turning_point:
            self.turning_point.draw()

    def _has_reached_target_y(self, target_y, target_direction):
        return (
            target_direction in (LEFT, RIGHT)
            and self.is_moving_up
            and self.y >= target_y
            or self.is_moving_down
            and self.y <= target_y
        )

    def _has_reached_target_x(self, target_x, target_direction):
        return (
            target_direction in (UP, DOWN)
            and self.is_moving_right
            and self.x >= target_x
            or self.is_moving_left
            and self.x <= target_x
        )


class Snake:
    """
    TODO
    """

    START_SPEED = 3

    START_X = 400
    START_Y = 300

    def __init__(self):
        self.head = SnakeBodySegment(
            x=self.START_X,
            y=self.START_Y,
            speed=self.START_SPEED,
            direction_x=START_DIRECTION_X,
            direction_y=START_DIRECTION_Y,
        )
        self.tail = self.head
        self.grow()

    def grow(self):
        self.tail.grow()
        self.tail = self.tail.next

    def move(self):
        segment = self.head

        while segment:
            segment.move()
            segment = segment.next

    def turn_up(self):
        self.head.turn_up()

    def turn_down(self):
        self.head.turn_down()

    def turn_left(self):
        self.head.turn_left()

    def turn_right(self):
        self.head.turn_right()

    def draw(self):
        segment = self.head

        while segment:
            segment.draw()
            segment = segment.next
