import pygame
from menu import Menu
from settings import Settings

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.window = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.menu = Menu(self.window)

if __name__ == '__main__':
    ai = Game()
