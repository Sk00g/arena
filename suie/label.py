# Represents a read-only piece of text
import assets
from pygame import Rect, Surface
from suie import Element, SuieContext


class Label(Element):
    def __init__(self, position, text: str, font_size=-1, color=(255, 255, 255)):
        Element.__init__(self, position)
        self._text = text
        self._color = color
        self._size = SuieContext.Instance.default_font_size if font_size == -1 else font_size
        self._font_object = assets.load_font(SuieContext.Instance.default_font, self._size)
        self.surface = None

        # Create the initial surface to draw (populates self.surface)
        self._render()

    # Generates the appropriate surface (and rect) based on self properties
    def _render(self):
        self.surface = self._font_object.render(self._text, False, self._color)

    # Return the size and location in a Rect object
    def get_display_rect(self):
        size = self.surface.get_rect()[2:4]
        return Rect(self._position + size)

    def set_color(self, new_color):
        self._color = new_color
        self._render()

    def set_font_size(self, new_size: int):
        self._size = new_size
        self._render()

    def set_text(self, new_text):
        self._text = new_text
        self._render()

    def draw(self, screen: Surface):
        return screen.blit(self.surface, self._get_final_position())



