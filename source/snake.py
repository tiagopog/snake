import arcade

STARTING_SPEED = 2

STARTING_X = 400
STARTING_Y = 300

POSITIVE_DIRECTION = 1
NEGATIVE_DIRECTION = -1
NEUTRAL_DIRECTION = 0

STARTING_DIRECTION_X = POSITIVE_DIRECTION
STARTING_DIRECTION_Y = NEUTRAL_DIRECTION


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
        self.next = None

    @property
    def width(self):
        return self.BODY_WIDTH

    @property
    def height(self):
        return self.BODY_HEIGHT

    @property
    def is_going_up(self):
        return (
            self.direction_x == NEUTRAL_DIRECTION and
            self.direction_y == POSITIVE_DIRECTION
        )

    @property
    def is_going_down(self):
        return (
            self.direction_x == NEUTRAL_DIRECTION and
            self.direction_y == NEGATIVE_DIRECTION
        )

    @property
    def is_going_left(self):
        return (
            self.direction_x == NEGATIVE_DIRECTION and
            self.direction_y == NEUTRAL_DIRECTION
        )

    @property
    def is_going_right(self):
        return (
            self.direction_x == POSITIVE_DIRECTION and
            self.direction_y == NEUTRAL_DIRECTION
        )

    def move(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed
        self._check_turning_point()

    def turn_up(self):
        if self.is_going_down:
            return

        self.direction_x = NEUTRAL_DIRECTION
        self.direction_y = POSITIVE_DIRECTION
        self.propagate_turning_point('up')

    def turn_down(self):
        if self.is_going_up:
            return

        self.direction_x = NEUTRAL_DIRECTION
        self.direction_y = NEGATIVE_DIRECTION
        self.propagate_turning_point('down')

    def turn_left(self):
        if self.is_going_right:
            return

        self.direction_x = NEGATIVE_DIRECTION
        self.direction_y = NEUTRAL_DIRECTION
        self.propagate_turning_point('left')

    def turn_right(self):
        if self.is_going_left:
            return

        self.direction_x = POSITIVE_DIRECTION
        self.direction_y = NEUTRAL_DIRECTION
        self.propagate_turning_point('right')

    def propagate_turning_point(self, direction):
        if self.next:
            self.next.turning_point = (self.x, self.y, direction)

    def grow(self):
        self.next = SnakeBodySegment(
            STARTING_X - 10,
            STARTING_Y,
            STARTING_DIRECTION_X,
            STARTING_DIRECTION_Y,
            STARTING_SPEED
        )

    def draw(self):
        arcade.create_rectangle_filled(
            center_x=self.x,
            center_y=self.y,
            width=self.BODY_WIDTH,
            height=self.BODY_HEIGHT,
            color=arcade.color.WHITE
        ).draw()

    def _check_turning_point(self):
        if self.turning_point is None:
            return

        target_x, target_y, target_direction = self.turning_point
        reached_x = self._has_reached_target_x
        reached_y = self._has_reached_target_y

        if reached_x(target_x, target_direction) or reached_y(target_y, target_direction):
            getattr(self, f'turn_{target_direction}')()
            self.turning_point = None

    def _has_reached_target_y(self, target_y, target_direction):
        return (
            target_direction in ('left', 'right') and
            self.is_going_up and self.y >= target_y or
            self.is_going_down and self.y <= target_y
        )

    def _has_reached_target_x(self, target_x, target_direction):
        return (
            target_direction in ('up', 'down') and
            self.is_going_right and self.x >= target_x or
            self.is_going_left and self.x <= target_x
        )


class Snake:
    """
    TODO
    """

    def __init__(self):
        self.head = SnakeBodySegment(
            STARTING_X,
            STARTING_Y,
            STARTING_DIRECTION_X,
            STARTING_DIRECTION_Y,
            STARTING_SPEED
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
