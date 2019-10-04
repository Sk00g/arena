import suie
import assets
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT

class SetupScene:
    def __init__(self, suie_context):
        self.suie_context = suie_context
        self.background = suie.Image(assets.load_image('backgrounds.forestSunset', 'png'),
                                     (0, 0),
                                     (self.suie_context.screen_width, self.suie_context.screen_height))

        self.test_rect = suie.Rectangle((10, 10), (100, 100), fill_color=(255, 0, 0))

    def update(self, event_list, elapsed):
        for event in event_list:
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    pos = self.test_rect.get_position()
                    self.test_rect.set_position((pos[0] + 4, pos[1]))
                elif event.key == K_LEFT:
                    pos = self.test_rect.get_position()
                    self.test_rect.set_position((pos[0] - 4, pos[1]))

    def draw(self, screen):
        self.background.draw(screen)
        self.test_rect.draw(screen)