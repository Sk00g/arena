import sys
import pygame
from timer import Timer
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

# Initialize pygame display so we can start creating surfaces on import
pygame.init()
pygame.display.set_caption('Arena')
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Import assets before suie so we can initialize suie
import asset_manager

# Initialize GUI engine
import suie
suie.init(asset_manager.load_image('ui/suiSource.png'))

# Finally we can import our scenes which are dependent on suie
from scenes import GameScene, SetupScene

# Initialize game by creating our first game scene
first_scene = SetupScene()

while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()

    # Run update logic based on input
    elapsed_ms = clock.get_time()
    Timer.update(elapsed_ms)
    GameScene.update_current(event_list, elapsed_ms)

    # Draw loop
    screen.fill((0, 0, 0))
    GameScene.draw_current(screen)

    pygame.display.flip()

    # Set frame rate
    clock.tick(45)
