import sys
import pygame
import assets
import suie
from timer import Timer
from scenes import GameScene, SetupScene
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize pygame display
pygame.init()
pygame.display.set_caption('Arena')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Initialize global suie context (singleton)
suie.SuieContext(assets.load_image('ui.suiSource', 'png'),
                 SCREEN_WIDTH, SCREEN_HEIGHT, 'emulogic', 12)

# Initialize game by creating our first game scene (automatic load to GameScene static_stack)
first_scene = SetupScene()

while True:
    # Gather keyboard and mouse events since the previous loop
    event_list = pygame.event.get()

    # Universal quit functions for convenience -- DEBUG ONLY!
    for event in event_list:
        if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()

    # Track time passed since last loop
    elapsed_ms = clock.get_time()

    # Update global Timer system
    Timer.update(elapsed_ms)

    # Run active scenes update logic based
    GameScene.update_current(event_list, elapsed_ms)

    # Clear entire screen (simple but inefficient)
    screen.fill((0, 0, 0))

    # Draw everything to screen (technically the back buffer)
    GameScene.draw_current(screen)

    # Flip backbuffer to front to display what we've drawn
    pygame.display.flip()

    # Set frame rate (wait specific time until next loop)
    clock.tick(45)