import pygame
import os
from settings import screen, SCREEN_HEIGHT, SCREEN_WIDTH

class Bullet:
    def __init__(self):
        assets_dir = os.path.join(os.path.dirname(__file__), "assets", "images")
        bullet_path = os.path.join(assets_dir, "bullet.png")
        
        if os.path.exists(bullet_path):
            self.image = pygame.image.load(bullet_path)
        else:
            print(f"Error: Bullet image not found at {bullet_path}")
            self.image = pygame.Surface((5, 10))
            self.image.fill((255, 255, 255))

        # Load laser sound
        laser_path = os.path.join(os.path.dirname(__file__), "assets", "sounds", "laser.wav")
        if os.path.exists(laser_path):
            self.laser_sound = pygame.mixer.Sound(laser_path)
        else:
            print(f"Warning: Laser sound not found at {laser_path}")
            self.laser_sound = None

        # Load explosion sound
        explosion_path = os.path.join(os.path.dirname(__file__), "assets", "sounds", "explosion.wav")
        if os.path.exists(explosion_path):
            self.explosion_sound = pygame.mixer.Sound(explosion_path)
        else:
            print(f"Warning: Explosion sound not found at {explosion_path}")
            self.explosion_sound = None

        self.x = 0
        self.y = SCREEN_HEIGHT
        self.speed = 10
        self.state = "ready"

    def fire(self, x, y):
        self.state = "fire"
        self.x = x
        self.y = y
        if self.laser_sound:
            self.laser_sound.play()

    def move(self):
        if self.state == "fire":
            self.y -= self.speed
            if self.y <= 0:
                self.state = "ready"
                self.y = SCREEN_HEIGHT

    def draw(self):
        if self.state == "fire":
            screen.blit(self.image, (self.x, self.y))

    def check_collision(self, enemy):
        bullet_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.image.get_width(), enemy.image.get_height())
        collision = bullet_rect.colliderect(enemy_rect)
        if collision and self.explosion_sound:
            self.explosion_sound.play()
        return collision