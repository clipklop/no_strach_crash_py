#


import sys
import pygame


def check_keydown_events(event, ship):
    """Reacts on a key down event."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
        text = game_font.render(event.key, True, (255, 0, 0), (255, 255, 255))
    if event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True    
    if event.key == pygame.K_UP:
        # Move the ship to the top
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        # Move the ship to the bottom
        ship.moving_down = True   

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # Stop moving ship to the right
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # Stop moving ship to the left
        ship.moving_left = False
    if event.key == pygame.K_UP:
        # Stop moving the ship to the top
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        # Stop moving the ship to the bottom
        ship.moving_down = False


def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """Updates the pictures on a screen and redraw new screen."""
    # Redraw the screen for each iteration
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Show the most recently drawn screen
    pygame.display.flip()

