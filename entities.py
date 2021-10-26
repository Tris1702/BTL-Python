import pygame
from abc import ABC, abstractclassmethod

black = (0, 0, 0) # đường đi
white = (255, 255, 255) 
blue_light = (39, 218, 238) # nhân vật
blue_dark = (0, 0, 246) # đích
gray_light = (192, 192, 192) # tường
gray_dark = (56, 56, 56) # cửa
red = (255, 0, 0) # ổ khóa
green = (0, 255, 0) # chìa khóa
yellow = (255, 255, 0) # sao
brown = (150, 75, 0) # hộp


class block(ABC):
    def __init__(self, content):
        self.content = content
    
    @abstractclassmethod
    def draw(self, surf, pos, block_size):
        pass

class road(block):
    def draw(self, surf,  pos, block_size):
        i = pos[0]
        j = pos[1]
        pygame.draw.rect(surf, black, (i*block_size+1, j*block_size+1, block_size-2, block_size-2))
        self.content.draw(surf,  pos, block_size)

class flag(block):
    def draw(self, surf,  pos, block_size):
        i = pos[0]
        j = pos[1]
        pygame.draw.rect(surf, blue_dark, (i*block_size+1, j*block_size+1, block_size-2, block_size-2))
        self.content.draw(surf,  pos, block_size)

class door(block):
    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        pygame.draw.rect(surf, gray_dark, (i*block_size+1, j*block_size+1, block_size-2, block_size-2))
        self.content.draw(surf,  pos, block_size)
    
class hole(block):
    def draw(self, surf,  pos, block_size):
        i = pos[0]
        j = pos[1]
        pygame.draw.rect(surf, green, (i*block_size+1, j*block_size+1, block_size-2, block_size-2))
        r = block_size / 2
        color = black
        center = (i*block_size + r, j*block_size + r)
        pygame.draw.circle(surf, color, center, r)
        self.content.draw(surf,  pos, block_size)

class content(ABC):
    @abstractclassmethod
    def get_color(self):
        pass

    @abstractclassmethod
    def draw(self, surf, pos, block_size):
        pass

class rock(content):
    def get_color(self):
        return gray_light
    
    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        color = self.get_color()
        pygame.draw.rect(surf, color, (i*block_size+1, j*block_size+1, block_size-2, block_size-2))

class box(content):
    def get_color(self):
        return brown
    
    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        color = self.get_color()
        pygame.draw.rect(surf, color, (i*block_size+10, j*block_size+10, block_size-20, block_size-20))

class empty(content):
    def get_color(self):
        return black
    def draw(self, surf, pos, block_size):
        pass

class key(content):
    def get_color(self):
        return green
    
    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        color = self.get_color()
        pygame.draw.rect(surf, color, (i*block_size+15, j*block_size+15, block_size-30, block_size-30))

class lock(content):
    def get_color(self):
        return red
    
    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        color = self.get_color()
        pygame.draw.rect(surf, color, (i*block_size+10, j*block_size+10, block_size-20, block_size-20))

class star(content):
    def get_color(self):
        return yellow
    
    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        color = self.get_color()
        pygame.draw.rect(surf, color, (i*block_size+15, j*block_size+15, block_size-30, block_size-30))

class player(content):
    def get_color(self):
        return blue_light

    def move(self, level, keys, locks):
        # print(self.get_key_run(level, keys), self.get_lock_run(level, locks))
        dir_x, dir_y, backward = self.get_input()
        self.pos = self.get_position(level)
        i = self.pos[0]
        j = self.pos[1]
        current = level[(i, j)]
        next_elm = level[(i + dir_x, j + dir_y)]
        next_ent = next_elm.content
        back_elm = level[(i - dir_x, j - dir_y)]
        back_ent = back_elm.content
        try:
            next_next_elm = level[(i + 2*dir_x, j + 2*dir_y)]
        except:
            next_next_elm = road(rock())
        next_next_ent = next_next_elm.content
        if not backward:
            if isinstance(next_ent, rock):
                return
            elif isinstance(next_ent, empty):
                if isinstance(current, door):
                    current.content = rock()
                    next_elm.content = self
                else:
                    current.content = empty()
                    next_elm.content = self
            elif isinstance(next_ent, star):
                if isinstance(current, door):
                    current.content = rock()
                    next_elm.content = self
                else:
                    current.content = empty()
                    next_elm.content = self
            elif isinstance(next_ent, key):
                if isinstance(current, door):
                    current.content = rock()
                    next_elm.content = self
                else:
                    current.content = empty()
                    next_elm.content = self
            elif isinstance(next_ent, lock) and self.get_key_run(level, keys) > self.get_lock_run(level, locks):
                if isinstance(current, door):
                    current.content = rock()
                    next_elm.content = self
                else:
                    current.content = empty()
                    next_elm.content = self
            elif isinstance(next_ent, box) and isinstance(next_next_ent, box):
                return
            elif isinstance(next_ent, box) and isinstance(next_next_ent, rock):
                return
            elif isinstance(next_ent, box) and isinstance(next_next_ent, empty):
                current.content = empty()
                next_elm.content = self
                next_next_elm.content = box()
        else:
            if isinstance(back_ent, box) and isinstance(next_ent, empty):
                current.content = box()
                back_elm.content = empty()
                next_elm.content = self

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                c_key = True if keys[pygame.K_c] else False
                if keys[pygame.K_LEFT]:
                    return -1, 0, c_key
                
                elif keys[pygame.K_RIGHT]:
                    return 1, 0, c_key

                elif keys[pygame.K_UP]:
                    return 0, -1, c_key

                elif keys[pygame.K_DOWN]:
                    return 0, 1, c_key
        return 0, 0, False

    def get_position(self, level):
        for pos, ent in level.items():
            if isinstance(ent.content, player):
                return pos

    def get_key_run(self, level, keys):
        dem = 0
        for pos, ent in level.items():
            if isinstance(ent.content, key):
                dem += 1
        return keys - dem

    def get_lock_run(self, level, locks):
        dem = 0
        for pos, ent in level.items():
            if isinstance(ent.content, lock):
                dem += 1
        return locks - dem

    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        color = self.get_color()
        pygame.draw.rect(surf, color, (i*block_size+1, j*block_size+1, block_size-2, block_size-2))
