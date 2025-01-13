import random
import time
import pygame
import os

def scale_image(image, target_size, cover=False):
    width, height = image.get_size()
    target_width, target_height = target_size

    if cover:
        scaling_factor = max(target_width / width, target_height / height)
    else:
        scaling_factor = min(target_width / width, target_height / height)

    new_size = (int(width * scaling_factor), int(height * scaling_factor))
    return pygame.transform.scale(image, new_size)

def hot_potato_game():
    pygame.init()
    pygame.mixer.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Disco Potato Panic!")

    original_potato = pygame.image.load("disco_potato.png")
    potato_image = scale_image(original_potato, (100, 100))

    original_background = pygame.image.load("dance_floor.png")
    background = scale_image(original_background, (screen_width, screen_height), cover=True)

    bg_rect = background.get_rect()
    bg_x = (screen_width - bg_rect.width) // 2
    bg_y = (screen_height - bg_rect.height) // 2

    pygame.mixer.music.load("funky_disco_beat.mp3")
    pygame.mixer.music.play(-1)

    potato_pos = [screen_width // 2, screen_height // 2]
    score = 0
    game_over = False

    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if potato_rect.collidepoint(event.pos):
                    score += 1
                    potato_pos = [random.randint(50, screen_width - 50),
                                  random.randint(50, screen_height - 50)]
                    pygame.mixer.Sound("boing.wav").play()

        screen.blit(background, (bg_x, bg_y))

        potato_rect = potato_image.get_rect(center=potato_pos)
        screen.blit(potato_image, potato_rect)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

        if pygame.time.get_ticks() - start_time >= 15000:
            game_over = True

    screen.fill((0, 0, 0))
    game_over_text = font.render("GAME OVER!", True, (255, 0, 0))
    final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 75))
    screen.blit(final_score_text, (screen_width // 2 - 100, screen_height // 2))
    pygame.display.flip()

    pygame.time.wait(1000)
    pygame.quit()

hot_potato_game()