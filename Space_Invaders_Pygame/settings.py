import pygame
import os

pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load assets folder path
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

# Load background image with a fallback color
bg_path = os.path.join(ASSETS_DIR, "images", "background.png")
if os.path.exists(bg_path):
    background = pygame.image.load(bg_path)
else:
    print(f"Warning: Background image not found! Using a solid color instead.")
    background = None

# Load icon
icon_path = os.path.join(ASSETS_DIR, "images", "ufo.png")
if os.path.exists(icon_path):
    icon = pygame.image.load(icon_path)
    pygame.display.set_icon(icon)
else:
    print(f"Warning: UFO icon not found!")

# Load sounds
pygame.mixer.init()
bg_sound_path = os.path.join(ASSETS_DIR, "sounds", "background.wav")
if os.path.exists(bg_sound_path):
    pygame.mixer.music.load(bg_sound_path)
    pygame.mixer.music.play(-1)
else:
    print(f"Warning: Background music not found!")