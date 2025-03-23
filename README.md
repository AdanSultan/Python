## Space Invaders - Pygame Edition

A classic Space Invaders game built with Pygame. Defend your spaceship against waves of descending enemies, rack up points, and aim for the high score!

## Features
- Player Controls: Move left/right with arrow keys, fire bullets with Spacebar.
- Multiple Bullets: Fire multiple shots at once (200ms cooldown).
- Lives System: Start with 3 lives; lose one if an enemy escapes or hits you.
- Audio: Laser sound on firing, explosion sound on enemy hits and player collisions.
- High Score: Tracks your best score, saved to "highscore.txt".
- Restart: Press 'R' to restart after game over.
- Progressive Difficulty: Enemies spawn faster and in greater numbers over time.

## Requirements
- Python 3.x
- Pygame (install with: "pip install pygame")

## Setup
1. Clone the repository:
   git clone https://github.com/AdanSultan/Python/tree/main/Space_Invaders_Pygame
   cd space-invaders-pygame
2. Ensure assets are in place under "assets/images/" and "assets/sounds/".
3. Run the game:
   python main.py

## Controls
- Left Arrow: Move spaceship left
- Right Arrow: Move spaceship right
- Spacebar: Fire bullets
- R: Restart after game over

## File Structure
- main.py: Main game loop and logic
- settings.py: Game setup and asset loading
- player.py: Player class (spaceship)
- enemy.py: Enemy class
- bullet.py: Bullet class with sound effects
- assets/: Images and sounds
- highscore.txt: Stores the highest score

## Contributing
Check out Pygame’s contribution guide at https://www.pygame.org/contribute.html for inspiration.

## Credits
Built by Adan Sultan with Pygame. Thanks to online learning resources and AI assistance for inspiration and guidance!
