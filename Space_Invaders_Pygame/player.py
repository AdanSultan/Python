import pygame
import os
from settings import screen, SCREEN_WIDTH

class Player:
    def __init__(self):
        assets_dir = os.path.join(os.path.dirname(__file__), "assets", "images")
        player_path = os.path.join(assets_dir, "player.png")

        if os.path.exists(player_path):
            self.image = pygame.image.load(player_path)
        else:
            print(f"Error: Player image not found - {player_path}")
            self.image = pygame.Surface((50, 50))  # Fallback square shape
            self.image.fill((0, 255, 0))  # Green color for visibility

        self.x = 370
        self.y = 480
        self.speed = 5

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < SCREEN_WIDTH - self.image.get_width():
            self.x += self.speed