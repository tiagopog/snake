import arcade

STARTING_SPEED = 1

STARTING_X = 400
STARTING_Y = 300

POSITIVE_DIRECTION = 1
NEGATIVE_DIRECTION = -1
NEUTRAL_DIRECTION = 0

STARTING_DIRECTION_X = POSITIVE_DIRECTION
STARTING_DIRECTION_Y = NEUTRAL_DIRECTION


class SnakeBodySegment:
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

    def grow(self):
        self.next = SnakeBodySegment(
            STARTING_X - 10,
            STARTING_Y,
            STARTING_DIRECTION_X,
            STARTING_DIRECTION_Y,
            STARTING_SPEED
        )

    def move(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed
        self.check_turning_point()

    def turn_up(self):
        self.direction_x = NEUTRAL_DIRECTION
        self.direction_y = POSITIVE_DIRECTION

    def turn_down(self):
        self.direction_x = NEUTRAL_DIRECTION
        self.direction_y = NEGATIVE_DIRECTION

    def turn_left(self):
        self.direction_x = NEGATIVE_DIRECTION
        self.direction_y = NEUTRAL_DIRECTION

    def turn_right(self):
        self.direction_x = POSITIVE_DIRECTION
        self.direction_y = NEUTRAL_DIRECTION

    def check_turning_point(self):
        if self.turning_point is None:
            return

        x, y, direction = self.turning_point

        if direction == 'up' and self.y >= y:
            self.turn_up()
            self.propagate_turning_point('up')
            self.turning_point = None

    def propagate_turning_point(self, direction):
        if self.next:
            self.next.turning_point = (self.x, self.y, direction)

    def draw(self):
        arcade.create_rectangle_filled(
            center_x=self.x,
            center_y=self.y,
            width=self.BODY_WIDTH,
            height=self.BODY_HEIGHT,
            color=arcade.color.WHITE
        ).draw()


class Snake:
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
        self.head.propagate_turning_point('up')

    def turn_down(self):
        self.head.turn_down()
        self.head.propagate_turning_point('down')

    def turn_left(self):
        self.head.turn_left()
        self.head.propagate_turning_point('left')

    def turn_right(self):
        self.head.turn_right()
        self.head.propagate_turning_point('right')

    def draw(self):
        segment = self.head

        while segment:
            segment.draw()
            segment = segment.next
