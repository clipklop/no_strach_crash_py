# **
# Arkanoid game.
# Moving ship, fires bullets to aliens!
# **


import pygame
import game_functions as gf
from ship import Ship
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Creates Play button
    play_button = Button(ai_settings, screen, "Play")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group of bullets
    bullets = Group()

    # Make a group of aliens
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instances to store game statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Start the main loop for the game.
    while True:
        # Watch for keyboards and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # Redraw the screen during each pass through the loop.
        # Make the most recently drawn screen visible.
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
