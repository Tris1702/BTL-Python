import pygame
import time
import map_run
import maps
import buttons
from settings import Settings

class Select:
    def __init__(self, maps):
        self.setting = Settings()

        #map
        self.maps = maps

        #load images
        self.back_img = pygame.image.load('assets/Back.png')
        self.select_level_img = pygame.image.load('assets/select level.png')
        self.rect = self.select_level_img.get_rect()
        self.level_1_img = pygame.image.load('assets/level 1.png')
        self.next_right_img = pygame.image.load('assets/right.png')
        self.next_left_img = pygame.image.load('assets/left.png')

        #create button
        self.back_button = buttons.Buttons(33, 33, self.back_img, 1)
        self.level_1_button = buttons.Buttons(156, 214, self.level_1_img, 1)
        self.next_right_button = buttons.Buttons(980, 323, self.next_right_img, 1)
        self.next_left_button = buttons.Buttons(35, 323, self.next_left_img, 1)

        #
        self.next_slide = True

    def select_level(self, surf):
        surf.blit(self.select_level_img, (370, 58))

        if self.next_slide:
            #level 1
            if self.level_1_button.draw(surf):
                time.sleep(0.1)
                map_run.RunMap(self.maps[0], surf).run_map()
                self.maps[0].set_level(maps.Map1().get_level())

            #level 2
            img = 'assets/Lock level.png'
            if self.maps[0].get_lock_level():
                img = 'assets/level 2.png'
            level_2_img = pygame.image.load(img)
            level_2_button = buttons.Buttons(362, 214, level_2_img, 1)
            if level_2_button.draw(surf):
                time.sleep(0.1)
                if self.maps[0].get_lock_level():
                    map_run.RunMap(self.maps[1], surf).run_map()
                    self.maps[1].set_level(maps.Map2().get_level())

            # level 3
            img = 'assets/Lock level.png'
            if self.maps[1].get_lock_level():
                img = 'assets/level 3.png'
            level_3_img = pygame.image.load(img)
            level_3_button = buttons.Buttons(575, 214, level_3_img, 1)
            if level_3_button.draw(surf):
                time.sleep(0.1)
                if self.maps[1].get_lock_level():
                    map_run.RunMap(self.maps[2], surf).run_map()
                    self.maps[2].set_level(maps.Map3().get_level())

            # level 4
            img = 'assets/Lock level.png'
            if self.maps[2].get_lock_level():
                img = 'assets/level 4.png'
            level_4_img = pygame.image.load(img)
            level_4_button = buttons.Buttons(781, 214, level_4_img, 1)
            if level_4_button.draw(surf):
                time.sleep(0.1)
                if self.maps[2].get_lock_level():
                    map_run.RunMap(self.maps[3], surf).run_map()
                    self.maps[3].set_level(maps.Map4().get_level())

            # level 5
            img = 'assets/Lock level.png'
            if self.maps[3].get_lock_level():
                img = 'assets/level 5.png'
            level_5_img = pygame.image.load(img)
            level_5_button = buttons.Buttons(156, 428, level_5_img, 1)
            if level_5_button.draw(surf):
                time.sleep(0.1)
                if self.maps[3].get_lock_level():
                    map_run.RunMap(self.maps[4], surf).run_map()
                    self.maps[4].set_level(maps.Map5().get_level())

            # level 6
            img = 'assets/Lock level.png'
            if self.maps[4].get_lock_level():
                img = 'assets/level 6.png'
            level_6_img = pygame.image.load(img)
            level_6_button = buttons.Buttons(369, 428, level_6_img, 1)
            if level_6_button.draw(surf):
                time.sleep(0.1)
                if self.maps[4].get_lock_level():
                    map_run.RunMap(self.maps[5], surf).run_map()
                    self.maps[5].set_level(maps.Map6().get_level())

            # level 7
            img = 'assets/Lock level.png'
            if self.maps[5].get_lock_level():
                img = 'assets/level 7.png'
            level_7_img = pygame.image.load(img)
            level_7_button = buttons.Buttons(575, 428, level_7_img, 1)
            if level_7_button.draw(surf):
                time.sleep(0.1)
                if self.maps[4].get_lock_level():
                    map_run.RunMap(self.maps[6], surf).run_map()
                    self.maps[6].set_level(maps.Map7().get_level())

            # level 8
            img = 'assets/Lock level.png'
            if self.maps[6].get_lock_level():
                img = 'assets/level 8.png'
            level_8_img = pygame.image.load(img)
            level_8_button = buttons.Buttons(781, 428, level_8_img, 1)
            if level_8_button.draw(surf):
                time.sleep(0.1)
                if self.maps[6].get_lock_level():
                    map_run.RunMap(self.maps[7], surf).run_map()
                    self.maps[7].set_level(maps.Map8().get_level())

            if self.next_right_button.draw(surf):
                time.sleep(0.2)
                self.next_slide = False
        else:
            # level 9
            img = 'assets/Lock level.png'
            if self.maps[7].get_lock_level():
                img = 'assets/level 9.png'
            level_9_img = pygame.image.load(img)
            level_9_button = buttons.Buttons(156, 214, level_9_img, 1)
            if level_9_button.draw(surf):
                time.sleep(0.1)
                if self.maps[7].get_lock_level():
                    map_run.RunMap(self.maps[8], surf).run_map()
                    self.maps[8].set_level(maps.Map9().get_level())

            # level 10
            img = 'assets/Lock level.png'
            if self.maps[8].get_lock_level():
                img = 'assets/level 10.png'
            level_10_img = pygame.image.load(img)
            level_10_button = buttons.Buttons(362, 214, level_10_img, 1)
            if level_10_button.draw(surf):
                time.sleep(0.1)
                if self.maps[8].get_lock_level():
                    map_run.RunMap(self.maps[9], surf).run_map()
                    self.maps[9].set_level(maps.Map10().get_level())

            # level 11
            img = 'assets/Lock level.png'
            if self.maps[9].get_lock_level():
                img = 'assets/level 11.png'
            level_11_img = pygame.image.load(img)
            level_11_button = buttons.Buttons(575, 214, level_11_img, 1)
            if level_11_button.draw(surf):
                time.sleep(0.1)
                if self.maps[9].get_lock_level():
                    map_run.RunMap(self.maps[10], surf).run_map()
                    self.maps[10].set_level(maps.Map11().get_level())

            # level 12
            img = 'assets/Lock level.png'
            if self.maps[10].get_lock_level():
                img = 'assets/level 12.png'
            level_12_img = pygame.image.load(img)
            level_12_button = buttons.Buttons(781, 214, level_12_img, 1)
            if level_12_button.draw(surf):
                time.sleep(0.1)
                if self.maps[10].get_lock_level():
                    map_run.RunMap(self.maps[11], surf).run_map()
                    self.maps[11].set_level(maps.Map12().get_level())

            # level 13
            img = 'assets/Lock level.png'
            if self.maps[11].get_lock_level():
                img = 'assets/level 13.png'
            level_13_img = pygame.image.load(img)
            level_13_button = buttons.Buttons(156, 428, level_13_img, 1)
            if level_13_button.draw(surf):
                time.sleep(0.1)
                if self.maps[11].get_lock_level():
                    map_run.RunMap(self.maps[12], surf).run_map()
                    self.maps[12].set_level(maps.Map13().get_level())

            # level 14
            img = 'assets/Lock level.png'
            if self.maps[12].get_lock_level():
                img = 'assets/level 14.png'
            level_14_img = pygame.image.load(img)
            level_14_button = buttons.Buttons(369, 428, level_14_img, 1)
            if level_14_button.draw(surf):
                time.sleep(0.1)
                if self.maps[12].get_lock_level():
                    map_run.RunMap(self.maps[13], surf).run_map()
                    self.maps[13].set_level(maps.Map14().get_level())

            # level 15
            img = 'assets/Lock level.png'
            if self.maps[13].get_lock_level():
                img = 'assets/level 15.png'
            level_15_img = pygame.image.load(img)
            level_15_button = buttons.Buttons(575, 428, level_15_img, 1)
            if level_15_button.draw(surf):
                time.sleep(0.1)
                if self.maps[13].get_lock_level():
                    map_run.RunMap(self.maps[14], surf).run_map()
                    self.maps[14].set_level(maps.Map15().get_level())

            # level 16
            img = 'assets/Lock level.png'
            if self.maps[14].get_lock_level():
                img = 'assets/level 16.png'
            level_16_img = pygame.image.load(img)
            level_16_button = buttons.Buttons(781, 428, level_16_img, 1)
            if level_16_button.draw(surf):
                if self.maps[14].get_lock_level():
                    map_run.RunMap(self.maps[15], surf).run_map()
                    self.maps[15].set_level(maps.Map16().get_level())

            if self.next_left_button.draw(surf):
                time.sleep(0.2)
                self.next_slide = True

    def run(self, surf):
        while True:
            surf.fill(self.setting.background_color)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()

            if self.back_button.draw(surf):
                time.sleep(0.1)
                return

            self.select_level(surf)

            pygame.display.update()
