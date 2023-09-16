import pygame
import random

pygame.init()

gadget_pair = 1
ch = int(input("Gadget: "))
if ch == 2:
    gadget_pair = 2

# INITIALS
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
DIRECTION = [-1, 1]
ANGLE = [(1, 2), (1, 1), (2, 1)]
WINNING_SCORE = 5

player_one_score = 0
player_two_score = 0

# COLORS
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# BALL INIT
RADIUS = 15
DEFAULT_BALL_VELOCITY = 0.2
ball_x = WIDTH / 2 - RADIUS
ball_y = HEIGHT / 2 - RADIUS
ball_velocity_x = DEFAULT_BALL_VELOCITY
ball_velocity_y = DEFAULT_BALL_VELOCITY
dummy_ball_x = WIDTH / 2 - RADIUS
dummy_ball_y = HEIGHT / 2 - RADIUS
dummy_ball_velocity_x = DEFAULT_BALL_VELOCITY
dummy_ball_velocity_y = DEFAULT_BALL_VELOCITY

# PADDLES INIT
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 120
PADDLE_VELOCITY_UP = -0.4
PADDLE_VELOCITY_DOWN = 0.4
LEFT_PADDLE_X = 100 - PADDLE_WIDTH / 2
RIGHT_PADDLE_X = WIDTH - LEFT_PADDLE_X
left_paddle_y = HEIGHT / 2 - PADDLE_HEIGHT / 2
right_paddle_y = left_paddle_y
left_paddle_velocity = 0
right_paddle_velocity = 0
SECOND_LEFT_PADDLE_X = 100 - PADDLE_WIDTH / 2
SECOND_RIGHT_PADDLE_X = WIDTH - LEFT_PADDLE_X
second_left_paddle_y = HEIGHT / 2 - PADDLE_HEIGHT / 2
second_right_paddle_y = left_paddle_y
second_left_paddle_velocity = 0
second_right_paddle_velocity = 0

