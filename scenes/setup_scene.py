import suie
import assets
from scenes import GameScene
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT

class SetupScene(GameScene):
    def __init__(self):
        GameScene.__init__(self)

        self.background = suie.Image(assets.load_image('backgrounds.forestSunset', 'png'),
                                     (0, 0),
                                     (suie.SuieContext.Instance.screen_width, suie.SuieContext.Instance.screen_height))

        self.test_rect = suie.Rectangle((10, 10), (100, 100))

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