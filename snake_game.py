import pygame
import random
import sys

WIDTH = 1540
HEIGHT = 810
FOOD_SIZE = 8
FONT_SIZE = 55
SNAKE_SIZE = 25
speed_increment = 0.5
PAUSE_BUTTON_SIZE = 40


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (240, 240, 240)
GRAY = (150, 150, 150)


offsets = {
    "up": (0, -SNAKE_SIZE),
    "down": (0, SNAKE_SIZE),
    "left": (-SNAKE_SIZE, 0),
    "right": (SNAKE_SIZE, 0)
}

def run():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    font = pygame.font.SysFont(None, FONT_SIZE)
    small_font = pygame.font.SysFont(None, FONT_SIZE // 2)


    global snake, snake_direction, food_pos, game_over, score, speed, paused
    snake = []
    snake_direction = "right"
    food_pos = (0, 0)
    game_over = False
    score = 0
    speed = 8
    paused = False

    def reset():
        global snake, snake_direction, food_pos, game_over, score, speed, paused
        snake = [[100, 100], [120, 100], [140, 100]]
        snake_direction = "right"
        food_pos = food_position()
        game_over = False
        score = 0
        speed = 8
        paused = False

    def move_snake():
        global snake_direction, game_over, speed

        if game_over or paused:
            return

        new_head = snake[-1].copy()
        new_head[0] += offsets[snake_direction][0]
        new_head[1] += offsets[snake_direction][1]

        if new_head in snake[:-1] or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            game_over = True
            gameover_screen()
            return

        snake.append(new_head)

        if not collision():
            snake.pop(0)

        screen.fill(BACKGROUND_COLOR)
        draw_snake()
        draw_food()
        display_score()
        display_pause_icon()

        pygame.display.flip()

    def collision():
        global food_pos, score, speed
        if get_distance(snake[-1], food_pos) < SNAKE_SIZE:
            food_pos = food_position()
            score += 1
            a = score % 10
            if a == 0:
                speed += speed_increment
            return True
        return False

    def draw_snake():
        for segment in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
            pygame.draw.rect(screen, BLACK, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE), 2)

    def draw_food():
        pygame.draw.circle(screen, RED, food_pos, FOOD_SIZE)

    def food_position():
        x = random.randint(10, (WIDTH - 30) // SNAKE_SIZE) * SNAKE_SIZE
        y = random.randint(10, (HEIGHT - 30) // SNAKE_SIZE) * SNAKE_SIZE
        return (x, y)

    def get_distance(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def up():
        global snake_direction
        if snake_direction != "down":
            snake_direction = "up"

    def right():
        global snake_direction
        if snake_direction != "left":
            snake_direction = "right"

    def down():
        global snake_direction
        if snake_direction != "up":
            snake_direction = "down"

    def left():
        global snake_direction
        if snake_direction != "right":
            snake_direction = "left"

    def display_score():
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

    def display_pause_icon():
        pause_icon_rect = pygame.Rect(WIDTH - PAUSE_BUTTON_SIZE - 10, 10, PAUSE_BUTTON_SIZE, PAUSE_BUTTON_SIZE)
        pygame.draw.rect(screen, GRAY, pause_icon_rect)
        pygame.draw.rect(screen, BLACK, pause_icon_rect, 2)
        pygame.draw.line(screen, BLACK, (pause_icon_rect.left + 10, pause_icon_rect.top + 5),
                         (pause_icon_rect.left + 10, pause_icon_rect.bottom - 5), 5)
        pygame.draw.line(screen, BLACK, (pause_icon_rect.right - 10, pause_icon_rect.top + 5),
                         (pause_icon_rect.right - 10, pause_icon_rect.bottom - 5), 5)

        return pause_icon_rect

    def pause_screen():
        global paused
        resume_button_text = small_font.render('Resume', True, WHITE)
        resume_button_rect = resume_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        pygame.draw.rect(screen, BLACK, resume_button_rect.inflate(40, 20))
        screen.blit(resume_button_text, resume_button_rect)
        pygame.display.flip()

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if resume_button_rect.collidepoint(event.pos):
                        paused = False

    def gameover_screen():
        game_over_text = font.render('You are out !!', True, RED)
        button_text = font.render('Start Again', True, WHITE)

        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, BLACK, button_rect.inflate(20, 20))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(button_text, button_rect)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        reset()
                        return

    reset()

    clock = pygame.time.Clock()

    while True:
        pause_icon_rect = display_pause_icon()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and not paused:
                if event.key == pygame.K_UP:
                    up()
                elif event.key == pygame.K_RIGHT:
                    right()
                elif event.key == pygame.K_DOWN:
                    down()
                elif event.key == pygame.K_LEFT:
                    left()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pause_icon_rect.collidepoint(event.pos):
                    paused = True
                    pause_screen()

        if not game_over and not paused:
            move_snake()

        clock.tick(int(speed))

if __name__ == "__main__":
    run()