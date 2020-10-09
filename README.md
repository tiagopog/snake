# Snake

A Python implementation of the classic :snake: game.

**Note:** the low frame rate here is due to the GIF recording not the game itself.

![python_snake_game](https://user-images.githubusercontent.com/760933/95542853-4fff2900-09cd-11eb-804f-6e805fc561c7.gif)

That's my first attempt on writing games in Python after releasing
some 2D games in Ruby like [Pong](https://github.com/tiagopog/pong)
and [Flappy Bird](https://github.com/tiagopog/flappy_bird).

As I did in the previous games I tried to use as little as possible
the tools available in the game framework I'm using (i.e. [Arcade](https://github.com/pythonarcade/arcade))
in favor of keep learning and forming a strong foundation in game development basics.
Particullarly, in this game my goal was not only experiment game development in Python
but also to to wrap my head around how to structure scenes in 2D games which is something
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

- [x] Implement the basics for the snake's mechanics;
- [x] Implement the logic for the snake's food;
- [x] Implement collision detection + score system;
- [x] Grow the snake's body and speed when scoring;
- [x] Make sure the snake's movement mechanics work at any speed;
- [x] Create arena to limit where the snake can go;
- [X] Make sure the food doesn't appear over or beyond the arena's border;
- [X] Detect collision between the snake and the arena's boundaries;
- [X] Detect collision between the snake and its own body;
- [X] Implement game over scene;
- [ ] Implement game reset;
- [ ] Implement scoreboard with best scores.
- [ ] Generate a binary executable for the game.
