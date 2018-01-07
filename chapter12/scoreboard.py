#


import pygame.font


class Scoreboard():
    """Creates a score boarding for a game."""
    def __init__(self, ai_settings, screen, stats):
        """Initiates an attributes for score counting."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Set the fonts for scoring board
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepares scores image
        self.prep_score()

    def prep_score(self):
        """Converts current score to an image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        
        # Output scores on top right side of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Outputs the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)