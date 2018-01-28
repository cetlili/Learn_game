import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    resolution = (ai_settings.screen_w,ai_settings.screen_h)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption('Alien Invasion')
    bg_color = ai_settings.bg_color
    ship= Ship(screen)
    while True:
        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)

run_game()