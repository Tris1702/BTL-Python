import pygame
from entities import flag, player, star, hole, box
from settings import Settings

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

    def make_level_dict(self): # lưu vị trí i, j và trạng thái ô
        level = {}
        for j, row in enumerate(self.map.get_level()):
            for i, ent in enumerate(row):
                level[(i + 4, j + 1)] = ent
        return level

    def re_make_window(self, surf, level): # vẽ map
        block_size = self.settings.block_size 
        for pos, ent in level.items():
            ent.draw(surf, pos, block_size)
        pygame.display.update()

    def check_star(self, level): # kiểm tra xem đã ăn lấy sao chưa
        for pos, ent in level.items():
            if isinstance(ent.content, star):
                return False
        return True

    def check_flag(self, level): # kiểm tra xem đã lấy được cờ chưa
        for pos, ent in level.items():
            if isinstance(ent, flag):
                if not isinstance(ent.content, player):
                    return False
        return True

    def check_box(self, level): # kiểm tra xem đã đẩy hết hộp vào hố chưa
        for pos, ent in level.items():
            if isinstance(ent, hole):
                if not isinstance(ent.content, box):
                    return False
        return True
    
    def run_map(self):
        block_size = self.settings.block_size 
        self.surf = pygame.display.set_mode((self.rows*block_size + 8 * block_size, self.cols*block_size + 2 * block_size)) # vẽ lại kích thước màn hình       
        level_not_done = True
        while level_not_done:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                return
            elif keys[pygame.K_r]:
                continue
            self.player.move(self.level, self.keys, self.locks)
            if self.check_flag(self.level) and self.check_star(self.level) and self.check_box(self.level):
                return
            self.re_make_window(self.surf, self.level)
            
            

