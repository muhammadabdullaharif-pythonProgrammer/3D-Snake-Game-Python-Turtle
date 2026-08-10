import turtle
import random
import time

# ============================================================
#                  3D STYLE SNAKE GAME
# ============================================================

# -----------------------------
# Game Variables
# -----------------------------
delay = 0.10
score = 0
highest_score = 0
game_running = True

bodies = []

# -----------------------------
# Screen
# -----------------------------
screen = turtle.Screen()
screen.title("🐍 3D Snake Game")
screen.bgcolor("#08111f")
screen.setup(width=1000, height=1000)
screen.tracer(0)

# -----------------------------
# Game Constants
# -----------------------------
WIDTH = 940
HEIGHT = 820
LIMIT_X = 460
LIMIT_Y = 390
STEP = 20

# ============================================================
#                    BACKGROUND
# ============================================================

# Outer border
border = turtle.Turtle()
border.speed(0)
border.penup()
border.hideturtle()
border.color("#00ffff")

border.goto(-470, -400)
border.pendown()

for _ in range(2):
    border.forward(940)
    border.left(90)
    border.forward(800)
    border.left(90)

border.penup()

# -----------------------------
# Grid
# -----------------------------
grid = turtle.Turtle()
grid.speed(0)
grid.penup()
grid.hideturtle()
grid.color("#132b43")

# Vertical grid
for x in range(-460, 461, 20):
    grid.goto(x, -390)
    grid.pendown()
    grid.goto(x, 390)
    grid.penup()

# Horizontal grid
for y in range(-390, 391, 20):
    grid.goto(-460, y)
    grid.pendown()
    grid.goto(460, y)
    grid.penup()

# ============================================================
#                       SCORE PANEL
# ============================================================

score_panel = turtle.Turtle()
score_panel.speed(0)
score_panel.penup()
score_panel.hideturtle()

score_panel.goto(0, 425)

score_panel.color("#00ffff")
score_panel.write(
    "🐍  3D SNAKE GAME  🐍",
    align="center",
    font=("Arial", 28, "bold")
)

# Score turtle
score_board = turtle.Turtle()
score_board.speed(0)
score_board.penup()
score_board.hideturtle()
score_board.color("white")


def update_score():
    score_board.clear()

    score_board.goto(0, 395)

    score_board.write(
        f"Score: {score}     |     Best: {highest_score}",
        align="center",
        font=("Arial", 18, "bold")
    )


update_score()

# ============================================================
#                     SNAKE HEAD SHADOW
# ============================================================

head_shadow = turtle.Turtle()
head_shadow.speed(0)
head_shadow.shape("circle")
head_shadow.color("#02060a")
head_shadow.shapesize(1.15, 1.15)
head_shadow.penup()
head_shadow.goto(4, -4)

# ============================================================
#                       SNAKE HEAD
# ============================================================

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#00ff99")
head.shapesize(1.0, 1.0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ============================================================
#                     SNAKE EYES
# ============================================================

left_eye = turtle.Turtle()
left_eye.speed(0)
left_eye.shape("circle")
left_eye.color("white")
left_eye.shapesize(0.18, 0.18)
left_eye.penup()

right_eye = turtle.Turtle()
right_eye.speed(0)
right_eye.shape("circle")
right_eye.color("white")
right_eye.shapesize(0.18, 0.18)
right_eye.penup()

left_pupil = turtle.Turtle()
left_pupil.speed(0)
left_pupil.shape("circle")
left_pupil.color("black")
left_pupil.shapesize(0.08, 0.08)
left_pupil.penup()

right_pupil = turtle.Turtle()
right_pupil.speed(0)
right_pupil.shape("circle")
right_pupil.color("black")
right_pupil.shapesize(0.08, 0.08)
right_pupil.penup()

# ============================================================
#                    FOOD SHADOW
# ============================================================

food_shadow = turtle.Turtle()
food_shadow.speed(0)
food_shadow.shape("circle")
food_shadow.color("#220000")
food_shadow.shapesize(0.85, 0.85)
food_shadow.penup()

# ============================================================
#                         FOOD
# ============================================================

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#ff1744")
food.shapesize(0.75, 0.75)
food.penup()


def place_food():
    x = random.randrange(-440, 441, STEP)
    y = random.randrange(-370, 371, STEP)

    food.goto(x, y)
    food_shadow.goto(x + 5, y - 5)


place_food()

# ============================================================
#                    MOVEMENT FUNCTIONS
# ============================================================

def move_up():
    if head.direction != "down":
        head.direction = "up"


def move_down():
    if head.direction != "up":
        head.direction = "down"


def move_left():
    if head.direction != "right":
        head.direction = "left"


def move_right():
    if head.direction != "left":
        head.direction = "right"


def stop_snake():
    head.direction = "stop"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + STEP)

    elif head.direction == "down":
        head.sety(head.ycor() - STEP)

    elif head.direction == "left":
        head.setx(head.xcor() - STEP)

    elif head.direction == "right":
        head.setx(head.xcor() + STEP)


# ============================================================
#                   KEYBOARD CONTROLS
# ============================================================

