import pygame as pg
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
#from GUI import ai_settings


def run_game():
    ai_settings = Settings()
    pg.init()
    screen = pg.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pg.display.set_caption('Alien Invasion')
    play_button = Button(ai_settings, screen, 'Play')
    clock = pg.time.Clock()
    stats = GameStats(ai_settings)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                         play_button)
        clock.tick(180)


run_game()