# GADGETS
DEFAULT_GADGET_AMOUNT = 5
left_gadget_activated = 0
right_gadget_activated = 0
left_gadget_remaining = DEFAULT_GADGET_AMOUNT
right_gadget_remaining = DEFAULT_GADGET_AMOUNT

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
                second_right_paddle_velocity = PADDLE_VELOCITY_UP
            elif event.key == pygame.K_DOWN:
                right_paddle_velocity = PADDLE_VELOCITY_DOWN
                second_right_paddle_velocity = PADDLE_VELOCITY_DOWN
            elif event.key == pygame.K_RIGHT and right_gadget_remaining:
                right_gadget_activated = 1
            elif event.key == pygame.K_LEFT and right_gadget_remaining:
                right_gadget_activated = 2

            # Left Player - W and S keys
            if event.key == pygame.K_w:
                left_paddle_velocity = PADDLE_VELOCITY_UP
                second_left_paddle_velocity = PADDLE_VELOCITY_UP
            elif event.key == pygame.K_s:
                left_paddle_velocity = PADDLE_VELOCITY_DOWN
                second_left_paddle_velocity = PADDLE_VELOCITY_DOWN
            elif event.key == pygame.K_d and left_gadget_remaining:
                left_gadget_activated = 1
            elif event.key == pygame.K_a and left_gadget_remaining:
                left_gadget_activated = 2

        if event.type == pygame.KEYUP:
            left_paddle_velocity = 0
            second_left_paddle_velocity = 0
            right_paddle_velocity = 0
            second_right_paddle_velocity = 0

    # Ball's Movement Controls
    # When ball touches the top or bottom of screen
    if ball_y <= 0 + RADIUS or ball_y >= HEIGHT - RADIUS:
        ball_velocity_y *= -1
    if dummy_ball_y <= 0 + RADIUS or dummy_ball_y >= HEIGHT - RADIUS:
        dummy_ball_velocity_y *= -1
    # When ball goes out of left or right window -> Ball must reset
    if ball_x <= 0 + RADIUS or ball_x >= WIDTH - RADIUS:
        if ball_x <= 0 + RADIUS:
            player_two_score += 1
        else:
            player_one_score += 1

        ball_x = WIDTH / 2 - RADIUS
        ball_y = HEIGHT / 2 - RADIUS
        dummy_ball_x = WIDTH / 2 - RADIUS
        dummy_ball_y = HEIGHT / 2 - RADIUS

        ball_direction = random.choice(DIRECTION)
        ball_angle = random.choice(ANGLE)
        ball_velocity_x = DEFAULT_BALL_VELOCITY if ball_velocity_x < 0 else -DEFAULT_BALL_VELOCITY
        ball_velocity_x = ball_angle[0] * ball_velocity_x
        ball_velocity_y = ball_direction * ball_angle[1] * DEFAULT_BALL_VELOCITY

        dummy_ball_velocity_x = DEFAULT_BALL_VELOCITY if dummy_ball_velocity_x < 0 else -DEFAULT_BALL_VELOCITY
        dummy_ball_velocity_x = ball_angle[0] * dummy_ball_velocity_x
        dummy_ball_velocity_y = ball_direction * ball_angle[1] * DEFAULT_BALL_VELOCITY

        left_paddle_y = HEIGHT / 2 - PADDLE_HEIGHT / 2
        right_paddle_y = left_paddle_y
        second_left_paddle_y = left_paddle_y
        second_right_paddle_y = right_paddle_y
        second_left_paddle_velocity = left_paddle_velocity
        second_right_paddle_velocity = right_paddle_velocity

    # Paddle's Movement Controls
    if left_paddle_y <= 0:
        left_paddle_y = 0
    elif left_paddle_y >= HEIGHT - PADDLE_HEIGHT:
        left_paddle_y = HEIGHT - PADDLE_HEIGHT
    if right_paddle_y <= 0:
        right_paddle_y = 0
    elif right_paddle_y >= HEIGHT - PADDLE_HEIGHT:
        right_paddle_y = HEIGHT - PADDLE_HEIGHT

    if second_left_paddle_y <= 0:
        second_left_paddle_y = 0
    elif second_left_paddle_y >= HEIGHT - PADDLE_HEIGHT:
        second_left_paddle_y = HEIGHT - PADDLE_HEIGHT
    if second_right_paddle_y <= 0:
        second_right_paddle_y = 0
    elif second_right_paddle_y >= HEIGHT - PADDLE_HEIGHT:
        second_right_paddle_y = HEIGHT - PADDLE_HEIGHT

    # Collisions
    # Left Paddle
    if LEFT_PADDLE_X <= ball_x <= LEFT_PADDLE_X + PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT:
        ball_x = LEFT_PADDLE_X + PADDLE_WIDTH
        dummy_ball_x = LEFT_PADDLE_X + PADDLE_WIDTH
        ball_velocity_x *= -1
        dummy_ball_velocity_x *= -1
    elif SECOND_LEFT_PADDLE_X <= ball_x <= SECOND_LEFT_PADDLE_X + PADDLE_WIDTH and second_left_paddle_y <= ball_y <= second_left_paddle_y + PADDLE_HEIGHT:
        ball_x = SECOND_LEFT_PADDLE_X + PADDLE_WIDTH
        dummy_ball_x = SECOND_LEFT_PADDLE_X + PADDLE_WIDTH
        ball_velocity_x *= -1
        dummy_ball_velocity_x *= -1
    # Right Paddle
    if RIGHT_PADDLE_X <= ball_x <= RIGHT_PADDLE_X + PADDLE_WIDTH and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT:
        ball_x = RIGHT_PADDLE_X
        dummy_ball_x = RIGHT_PADDLE_X
        ball_velocity_x *= -1
        dummy_ball_velocity_x *= -1
    elif SECOND_RIGHT_PADDLE_X <= ball_x <= SECOND_RIGHT_PADDLE_X + PADDLE_WIDTH and second_right_paddle_y <= ball_y <= second_right_paddle_y + PADDLE_HEIGHT:
        ball_x = SECOND_RIGHT_PADDLE_X
        dummy_ball_x = SECOND_RIGHT_PADDLE_X
        ball_velocity_x *= -1
        dummy_ball_velocity_x *= -1

    # Gadgets
    if gadget_pair == 1:
        if left_gadget_activated == 1:
            if LEFT_PADDLE_X <= ball_x <= LEFT_PADDLE_X + PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT:
                ball_x = LEFT_PADDLE_X + PADDLE_WIDTH
                dummy_ball_x = LEFT_PADDLE_X + PADDLE_WIDTH
                ball_velocity_x *= 3.5
                dummy_ball_velocity_x *= 3.5
                left_gadget_activated = 0
                left_gadget_remaining -= 1
        if right_gadget_activated == 1:
            if RIGHT_PADDLE_X <= ball_x <= RIGHT_PADDLE_X + PADDLE_WIDTH and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT:
                ball_x = RIGHT_PADDLE_X
                dummy_ball_x = RIGHT_PADDLE_X
                ball_velocity_x *= 3.5
                dummy_ball_velocity_x *= 3.5
                right_gadget_activated = 0
                right_gadget_remaining -= 1

        if left_gadget_activated == 2:
            left_paddle_y = ball_y
            second_left_paddle_y = ball_y
            left_gadget_activated = 0
            left_gadget_remaining -= 1
        if right_gadget_activated == 2:
            right_paddle_y = ball_y
            second_right_paddle_y = ball_y
            right_gadget_activated = 0
            right_gadget_remaining -= 1
    elif gadget_pair == 2:
        if left_gadget_activated == 1:
            if LEFT_PADDLE_X <= ball_x <= LEFT_PADDLE_X + PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT:
                ball_x = LEFT_PADDLE_X + PADDLE_WIDTH
                dummy_ball_x = LEFT_PADDLE_X + PADDLE_WIDTH
                ball_velocity_x *= -1
                dummy_ball_velocity_x *= -1
                dummy_ball_velocity_y *= -1
                left_gadget_activated = 0
                left_gadget_remaining -= 1
        if right_gadget_activated == 1:
            if RIGHT_PADDLE_X <= ball_x <= RIGHT_PADDLE_X + PADDLE_WIDTH and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT:
                ball_x = RIGHT_PADDLE_X
                dummy_ball_x = RIGHT_PADDLE_X
                ball_velocity_x *= -1
                dummy_ball_velocity_x *= -1
                dummy_ball_velocity_y *= -1
                right_gadget_activated = 0
                right_gadget_remaining -= 1

        if left_gadget_activated == 2:
            second_left_paddle_y = left_paddle_y + 200
            left_gadget_activated = 0
            left_gadget_remaining -= 1
        if right_gadget_activated == 2:
            second_right_paddle_y = right_paddle_y + 200
            right_gadget_activated = 0
            right_gadget_remaining -= 1


    # Movements
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y
    dummy_ball_x += dummy_ball_velocity_x
    dummy_ball_y += dummy_ball_velocity_y
    left_paddle_y += left_paddle_velocity
    right_paddle_y += right_paddle_velocity
    second_left_paddle_y += second_left_paddle_velocity
    second_right_paddle_y += second_right_paddle_velocity

    # Scoreboard
    font = pygame.font.SysFont('calibri', 32)

    score_1 = font.render("Player 1: " + str(player_one_score), True, WHITE)
    window.blit(score_1, (25, 25))
    score_2 = font.render("Player 2: " + str(player_two_score), True, WHITE)
    window.blit(score_2, (825, 25))

    gad_left_1 = font.render("Gadget left: " + str(left_gadget_remaining), True, WHITE)
    window.blit(gad_left_1, (25, 65))
    gad_left_2 = font.render("Gadget left: " + str(right_gadget_remaining), True, WHITE)
    window.blit(gad_left_1, (825, 65))

    # Objects - Balls and Paddles
    pygame.draw.circle(window, BLUE, (ball_x, ball_y), RADIUS)
    pygame.draw.rect(window, RED, pygame.Rect(LEFT_PADDLE_X, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, RED, pygame.Rect(RIGHT_PADDLE_X, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # dummy ball
    pygame.draw.circle(window, BLUE, (dummy_ball_x, dummy_ball_y), RADIUS)

    # second paddle
    pygame.draw.rect(window, RED, pygame.Rect(SECOND_LEFT_PADDLE_X, second_left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, RED, pygame.Rect(SECOND_RIGHT_PADDLE_X, second_right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    if left_gadget_activated == 1:
        pygame.draw.circle(window, WHITE, (LEFT_PADDLE_X + 10, left_paddle_y + 10), 4)
    if right_gadget_activated == 1:
        pygame.draw.circle(window, WHITE, (RIGHT_PADDLE_X + 10, right_paddle_y + 10), 4)

    # Endscreen
    winning_font = pygame.font.SysFont("callibri", 32)
    if player_one_score >= WINNING_SCORE:
        window.fill(BLACK)
        endscreen = winning_font.render("Player 1 won!!!!", True, WHITE)
        window.blit(endscreen, (200, 250))
    if player_two_score >= WINNING_SCORE:
        window.fill(BLACK)
        endscreen = winning_font.render("Player 2 won!!!!", True, WHITE)
        window.blit(endscreen, (200, 250))

    pygame.display.update()
