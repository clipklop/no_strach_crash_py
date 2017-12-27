# **
# Arkanoid game.
# Moving ship, fires bullets to alines!
# **


import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Initialize a font
    # game_font = pygame.font.SysFont("Calibri", 30)   
    # text = game_font.render("Hello, world." , True, (255, 0, 0), (255, 255, 255)) 

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Start the main loop for the game.
    while True:
        # Watch for keyboards and mouse events.
        gf.check_events(ship)

        ship.update()

        # Redraw the screen during each pass through the loop.
        # Make the most recently drawn screen visible.
        gf.update_screen(ai_settings, screen, ship)

run_game()