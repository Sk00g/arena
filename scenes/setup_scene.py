import asset_manager
import suie
from scenes import GameScene

class SetupScene(GameScene):
    def __init__(self):
        GameScene.__init__(self)

        self.background = suie.Image(asset_manager.load_image('forestSunset.png'), (0, 0), (800, 600))

    def update(self, event_list, elapsed):
        pass

    def draw(self, screen):
        self.background.draw(screen)