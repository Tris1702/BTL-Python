import pygame
import time
from abc import ABC, abstractclassmethod

black = "#0D0E2E"  # đường đi
white = "#dbdfe2"
blue_light = (39, 218, 238)  # nhân vật
blue_dark = (0, 0, 246)  # đích
gray_light = (192, 192, 192)  # tường
gray_dark = (56, 56, 56)  # cửa
red = (255, 0, 0)  # ổ khóa
green = (0, 255, 0)  # chìa khóa
yellow = (255, 255, 0)  # sao
brown = (150, 75, 0)  # hộp


class block(ABC):
    def __init__(self, content):
        self.content = content

    @abstractclassmethod
    def draw(self, surf, pos, block_size):
        pass


class road(block):
    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        pygame.draw.rect(surf, black, (i * block_size, j * block_size, block_size, block_size))
        self.content.draw(surf, pos, block_size)


class flag(block):
    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        pygame.draw.rect(surf, black, (i * block_size, j * block_size, block_size, block_size))
        image = pygame.image.load('assets/chanhchanh 1.png')
        surf.blit(image, (i * block_size + 6, j * block_size + 5))
        self.content.draw(surf, pos, block_size)


class door(block):
    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        pygame.draw.rect(surf, black, (i * block_size, j * block_size, block_size, block_size))
        image = pygame.image.load('assets/door.png')
        surf.blit(image, (i * block_size, j * block_size))
        self.content.draw(surf, pos, block_size)

class content(ABC):
    @abstractclassmethod
    def draw(self, surf, pos, block_size):
        pass


class rock(content):
    def __init__(self):
        self.image = pygame.image.load('assets/wall.png')
        self.rect = self.image.get_rect()

    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        pygame.draw.rect(surf, white, (i * block_size, j * block_size, block_size, block_size))
        surf.blit(self.image, (i * block_size, j * block_size))


class box(content):
    def __init__(self):
        self.image = pygame.image.load('assets/box.png')
        self.rect = self.image.get_rect()

    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        surf.blit(self.image, (i * block_size, j * block_size))


class empty(content):
    def draw(self, surf, pos, block_size):
        pass


class key(content):
    def __init__(self):
        self.image = pygame.image.load('assets/key.png')
        self.rect = self.image.get_rect()

    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        surf.blit(self.image, (i * block_size + 10, j * block_size + 10))


class lock(content):
    def __init__(self):
        self.image = pygame.image.load('assets/lock.png')
        self.rect = self.image.get_rect()

    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        surf.blit(self.image, (i * block_size, j * block_size))


class star(content):
    def __init__(self):
        self.image = pygame.image.load('assets/cake.png')
        self.rect = self.image.get_rect()

    def draw(self, surf, pos, block_size):
        i = pos[0]
        j = pos[1]
        surf.blit(self.image, (i * block_size + 12, j * block_size + 12))


class player(content):
    def __init__(self):
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()

    def get_color(self):
        return blue_light

    def move(self, level, keys, locks):
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
            next_next_elm = level[(i + 2 * dir_x, j + 2 * dir_y)]
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
                if isinstance(current, door):
                    current.content = rock()
                    next_elm.content = self
                    next_next_elm.content = box()
                else:
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
                    time.sleep(0.1)
                    return -1, 0, c_key

                elif keys[pygame.K_RIGHT]:
                    time.sleep(0.1)
                    return 1, 0, c_key

                elif keys[pygame.K_UP]:
                    time.sleep(0.1)
                    return 0, -1, c_key

                elif keys[pygame.K_DOWN]:
                    time.sleep(0.1)
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
        surf.blit(self.image, (i * block_size + 6, j * block_size + 6))