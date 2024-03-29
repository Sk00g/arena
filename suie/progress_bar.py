import pygame
import math
import assets
from suie import Element


# PROGRESS BAR COLOR ENUM
BAR_COLOR_GREEN = 0
BAR_COLOR_RED = 1
BAR_COLOR_BLUE = 2
BAR_COLOR_YELLOW = 3
BAR_COLOR_DARK = 4

# Load initial images to surfaces
BAR_IMAGE_SOURCE = {
    BAR_COLOR_RED: 'ui/ProgressBars/lifeBarRed.png',
    BAR_COLOR_YELLOW: 'ui/ProgressBars/lifeBarYellow.png',
    BAR_COLOR_DARK: 'ui/ProgressBars/lifeBarDark.png',
    BAR_COLOR_BLUE: 'ui/ProgressBars/lifeBarBlue.png',
    BAR_COLOR_GREEN: 'ui/ProgressBars/lifeBarGreen.png'
}

# CONSTANTS
BAR_FILL_INCREMENT = 0.03
BAR_FILLED_RECT = pygame.Rect(8, 8, 176, 17)
BAR_EMPTY_RECT = pygame.Rect(8, 32, 176, 17)


class ProgressBar(Element):
    def __init__(self, position, size, bar_color):
        Element.__init__(self, position)
        self.color = bar_color
        self.size = size
        self._fill = 1.0
        self._target_fill = 1.0
        self._image = pygame.Surface((size[0], size[1]), pygame.SRCALPHA, 32)
        self._render()
        self._bar_image = assets.load_image(BAR_IMAGE_SOURCE[self.color])

    def _render(self):
        full_image = pygame.Surface((BAR_FILLED_RECT.width, BAR_FILLED_RECT.height), pygame.SRCALPHA, 32)
        full_image.blit(BAR_IMAGE_SOURCE[self.color], (0, 0), BAR_FILLED_RECT)
        if self._fill != 1.0:
            empty_start = BAR_EMPTY_RECT.width * self._fill
            full_image.blit(self._bar_image[self.color],
                            (empty_start, 0),
                            (BAR_EMPTY_RECT.left + empty_start,
                             BAR_EMPTY_RECT.top,
                             BAR_EMPTY_RECT.width - empty_start,
                             BAR_EMPTY_RECT.height))
        self._image = pygame.transform.scale(full_image, (self.size[0], self.size[1]))

    def get_fill(self):
        return self._target_fill

    def set_fill(self, fill_pct):
        self._target_fill = fill_pct
        self._render()

    def update(self, elapsed):
        if not self.visible or self._target_fill == self._fill:
            return

        if math.fabs(self._target_fill - self._fill) < BAR_FILL_INCREMENT:
            self._fill = self._target_fill
            self._render()
        elif self._target_fill < self._fill:
            self._fill -= BAR_FILL_INCREMENT
            self._render()
        elif self._target_fill > self._fill:
            self._fill += BAR_FILL_INCREMENT
            self._render()

    def draw(self, screen: pygame.Surface):
        if self.visible:
            screen.blit(self._image, self._get_final_position())

