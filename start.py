import time

import pygame

import maps
from select import Select
import buttons
from settings import Settings

class Start:
    def __init__(self, surf):
        self.surf = surf
        self.setting = Settings()

        self.maps = [maps.Map1(), maps.Map2(), maps.Map3(), maps.Map4(), maps.Map5(), maps.Map6(), maps.Map7(), maps.Map8(),
                     maps.Map9(), maps.Map10(), maps.Map11(), maps.Map12(), maps.Map13(), maps.Map14(), maps.Map15(), maps.Map16()]

        #load images
        self.start_img = pygame.image.load('assets/Start.png')

        self.logo_img = pygame.image.load('assets/Logo.png')
        self.rect = self.logo_img.get_rect()

        self.about_us = pygame.image.load('assets/About us.png')

        self.about_us_screen = pygame.image.load('assets/About us screen.png')

        self.exit_img = pygame.image.load('assets/Exit.png')

        #create button instances
        self.start_button = buttons.Buttons(400, 530, self.start_img, 1)
        self.about_us_button = buttons.Buttons(982, 626, self.about_us, 1)
        self.exit_button = buttons.Buttons(810, 155, self.exit_img, 1)

        self.select_start()

    def run(self, surf):

        surf.fill(self.setting.background_color)
        
        surf.blit(self.logo_img, (300, 40))

        if self.start_button.draw(surf):
            time.sleep(0.1)
            Select(self.maps).run(surf)

    def select_start(self):

        click_about_us = False

        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
            if click_about_us == False:
                self.run(self.surf)

            if self.about_us_button.draw(self.surf):
                time.sleep(0.1)
                click_about_us = True

            if click_about_us:
                self.surf.blit(self.about_us_screen, (0, 0))
                if self.exit_button.draw(self.surf):
                    time.sleep(0.1)
                    click_about_us = False

            pygame.display.update()
