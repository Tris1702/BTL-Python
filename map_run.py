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

        #load images
        self.level_1_img = pygame.image.load('assets/Map 1.png')
        self.level_2_img = pygame.image.load('assets/Map 2.png')
        self.back_img = pygame.image.load('assets/Back.png')

        # create button instances
        self.back_button = buttons.Buttons(33, 33, self.back_img, 1)

    def play_again(self):
        if self.map.get_name() == "1":
            self.map.set_level(maps.Map1().get_level())

        self.locks = self.map.get_lock()
        self.level = self.make_level_dict()
        self.player = self.map.get_player()

    def make_level_dict(self): # lưu vị trí i, j và trạng thái ô
        level = {}
        for j, row in enumerate(self.map.get_level()):
            for i, ent in enumerate(row):
                level[(i + 2, j + 2)] = ent
        return level

    def re_make_window(self, surf, level): # vẽ map
        block_size = self.settings.block_size 
        for pos, ent in level.items():
            ent.draw(surf, pos, block_size)
        pygame.display.update()

    def check_star(self, level): # kiểm tra xem đã ăn lấy "star" chưa
        for pos, ent in level.items():
            if isinstance(ent.content, star):
                return False
        return True

    def check_flag(self, level): # kiểm tra xem đã lấy được "flag" chưa
        for pos, ent in level.items():
            if isinstance(ent, flag):
                if not isinstance(ent.content, player):
                    return False
        return True

    def check_box(self, level): # kiểm tra xem đã đẩy hết "box" vào "hole" chưa
        for pos, ent in level.items():
            if isinstance(ent, hole):
                if not isinstance(ent.content, box):
                    return False
        return True

    def run_map(self):
        level_not_done = True

        while level_not_done:
            if self.map.get_name() == "1":
                self.surf.blit(self.level_1_img, (0, 0))

            if self.map.get_name() == "2":
                self.surf.blit(self.level_2_img, (0, 0))

            if self.map.get_name() == "3":
                self.surf.blit(self.level_1_img, (0, 0))

            if self.map.get_name() == "4":
                self.surf.blit(self.level_1_img, (0, 0))

            if self.map.get_name() == "5":
                self.surf.blit(self.level_1_img, (0, 0))

            if self.map.get_name() == "6":
                self.surf.blit(self.level_1_img, (0, 0))

            if self.map.get_name() == "7":
                self.surf.blit(self.level_1_img, (0, 0))

            if self.map.get_name() == "8":
                self.surf.blit(self.level_1_img, (0, 0))
            
            sum_key = self.settings.font.render(f"{self.player.get_key_run(self.level, self.keys) - self.player.get_lock_run(self.level, self.locks)}", 1, (255,255,255))
            self.surf.blit(sum_key, (783, 520))

            keys=pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                time.sleep(0.1)
                return

            if keys[pygame.K_r]:
                time.sleep(0.1)
                self.play_again()

            if self.back_button.draw(self.surf):
                time.sleep(0.1)
                return

            self.player.move(self.level, self.keys, self.locks)

            if self.check_flag(self.level) and self.check_star(self.level) and self.check_box(self.level):
                self.map.set_lock_level(True)
                time.sleep(0.5)
                return

            self.re_make_window(self.surf, self.level)
            
            

