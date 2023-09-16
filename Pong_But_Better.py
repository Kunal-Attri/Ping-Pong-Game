import pygame

pygame.init()

# INITIALS
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# COLORS
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# BALL INIT
RADIUS = 15
BALL_X = WIDTH / 2 - RADIUS
BALL_Y = HEIGHT / 2 - RADIUS

# PADDLES INIT
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 120
LEFT_PADDLE_X = 100 - PADDLE_WIDTH / 2
LEFT_PADDLE_Y = HEIGHT / 2 - PADDLE_HEIGHT / 2
RIGHT_PADDLE_X = WIDTH - LEFT_PADDLE_X
RIGHT_PADDLE_Y = LEFT_PADDLE_Y

# MAIN LOOP
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.circle(window, BLUE, (BALL_X, BALL_Y), RADIUS)
    pygame.draw.rect(window, RED, pygame.Rect(LEFT_PADDLE_X, LEFT_PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, RED, pygame.Rect(RIGHT_PADDLE_X, RIGHT_PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.display.update()
