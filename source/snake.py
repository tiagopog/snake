import arcade

START_SPEED = 3

START_X = 400
START_Y = 300

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

POSITIVE_DIRECTION = 1
NEGATIVE_DIRECTION = -1
NEUTRAL_DIRECTION = 0

START_DIRECTION_X = POSITIVE_DIRECTION
START_DIRECTION_Y = NEUTRAL_DIRECTION


class SnakeBodySegment:
    """
    TODO
    """

    BODY_WIDTH = 10
    BODY_HEIGHT = 10

    def __init__(self, x, y, direction_x, direction_y, speed):
        self.x = x
        self.y = y

        self.direction_x = direction_x
        self.direction_y = direction_y

        self.speed = speed
        self.turning_point = None
        self.previous = None
        self.next = None

    @property
    def width(self):
        return self.BODY_WIDTH

    @property
    def height(self):
        return self.BODY_HEIGHT

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
        self._check_turning_point()

    def turn_up(self):
        if self.is_moving_vertically or not self.can_turn_direction:
            return

        self.direction_x = NEUTRAL_DIRECTION
        self.direction_y = POSITIVE_DIRECTION
        self.propagate_turning_point(UP)

    def turn_down(self):
        if self.is_moving_vertically or not self.can_turn_direction:
            return

        self.direction_x = NEUTRAL_DIRECTION
        self.direction_y = NEGATIVE_DIRECTION
        self.propagate_turning_point(DOWN)

    def turn_left(self):
        if self.is_moving_horizontally or not self.can_turn_direction:
            return

        self.direction_x = NEGATIVE_DIRECTION
        self.direction_y = NEUTRAL_DIRECTION
        self.propagate_turning_point(LEFT)

    def turn_right(self):
        if self.is_moving_horizontally or not self.can_turn_direction:
            return

        self.direction_x = POSITIVE_DIRECTION
        self.direction_y = NEUTRAL_DIRECTION
        self.propagate_turning_point(RIGHT)

    def propagate_turning_point(self, direction):
        """
        Set to next body segment a Cartensian coordinate where it will turn to
        given `direction`.
        """
        if self.next:
            self.next.turning_point = (self.x, self.y, direction)

    def grow(self):
        self.next = SnakeBodySegment(
            x=START_X - SnakeBodySegment.BODY_HEIGHT,
            y=START_Y,
            direction_x=START_DIRECTION_X,
            direction_y=START_DIRECTION_Y,
            speed=START_SPEED,
        )
        self.next.previous = self

    def draw(self):
        arcade.create_rectangle_filled(
            center_x=self.x,
            center_y=self.y,
            width=self.BODY_WIDTH,
            height=self.BODY_HEIGHT,
            color=arcade.color.WHITE,
        ).draw()

    def _check_turning_point(self):
        """
        Make sure to change a body segment's direction if it has reached a
        turning point.
        """
        if self.turning_point is None:
            return

        target_x, target_y, target_direction = self.turning_point
        reached_x = self._has_reached_target_x
        reached_y = self._has_reached_target_y
        reached = reached_x(target_x, target_direction) or reached_y(
            target_y, target_direction
        )

        if not reached:
            return

        getattr(self, f"turn_{target_direction}")()
        self.turning_point = None
        self._fix_segment_positions(target_x, target_y)

    def _fix_segment_positions(self, target_x, target_y):
        """
        TODO
        """
        if self.is_moving_horizontally:
            direction = -1 * self.direction_x
            self.x = self.previous.x + direction * self.BODY_WIDTH
            self.y = target_y
        else:
            direction = -1 * self.direction_y
            self.y = self.previous.y + direction * self.BODY_HEIGHT
            self.x = target_x

    def _has_reached_target_y(self, target_y, target_direction):
        return (
            target_direction in ("left", "right")
            and self.is_moving_up
            and self.y >= target_y
            or self.is_moving_down
            and self.y <= target_y
        )

    def _has_reached_target_x(self, target_x, target_direction):
        return (
            target_direction in ("up", "down")
            and self.is_moving_right
            and self.x >= target_x
            or self.is_moving_left
            and self.x <= target_x
        )


class Snake:
    """
    TODO
    """

    def __init__(self):
        self.head = SnakeBodySegment(
            x=START_X,
            y=START_Y,
            direction_x=START_DIRECTION_X,
            direction_y=START_DIRECTION_Y,
            speed=START_SPEED,
        )
        self.tail = self.head
        # Mock (remove it later):
        self.grow()

    def grow(self):
        self.tail.grow()

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
