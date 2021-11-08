from entities import box, flag, road, rock, empty, player, key, star, door, lock, hole
from abc import ABC, abstractmethod

r = rock()
p = player()
e = empty()
k = key()
l = lock()
s = star()
b = box()


class Map(ABC):
    def __iter__(self):
        self.i = 0
        self.j = 0
        yield self

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_key(self):
        pass

    @abstractmethod
    def get_lock(self):
        pass

    @abstractmethod
    def set_lock_level(self, lock):
        pass

    @abstractmethod
    def get_lock_level(self):
        pass

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_player(self):
        return p


class Map1(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(e), road(r), road(r), road(e), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(r), road(r), road(r), road(r), road(r), road(e), road(r)],
            [road(r), road(r), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(e), road(r), road(e), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(r), flag(e), road(r)],
            [road(r), road(e), road(p), road(e), road(e), road(r), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "1"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map2(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(s), road(r), road(s), road(e), road(e), road(e), road(r), road(s), road(r)],
            [road(r), road(e), road(r), road(r), road(r), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(p), road(r), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(r), road(r), road(r), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(r), road(e), road(e), road(e), road(e), road(e), road(e), road(r)],
            [road(r), road(e), flag(e), road(r), road(e), road(r), road(e), road(e), road(r), road(r)],
            [road(r), road(e), road(r), road(e), road(e), road(r), road(r), road(e), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(s), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "2"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map3(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(s), road(e), road(e), road(e), road(e), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(s), road(r), road(e), road(r), road(s), road(r), road(e), road(e), road(r)],
            [road(r), road(e), road(e), door(e), road(e), road(e), door(e), road(e), road(r), road(r)],
            [road(r), road(e), road(r), road(e), road(r), road(r), road(r), road(e), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(r), road(r)],
            [road(r), road(r), road(r), road(r), road(e), road(r), door(e), road(e), road(e), road(r)],
            [road(r), flag(e), road(e), road(e), road(e), road(e), road(s), road(r), road(p), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "3"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map4(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(p), door(e), road(s), road(e), road(e), road(r), road(r)],
            [road(r), road(e), road(e), road(r), road(e), road(r), road(e), road(e), road(r), road(r)],
            [road(r), road(e), road(r), road(e), road(r), road(e), road(r), road(e), road(r), road(r)],
            [road(r), road(e), road(r), flag(e), road(e), road(e), road(r), road(e), road(r), road(r)],
            [road(r), door(e), road(e), road(r), road(e), road(r), road(e), road(e), road(r), road(r)],
            [road(r), road(s), door(e), road(e), door(e), road(e), road(e), road(e), road(s), road(r)],
            [road(r), road(r), door(e), road(r), road(r), road(r), door(e), road(r), road(r), road(r)],
            [road(r), road(r), road(s), road(e), road(e), road(e), road(e), road(e), road(r), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "4"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map5(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(p), road(e), door(s), road(e), road(e), door(s), road(e), door(s), road(r)],
            [road(r), road(e), road(r), road(e), road(r), road(r), road(e), road(r), road(e), road(r)],
            [road(r), door(s), road(e), door(e), road(e), road(e), door(s), road(e), door(s), road(r)],
            [road(r), road(e), road(r), road(e), road(r), road(r), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(r), road(e), road(r), road(r), road(e), road(r), road(e), road(r)],
            [road(r), door(s), road(e), door(s), road(e), road(e), door(e), road(e), door(s), road(r)],
            [road(r), road(e), road(r), road(e), road(r), road(r), road(e), road(r), road(e), road(r)],
            [road(r), door(s), road(e), door(s), road(e), road(e), door(s), road(e), flag(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "5"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map6(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(k), road(e), road(r), road(s), road(e), flag(e), road(r), road(k), road(r)],
            [road(r), road(s), road(l), road(e), road(r), road(l), road(r), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(e), road(e), road(e), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(e), road(r), road(r), road(e), road(p), road(r)],
            [road(r), road(k), road(e), road(e), road(l), road(e), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(r), road(e), road(e), road(e), road(e), road(e), road(r)],
            [road(r), road(l), road(r), road(r), road(r), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(k), road(e), road(s), road(r), road(e), road(r), road(s), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "6"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 4

    def get_lock(self):
        return 4

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map7(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(k), road(s), road(r), road(e), road(e), road(e), road(e), road(r)],
            [road(r), road(l), road(r), road(r), road(r), door(e), road(r), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(e), road(r), road(s), road(e), road(r)],
            [road(r), road(e), road(r), road(l), road(r), door(e), road(r), road(k), road(p), road(r)],
            [road(r), road(l), road(r), door(e), road(r), road(e), road(r), road(r), road(l), road(r)],
            [road(r), road(s), door(e), road(e), road(l), road(e), road(l), road(s), road(e), road(r)],
            [road(r), road(e), road(r), flag(e), road(r), road(e), road(r), road(e), road(e), road(r)],
            [road(r), door(s), road(k), door(k), road(r), road(s), road(r), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "7"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 4

    def get_lock(self):
        return 6

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map8(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(k), road(e), road(l), road(s), road(s), road(l), road(r), road(p), road(r)],
            [road(r), road(s), road(e), road(e), door(e), road(l), road(l), door(e), road(e), road(r)],
            [road(r), road(r), road(r), road(l), road(r), road(r), door(e), road(e), road(e), road(r)],
            [road(r), road(r), road(k), road(l), road(r), road(r), road(k), road(s), road(r), road(r)],
            [road(r), road(e), door(e), door(e), door(e), door(s), road(l), road(k), door(e), road(r)],
            [road(r), road(e), road(r), flag(e), road(k), door(e), road(r), road(l), road(l), road(r)],
            [road(r), road(e), road(r), door(e), road(r), road(r), road(k), road(l), road(s), road(r)],
            [road(r), road(s), door(e), road(s), road(e), road(e), road(l), road(r), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "8"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 6

    def get_lock(self):
        return 11

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map9(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(l), road(e), road(k), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(e), road(r), road(e), road(e), road(e), road(e), road(r), road(l), road(r)],
            [road(r), road(s), road(r), road(e), road(r), road(r), road(r), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(e), road(e), door(e), road(l), road(k), road(p), road(r)],
            [road(r), road(r), road(r), road(e), door(e), road(k), road(r), road(r), road(e), road(r)],
            [road(r), road(s), road(e), door(e), flag(e), road(r), road(s), road(r), road(l), road(r)],
            [road(r), road(l), road(r), road(r), road(r), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(k), road(k), road(e), road(l), road(e), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "9"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 5

    def get_lock(self):
        return 6

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map10(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(p), road(e), road(e), road(l), door(s), road(e), road(e), road(r), road(r)],
            [road(r), road(e), road(r), door(e), road(r), road(r), road(e), road(l), door(k), road(r)],
            [road(r), door(e), door(e), road(k), road(r), road(r), road(e), road(r), road(k), road(r)],
            [road(r), door(e), road(l), road(r), door(l), door(l), door(s), road(r), road(k), road(r)],
            [road(r), road(e), road(l), road(s), door(l), door(l), road(e), road(e), door(e), road(r)],
            [road(r), door(e), door(s), road(r), road(l), road(s), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(r), road(e), door(k), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(e), road(e), road(e), door(s), road(e), road(r), flag(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "10"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 5

    def get_lock(self):
        return 9

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map11(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(e), road(r), road(e), flag(e), road(r)],
            [road(r), road(e), road(e), road(r), road(r), road(e), road(b), door(e), door(e), road(r)],
            [road(r), road(s), road(e), road(r), road(r), road(e), road(r), road(r), road(e), road(r)],
            [road(r), road(e), road(b), road(p), road(e), road(e), road(s), road(e), road(b), road(r)],
            [road(r), road(e), road(r), road(b), road(r), door(e), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(r)],
            [road(r), road(b), road(r), road(r), road(r), door(e), road(r), road(e), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(e), road(e), road(e), road(s), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "11"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map12(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(b), hole(e), road(r), road(r), road(r), road(r)],
            [road(r), road(e), flag(e), hole(e), hole(e), road(p), road(r), road(r)],
            [road(r), road(e), road(e), road(r), road(r), road(b), road(r), road(r)],
            [road(r), road(r), road(e), road(e), road(r), road(e), road(e), road(r)],
            [road(r), road(r), road(b), road(e), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(e), road(e), road(r), road(r), road(r), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "12"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map13(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(e), road(r), road(r), road(e), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(r), road(r), road(r), road(r), road(r), road(e), road(r)],
            [road(r), road(r), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(e), road(r), road(e), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(r), flag(e), road(r)],
            [road(r), road(e), road(p), road(e), road(e), road(r), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "13"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map14(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(e), road(r), road(r), road(e), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(r), road(r), road(r), road(r), road(r), road(e), road(r)],
            [road(r), road(r), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(e), road(r), road(e), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(r), flag(e), road(r)],
            [road(r), road(e), road(p), road(e), road(e), road(r), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "14"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map15(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(e), road(r), road(r), road(e), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(r), road(r), road(r), road(r), road(r), road(e), road(r)],
            [road(r), road(r), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(e), road(r), road(e), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(r), flag(e), road(r)],
            [road(r), road(e), road(p), road(e), road(e), road(r), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "15"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level


class Map16(Map):
    def __init__(self):
        self.lock_level = False
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(e), road(r), road(r), road(e), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(r), road(r), road(r), road(r), road(r), road(e), road(r)],
            [road(r), road(r), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(e), road(r), road(e), road(r), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(r), flag(e), road(r)],
            [road(r), road(e), road(p), road(e), road(e), road(r), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
        ]

    def get_name(self):
        return "16"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

    def set_lock_level(self, lock):
        self.lock_level = lock

    def get_lock_level(self):
        return self.lock_level