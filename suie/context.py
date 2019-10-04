import pygame

"""
CONSTRUCTOR
    
    :param source_image         -> The pygame.Image object representing the source for borders, buttons, etc.
    :param screen_width/height  -> Dimensions of host screen, these must remain static 
    :param default_font         -> The name of the font to use for all on-screen text
    :param default_font_size    -> QoL parameter to avoid setting the same size all the time
    
"""

class SuieContext:
    def __init__(self, source_image, screen_width, screen_height, default_font, default_font_size=12):
        # Suie engine is only relevant when used with pygame
        pygame.init()

        # Save general context configuration
        self.source_image = source_image
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.default_font = default_font
        self.default_font_size = default_font_size