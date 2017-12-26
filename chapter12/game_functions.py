#


import sys
import pygame


def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                ship.rect.centerx += 1

def update_screen(ai_settings, screen, ship):
    """Updates the pictures on a screen and redraw new screen."""
    # Redraw the screen for each iteration
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Show the most recently drawn screen
    pygame.display.flip()

