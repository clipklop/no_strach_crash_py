# **
# Arkanoid game.
# Moving ship, fires bullets to aliens!
# **


import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats


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

    # Make a group of bullets
    bullets = Group()

    # Make a group of aliens
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store game statistics
    stats = GameStats(ai_settings)

    # Start the main loop for the game.
    while True:
        # Watch for keyboards and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

            # Redraw the screen during each pass through the loop.
            # Make the most recently drawn screen visible.
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()