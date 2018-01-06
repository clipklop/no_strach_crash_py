#


import pygame.font


class Button():
    """Creates a button for starting a game."""
    def __init__(self, ai_settings, screen, msg):
        """Initiates an attributes of a button."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of a button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Builds rect object of a button and align it to the center of the scren
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message of button creates only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Converts string into rectabgle and align the text to the center"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Display empty button and message output."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)