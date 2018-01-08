#


import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, stats, sb, play_button,
    ship, aliens, bullets):
    """Reacts on a key down event."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True
    if event.key == pygame.K_UP:
        # Move the ship to the top
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        # Move the ship to the bottom
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        initiate_new_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

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


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
    bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb,
             play_button, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
             aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
 bullets, mouse_x, mouse_y):
    """Launch new game after Play button has been clicked."""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # Reset the game settings
        ai_settings.initialize_dynamic_settings()

        initiate_new_game(ai_settings, screen, stats, sb, ship, aliens, bullets)


def initiate_new_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Hide mouse pointer
    pygame.mouse.set_visible(False)
    stats.game_active = True

    # Reset the scoreboard imagesmouse_x, mouse_y
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # Resets aliens and bullets
    aliens.empty()
    bullets.empty()

    # Creates new fleet of aliens and align the ship to the center
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    stats.ship_left = 3


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
 play_button):
    """Updates the pictures on a screen and redraw new screen."""
    # Redraw the screen for each iteration
    screen.fill(ai_settings.bg_color)

    # All bullets appears behind pictures of ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Output the score
    sb.show_score()

    # Show Play button is game is not active
    if not stats.game_active:
        play_button.draw_button()

    # Show the most recently drawn screen
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Updates position of the bullet and removes drop out bullets."""
    bullets.update()

    # Removes bullets that reaches top of the screen.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Collisions processing of bullets and aliens."""
    # Removes the bullets and aliens involved in collisions
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy remaining bullets and create new fleet
        bullets.empty()
        ai_settings.increase_speed()
        # Increase level
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Creats new bullet and add it to the Group of bullets."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    # Spacing between each alien is equal to one alien width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row
    # Create an alien and placed it in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of the aliens
    for row_number in range(number_rows):
        # Create the first row of aliens
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Checks if alien reaches edge of the screen."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drops fleet down and change its movement possition."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships_left
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    # Empty the list of aliens and bullets
    aliens.empty()
    bullets.empty()

    # Create a new fleet and center the ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # Pause
    sleep(0.5)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Checks if fleet reaches edge of the screen and then
    updates position of every aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