screen.listen()

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(stop_snake, "space")

# WASD controls
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

# ============================================================
#                  UPDATE HEAD DESIGN
# ============================================================

def update_head_design():

    # Shadow
    head_shadow.goto(
        head.xcor() + 5,
        head.ycor() - 5
    )

    # Eyes based on direction
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        left_eye.goto(x - 6, y + 8)
        right_eye.goto(x + 6, y + 8)

    elif head.direction == "down":
        left_eye.goto(x - 6, y - 8)
        right_eye.goto(x + 6, y - 8)

    elif head.direction == "left":
        left_eye.goto(x - 8, y + 6)
        right_eye.goto(x - 8, y - 6)

    elif head.direction == "right":
        left_eye.goto(x + 8, y + 6)
        right_eye.goto(x + 8, y - 6)

    else:
        left_eye.goto(x - 6, y + 7)
        right_eye.goto(x + 6, y + 7)

    # Pupils
    left_pupil.goto(left_eye.xcor(), left_eye.ycor())
    right_pupil.goto(right_eye.xcor(), right_eye.ycor())


# ============================================================
#                     CREATE BODY
# ============================================================

def create_body():

    body_shadow = turtle.Turtle()
    body_shadow.speed(0)
    body_shadow.shape("circle")
    body_shadow.color("#02070a")
    body_shadow.shapesize(0.9, 0.9)
    body_shadow.penup()

    body = turtle.Turtle()
    body.speed(0)
    body.shape("circle")
    body.color("#00cc88")
    body.shapesize(0.8, 0.8)
    body.penup()

    # Store body + shadow
    body.shadow = body_shadow

    bodies.append(body)


# ============================================================
#                  MOVE BODY
# ============================================================

def move_body():

    # Move body from last to first
    for index in range(len(bodies) - 1, 0, -1):

        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()

        bodies[index].goto(x, y)

    # First body follows head
    if len(bodies) > 0:

        bodies[0].goto(
            head.xcor(),
            head.ycor()
        )

    # Update shadows
    for body in bodies:

        body.shadow.goto(
            body.xcor() + 5,
            body.ycor() - 5
        )


# ============================================================
#                    BORDER COLLISION
# ============================================================

def check_border_collision():

    if head.xcor() > LIMIT_X:
        return True

    if head.xcor() < -LIMIT_X:
        return True

    if head.ycor() > LIMIT_Y:
        return True

    if head.ycor() < -LIMIT_Y:
        return True

    return False


# ============================================================
#                     FOOD COLLISION
# ============================================================

def check_food_collision():

    global score
    global highest_score
    global delay

    if head.distance(food) < 25:

        # New food position
        place_food()

        # Create body
        create_body()

        # Increase score
        score += 10

        # Highest score
        if score > highest_score:
            highest_score = score

        # Increase speed
        if delay > 0.035:
            delay -= 0.004

        update_score()


# ============================================================
#                 BODY COLLISION
# ============================================================

def check_body_collision():

    for body in bodies:

        if body.distance(head) < 15:
            return True

    return False


# ============================================================
#                      GAME OVER
# ============================================================

game_over_text = turtle.Turtle()
game_over_text.speed(0)
game_over_text.penup()
game_over_text.hideturtle()
game_over_text.color("#ff1744")


def show_game_over():

    game_over_text.clear()

    game_over_text.goto(0, 60)

    game_over_text.write(
        "GAME OVER!",
        align="center",
        font=("Arial", 42, "bold")
    )

    game_over_text.goto(0, 5)

    game_over_text.color("white")

    game_over_text.write(
        f"Final Score: {score}",
        align="center",
        font=("Arial", 22, "bold")
    )

    game_over_text.goto(0, -45)

    game_over_text.write(
        "Press SPACE to restart",
        align="center",
        font=("Arial", 18, "normal")
    )


# ============================================================
#                    RESTART GAME
# ============================================================

def restart_game():

    global score
    global delay
    global game_running

    if game_running:
        return

    # Remove old bodies
    for body in bodies:

        body.hideturtle()
        body.shadow.hideturtle()

    bodies.clear()

    # Reset snake
    head.goto(0, 0)
    head.direction = "stop"

    head_shadow.goto(5, -5)

    # Reset score
    score = 0
    delay = 0.10

    # New food
    place_food()

    # Clear game over
    game_over_text.clear()
    game_over_text.color("#ff1744")

    update_score()

    game_running = True


screen.onkey(restart_game, "space")

# ============================================================
#                       MAIN GAME LOOP
# ============================================================

while True:

    screen.update()

    # -----------------------------
    # Game Running
    # -----------------------------
    if game_running:

        # Move body BEFORE head
        move_body()

        # Move head
        move()

        # Update head graphics
        update_head_design()

        # Food collision
        check_food_collision()

        # Border collision
        if check_border_collision():

            game_running = False
            show_game_over()

        # Body collision
        elif check_body_collision():

            game_running = False
            show_game_over()

    # Game speed
    time.sleep(delay)

# Keep window open
screen.mainloop()
