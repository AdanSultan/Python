import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet
from settings import screen, SCREEN_WIDTH, SCREEN_HEIGHT
import random

# Initialize player, enemy, and bullet objects
player = Player()
enemy = Enemy()
bullet = Bullet()

# Test loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")
    if keys[pygame.K_SPACE] and bullet.state == "ready":
        bullet.fire(player.x + player.image.get_width() // 2 - bullet.image.get_width() // 2, player.y)

    # Move enemy for testing
    enemy.move()

    # Update and draw bullet
    bullet.move()
    bullet.draw()

    # Draw elements
    player.draw()
    enemy.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()