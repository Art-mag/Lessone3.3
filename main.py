import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/42648.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Добавляем счетчик очков
score = 0
font = pygame.font.SysFont(None, 36)

# Добавляем таймер
timer_font = pygame.font.SysFont(None, 48)
game_time = 30  # Время в секундах
start_time = pygame.time.get_ticks()

running = True
while running:
    screen.fill(color)

    # Отображаем счетчик очков
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Отображаем таймер
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    time_left = max(0, game_time - elapsed_time)
    timer_text = timer_font.render(f"Время: {time_left}", True, (255, 255, 255))
    text_rect = timer_text.get_rect(center=(SCREEN_WIDTH // 2, 10 + timer_text.get_height() // 2))
    screen.blit(timer_text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

    # Проверяем время
    if time_left <= 0:
        running = False

pygame.quit()
