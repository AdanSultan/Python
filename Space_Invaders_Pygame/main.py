import pygame
import os
from settings import screen, SCREEN_WIDTH, SCREEN_HEIGHT, background
from player import Player
from enemy import Enemy
from bullet import Bullet
import random

# High score functions
def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

# Initialize game objects
player = Player()
enemies = []
bullets = []  # Now a list to store multiple bullets
score = 0
lives = 3
game_over = False
high_score = load_high_score()

# Load explosion sound for player-enemy collision
explosion_path = os.path.join(os.path.dirname(__file__), "assets", "sounds", "explosion.wav")
if os.path.exists(explosion_path):
    explosion_sound = pygame.mixer.Sound(explosion_path)
else:
    print(f"Warning: Explosion sound not found at {explosion_path}")
    explosion_sound = None

# Enemy spawning variables
spawn_timer = 0
spawn_interval = 3000
enemy_speed = 3
enemy_count = 1
clock = pygame.time.Clock()

# Bullet firing cooldown
bullet_cooldown = 200  # 200 ms cooldown between shots
last_shot_time = 0

# Fonts for UI
regular_font = pygame.font.Font(None, 36)
high_score_font = pygame.font.Font(None, 48)

# Game loop
running = True
while running:
    if not game_over:
        # Draw background
        if background:
            screen.blit(background, (0, 0))
        else:
            screen.fill((0, 0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")
        if keys[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            if current_time - last_shot_time >= bullet_cooldown:  # Check cooldown
                new_bullet = Bullet()
                new_bullet.fire(player.x + player.image.get_width() // 2 - new_bullet.image.get_width() // 2, player.y)
                bullets.append(new_bullet)
                last_shot_time = current_time

        # Spawn enemies
        spawn_timer += clock.get_time()
        if spawn_timer >= spawn_interval:
            for _ in range(enemy_count):
                enemies.append(Enemy(speed=enemy_speed))
            spawn_timer = 0
            if spawn_interval > 1000:
                spawn_interval -= 100
            enemy_speed += 0.2
            if random.random() < 0.3:
                enemy_count = min(enemy_count + 1, 5)

        # Update and draw objects
        player.draw()

        # Handle multiple bullets
        for bullet in bullets[:]:
            bullet.move()
            bullet.draw()
            if bullet.state == "ready":  # Remove bullets that go off-screen
                bullets.remove(bullet)

        # Move enemies and check collisions
        for enemy in enemies[:]:
            if not enemy.move():
                enemies.remove(enemy)
                lives -= 1
                if lives <= 0:
                    game_over = True
            else:
                enemy.draw()
                # Check collision with all bullets
                for bullet in bullets[:]:
                    if bullet.state == "fire" and bullet.check_collision(enemy):
                        enemies.remove(enemy)
                        bullets.remove(bullet)  # Remove bullet on hit
                        score += 1
                        break  # Move to next enemy after hit
                # Check player collision
                if enemy.check_collision(player):
                    if explosion_sound:
                        explosion_sound.play()
                    game_over = True

        # Display score, lives, and high score
        score_text = regular_font.render(f"Score: {score}", True, (255, 255, 255))
        lives_text = regular_font.render(f"Lives: {lives}", True, (255, 255, 255))
        high_score_text = high_score_font.render(f"High Score: {high_score}", True, (255, 215, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))
        screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, 10))

    else:
        # Game over screen
        screen.fill((0, 0, 0))
        reason = "Collision with Enemy!" if lives > 0 else "No Lives Left!"
        if score > high_score:
            high_score = score
            save_high_score(high_score)
        
        game_over_text = regular_font.render(f"Game Over! {reason}", True, (255, 0, 0))
        score_text = regular_font.render(f"Final Score: {score}", True, (255, 255, 255))
        high_score_text = high_score_font.render(f"High Score: {high_score}", True, (255, 215, 0))
        restart_text = regular_font.render("Press R to Restart", True, (255, 255, 255))
        
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 80))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 - 40))
        screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))
        pygame.display.update()

        # Check for restart
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                # Reset game state
                player = Player()
                enemies = []
                bullets = []  # Reset bullets list
                score = 0
                lives = 3
                spawn_timer = 0
                spawn_interval = 3000
                enemy_speed = 3
                enemy_count = 1
                game_over = False
                last_shot_time = 0

    pygame.display.update()
    clock.tick(60)

pygame.quit()