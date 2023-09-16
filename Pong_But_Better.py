import pygame
import random

pygame.init()

# INITIALS
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
DIRECTION = [-1, 1]
ANGLE = [(1, 2), (1, 1), (2, 1)]

# COLORS
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# BALL INIT
RADIUS = 15
BALL_X = WIDTH / 2 - RADIUS
BALL_Y = HEIGHT / 2 - RADIUS
DEFAULT_BALL_VELOCITY = 0.08
BALL_VELOCITY_X = DEFAULT_BALL_VELOCITY
BALL_VELOCITY_Y = DEFAULT_BALL_VELOCITY

# PADDLES INIT
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 120
PADDLE_VELOCITY_UP = -0.15
PADDLE_VELOCITY_DOWN = 0.15
LEFT_PADDLE_X = 100 - PADDLE_WIDTH / 2
LEFT_PADDLE_Y = HEIGHT / 2 - PADDLE_HEIGHT / 2
RIGHT_PADDLE_X = WIDTH - LEFT_PADDLE_X
RIGHT_PADDLE_Y = LEFT_PADDLE_Y
LEFT_PADDLE_VELOCITY = 0
RIGHT_PADDLE_VELOCITY = LEFT_PADDLE_VELOCITY

# MAIN LOOP
run = True
while run:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # Right Player - Up and Down keys
            if event.key == pygame.K_UP:
                RIGHT_PADDLE_VELOCITY = PADDLE_VELOCITY_UP
            if event.key == pygame.K_DOWN:
                RIGHT_PADDLE_VELOCITY = PADDLE_VELOCITY_DOWN

            # Left Player - W and S keys
            if event.key == pygame.K_w:
                LEFT_PADDLE_VELOCITY = PADDLE_VELOCITY_UP
            if event.key == pygame.K_s:
                LEFT_PADDLE_VELOCITY = PADDLE_VELOCITY_DOWN

        if event.type == pygame.KEYUP:
            LEFT_PADDLE_VELOCITY = 0
            RIGHT_PADDLE_VELOCITY = 0

    # Ball's Movement Controls
    # When ball touches the top or bottom of screen
    if BALL_Y <= 0 + RADIUS or BALL_Y >= HEIGHT - RADIUS:
        BALL_VELOCITY_Y *= -1

    # When ball goes out of left or right window -> Ball must reset
    if BALL_X <= 0 + RADIUS or BALL_X >= WIDTH - RADIUS:
        BALL_X = WIDTH / 2 - RADIUS
        BALL_Y = HEIGHT / 2 - RADIUS

        ball_direction = random.choice(DIRECTION)
        ball_angle = random.choice(ANGLE)
        BALL_VELOCITY_X = DEFAULT_BALL_VELOCITY if BALL_VELOCITY_X < 0 else -DEFAULT_BALL_VELOCITY
        BALL_VELOCITY_X = ball_angle[0] * BALL_VELOCITY_X
        BALL_VELOCITY_Y = ball_direction * ball_angle[1] * DEFAULT_BALL_VELOCITY

    # Paddle's Movement Controls
    if LEFT_PADDLE_Y <= 0:
        LEFT_PADDLE_Y = 0
    elif LEFT_PADDLE_Y >= HEIGHT - PADDLE_HEIGHT:
        LEFT_PADDLE_Y = HEIGHT - PADDLE_HEIGHT
    if RIGHT_PADDLE_Y <= 0:
        RIGHT_PADDLE_Y = 0
    elif RIGHT_PADDLE_Y >= HEIGHT - PADDLE_HEIGHT:
        RIGHT_PADDLE_Y = HEIGHT - PADDLE_HEIGHT

    # Collisions
    # Left Paddle
    if LEFT_PADDLE_X <= BALL_X <= LEFT_PADDLE_X + PADDLE_WIDTH and LEFT_PADDLE_Y <= BALL_Y <= LEFT_PADDLE_Y + PADDLE_HEIGHT:
        BALL_X = LEFT_PADDLE_X + PADDLE_WIDTH
        BALL_VELOCITY_X *= -1
    # Right Paddle
    if RIGHT_PADDLE_X <= BALL_X <= RIGHT_PADDLE_X + PADDLE_WIDTH and RIGHT_PADDLE_Y <= BALL_Y <= RIGHT_PADDLE_Y + PADDLE_HEIGHT:
        BALL_X = RIGHT_PADDLE_X
        BALL_VELOCITY_X *= -1

    # Movements
    BALL_X += BALL_VELOCITY_X
    BALL_Y += BALL_VELOCITY_Y
    LEFT_PADDLE_Y += LEFT_PADDLE_VELOCITY
    RIGHT_PADDLE_Y += RIGHT_PADDLE_VELOCITY

    # Objects - Balls and Paddles
    pygame.draw.circle(window, BLUE, (BALL_X, BALL_Y), RADIUS)
    pygame.draw.rect(window, RED, pygame.Rect(LEFT_PADDLE_X, LEFT_PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, RED, pygame.Rect(RIGHT_PADDLE_X, RIGHT_PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.display.update()
