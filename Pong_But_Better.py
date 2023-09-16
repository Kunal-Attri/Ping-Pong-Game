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
ball_x = WIDTH / 2 - RADIUS
ball_y = HEIGHT / 2 - RADIUS
DEFAULT_BALL_VELOCITY = 0.08
ball_velocity_x = DEFAULT_BALL_VELOCITY
ball_velocity_y = DEFAULT_BALL_VELOCITY

# PADDLES INIT
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 120
PADDLE_VELOCITY_UP = -0.15
PADDLE_VELOCITY_DOWN = 0.15
LEFT_PADDLE_X = 100 - PADDLE_WIDTH / 2
left_paddle_y = HEIGHT / 2 - PADDLE_HEIGHT / 2
RIGHT_PADDLE_X = WIDTH - LEFT_PADDLE_X
right_paddle_y = left_paddle_y
left_paddle_velocity = 0
right_paddle_velocity = 0

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
                right_paddle_velocity = PADDLE_VELOCITY_UP
            if event.key == pygame.K_DOWN:
                right_paddle_velocity = PADDLE_VELOCITY_DOWN

            # Left Player - W and S keys
            if event.key == pygame.K_w:
                left_paddle_velocity = PADDLE_VELOCITY_UP
            if event.key == pygame.K_s:
                left_paddle_velocity = PADDLE_VELOCITY_DOWN

        if event.type == pygame.KEYUP:
            left_paddle_velocity = 0
            right_paddle_velocity = 0

    # Ball's Movement Controls
    # When ball touches the top or bottom of screen
    if ball_y <= 0 + RADIUS or ball_y >= HEIGHT - RADIUS:
        ball_velocity_y *= -1

    # When ball goes out of left or right window -> Ball must reset
    if ball_x <= 0 + RADIUS or ball_x >= WIDTH - RADIUS:
        ball_x = WIDTH / 2 - RADIUS
        ball_y = HEIGHT / 2 - RADIUS

        ball_direction = random.choice(DIRECTION)
        ball_angle = random.choice(ANGLE)
        ball_velocity_x = DEFAULT_BALL_VELOCITY if ball_velocity_x < 0 else -DEFAULT_BALL_VELOCITY
        ball_velocity_x = ball_angle[0] * ball_velocity_x
        ball_velocity_y = ball_direction * ball_angle[1] * DEFAULT_BALL_VELOCITY

    # Paddle's Movement Controls
    if left_paddle_y <= 0:
        left_paddle_y = 0
    elif left_paddle_y >= HEIGHT - PADDLE_HEIGHT:
        left_paddle_y = HEIGHT - PADDLE_HEIGHT
    if right_paddle_y <= 0:
        right_paddle_y = 0
    elif right_paddle_y >= HEIGHT - PADDLE_HEIGHT:
        right_paddle_y = HEIGHT - PADDLE_HEIGHT

    # Collisions
    # Left Paddle
    if LEFT_PADDLE_X <= ball_x <= LEFT_PADDLE_X + PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT:
        ball_x = LEFT_PADDLE_X + PADDLE_WIDTH
        ball_velocity_x *= -1
    # Right Paddle
    if RIGHT_PADDLE_X <= ball_x <= RIGHT_PADDLE_X + PADDLE_WIDTH and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT:
        ball_x = RIGHT_PADDLE_X
        ball_velocity_x *= -1

    # Movements
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y
    left_paddle_y += left_paddle_velocity
    right_paddle_y += right_paddle_velocity

    # Objects - Balls and Paddles
    pygame.draw.circle(window, BLUE, (ball_x, ball_y), RADIUS)
    pygame.draw.rect(window, RED, pygame.Rect(LEFT_PADDLE_X, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, RED, pygame.Rect(RIGHT_PADDLE_X, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.display.update()
