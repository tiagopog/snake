# Snake

A Python implementation of the classic :snake: game.

**Note:** the low frame rate here is due to the GIF recording not the game itself.

![snake_demo_1](https://user-images.githubusercontent.com/760933/95654304-993aa000-0ad5-11eb-8bc7-b7bc9820eb5e.gif)

That's my first attempt on writing games in Python after implementing
some 2D games in Ruby like [Pong](https://github.com/tiagopog/pong)
and [Flappy Bird](https://github.com/tiagopog/flappy_bird).

Particullarly, in this game my goal was not only to experiment game development in Python
but also to wrap my head around how to start structuring scenes in 2D games which is something
I haven't done in other games so far.

# Installation

Install the awesome [Arcade](https://github.com/pythonarcade/arcade) library:

```
pip install arcade
```

Clone this repo:

```
git clone https://github.com/tiagopog/snake
```

Run the game:

```
python snake/main.py
```

Enjoy!

# TODOs

- [x] Implement the snake's movement mechanics;
- [x] Implement logic of the snake's food;
- [x] Implement collision detection + score system;
- [x] Grow the snake's body and speed when scoring;
- [x] Make sure the snake's movement mechanics work at any speed;
- [x] Create arena to limit where the snake can go;
- [X] Make sure the food doesn't appear over or beyond the arena's border;
- [X] Detect collision between the snake and the arena's borders;
- [X] Detect collision between the snake and its own body;
- [X] Implement game over;
- [ ] Implement game reset;
- [ ] Implement initial scene with the game control;
- [ ] Implement scoreboard scene with best scores;
- [ ] Generate a binary executable for the game.
