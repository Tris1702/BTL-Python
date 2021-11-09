import pygame

class Settings:
    def __init__(self):

        # background
        self.screen_width = 1080
        self.screen_height = 720
        self.screen_size = (1080, 720)
        self.background_color = "#2A3756"

        # map_run
        self.block_size = 55 # kích thước 1 ô

        #font
        self.font_loading = pygame.font.SysFont("Showcard Gothic", 45)
        self.font = pygame.font.SysFont("Showcard Gothic", 35)
        