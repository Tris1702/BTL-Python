import pygame
import buttons
import maps
from entities import flag, player, star, hole, box
from settings import Settings
import time


class RunMap:
    def __init__(self, map_obj, surf):
        self.map = map_obj
        self.surf = surf
        self.settings = Settings()
        self.rows = map_obj.get_width()
        self.cols = map_obj.get_height()
        self.keys = map_obj.get_key()
        self.locks = map_obj.get_lock()
        self.level = self.make_level_dict()
        self.player = self.map.get_player()

        # load images
        self.level_1_img = pygame.image.load('assets/Map 1.png')
        self.level_2_img = pygame.image.load('assets/Map 2.png')
        self.level_3_img = pygame.image.load('assets/Map 3.png')
        self.level_4_img = pygame.image.load('assets/Map 4.png')
        self.level_5_img = pygame.image.load('assets/Map 5.png')
        self.level_6_img = pygame.image.load('assets/Map 6.png')
        self.level_7_img = pygame.image.load('assets/Map 7.png')
        self.level_8_img = pygame.image.load('assets/Map 8.png')
        self.level_9_img = pygame.image.load('assets/Map 9.png')
        self.level_10_img = pygame.image.load('assets/Map 10.png')
        self.level_11_img = pygame.image.load('assets/Map 11.png')
        self.level_12_img = pygame.image.load('assets/Map 12.png')
        self.level_13_img = pygame.image.load('assets/Map 6.png')
        self.level_14_img = pygame.image.load('assets/Map 6.png')
        self.level_15_img = pygame.image.load('assets/Map 6.png')
        self.level_16_img = pygame.image.load('assets/Map 6.png')
        self.back_img = pygame.image.load('assets/Back.png')

        # create button instances
        self.back_button = buttons.Buttons(33, 33, self.back_img, 1)

    def play_again(self):
        if self.map.get_name() == "1":
            self.map.set_level(maps.Map1().get_level())

        if self.map.get_name() == "2":
            self.map.set_level(maps.Map2().get_level())

        if self.map.get_name() == "3":
            self.map.set_level(maps.Map3().get_level())

        if self.map.get_name() == "4":
            self.map.set_level(maps.Map4().get_level())

        if self.map.get_name() == "5":
            self.map.set_level(maps.Map5().get_level())

        if self.map.get_name() == "6":
            self.map.set_level(maps.Map6().get_level())

        if self.map.get_name() == "7":
            self.map.set_level(maps.Map7().get_level())

        if self.map.get_name() == "8":
            self.map.set_level(maps.Map8().get_level())

        if self.map.get_name() == "9":
            self.map.set_level(maps.Map9().get_level())

        if self.map.get_name() == "10":
            self.map.set_level(maps.Map10().get_level())

        if self.map.get_name() == "11":
            self.map.set_level(maps.Map11().get_level())

        if self.map.get_name() == "12":
            self.map.set_level(maps.Map12().get_level())

        if self.map.get_name() == "13":
            self.map.set_level(maps.Map13().get_level())

        if self.map.get_name() == "14":
            self.map.set_level(maps.Map14().get_level())

        if self.map.get_name() == "15":
            self.map.set_level(maps.Map15().get_level())

        if self.map.get_name() == "16":
            self.map.set_level(maps.Map16().get_level())

        self.locks = self.map.get_lock()
        self.level = self.make_level_dict()
        self.player = self.map.get_player()

    def draw_map(self):
        if self.map.get_name() == "1":
            self.surf.blit(self.level_1_img, (0, 0))

        if self.map.get_name() == "2":
            self.surf.blit(self.level_2_img, (0, 0))

        if self.map.get_name() == "3":
            self.surf.blit(self.level_3_img, (0, 0))

        if self.map.get_name() == "4":
            self.surf.blit(self.level_4_img, (0, 0))

        if self.map.get_name() == "5":
            self.surf.blit(self.level_5_img, (0, 0))

        if self.map.get_name() == "6":
            self.surf.blit(self.level_6_img, (0, 0))

        if self.map.get_name() == "7":
            self.surf.blit(self.level_7_img, (0, 0))

        if self.map.get_name() == "8":
            self.surf.blit(self.level_8_img, (0, 0))

        if self.map.get_name() == "9":
            self.surf.blit(self.level_9_img, (0, 0))

        if self.map.get_name() == "10":
            self.surf.blit(self.level_10_img, (0, 0))

        if self.map.get_name() == "11":
            self.surf.blit(self.level_11_img, (0, 0))

        if self.map.get_name() == "12":
            self.surf.blit(self.level_12_img, (0, 0))

        if self.map.get_name() == "13":
            self.surf.blit(self.level_13_img, (0, 0))

        if self.map.get_name() == "14":
            self.surf.blit(self.level_14_img, (0, 0))

        if self.map.get_name() == "15":
            self.surf.blit(self.level_15_img, (0, 0))

        if self.map.get_name() == "16":
            self.surf.blit(self.level_16_img, (0, 0))

    def make_level_dict(self):  # lưu vị trí i, j và trạng thái ô
        level = {}
        for j, row in enumerate(self.map.get_level()):
            for i, ent in enumerate(row):
                level[(i + 2, j + 2)] = ent
        return level

    def re_make_window(self, surf, level):  # vẽ map
        block_size = self.settings.block_size
        for pos, ent in level.items():
            ent.draw(surf, pos, block_size)
        pygame.display.update()

    def check_star(self, level):  # kiểm tra xem đã ăn lấy "cake" chưa
        for pos, ent in level.items():
            if isinstance(ent.content, star):
                return False
        return True

    def check_flag(self, level):  # kiểm tra xem đã lấy được "flag" chưa
        for pos, ent in level.items():
            if isinstance(ent, flag):
                if not isinstance(ent.content, player):
                    return False
        return True

    def run_map(self):
        level_not_done = True

        while level_not_done:
            self.draw_map()

            sum_key = self.settings.font.render(
                f"{self.player.get_key_run(self.level, self.keys) - self.player.get_lock_run(self.level, self.locks)}",
                1, (255, 255, 255))
            self.surf.blit(sum_key, (783, 520))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                time.sleep(0.2)
                return

            if keys[pygame.K_r]:
                time.sleep(0.2)
                self.play_again()

            if self.back_button.draw(self.surf):
                time.sleep(0.2)
                return

            self.player.move(self.level, self.keys, self.locks)

            if self.check_flag(self.level) and self.check_star(self.level):
                self.map.set_lock_level(True)
                time.sleep(0.5)
                return

            self.re_make_window(self.surf, self.level)

