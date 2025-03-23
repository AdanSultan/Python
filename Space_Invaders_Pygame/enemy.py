import pygame
import os
import random
from settings import screen, SCREEN_WIDTH, SCREEN_HEIGHT  # Only import from settings

class Enemy:
    def __init__(self, speed=3):
        assets_dir = os.path.join(os.path.dirname(__file__), "assets", "images")
        enemy_path = os.path.join(assets_dir, "enemy.png")

        if os.path.exists(enemy_path):
            self.image = pygame.image.load(enemy_path)
        else:
            print(f"Error: Enemy image not found - {enemy_path}")
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))

        self.x = random.randint(0, SCREEN_WIDTH - self.image.get_width())
        self.y = -self.image.get_height()
        self.speed = speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            return False
        return True

    def check_collision(self, player):
        enemy_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        player_rect = pygame.Rect(player.x, player.y, player.image.get_width(), player.image.get_height())
        return enemy_rect.colliderect(player_rect)