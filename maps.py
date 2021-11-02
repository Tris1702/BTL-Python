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

    def get_level(self):
        return self.level

    def get_player(self):
        return p

class Map1(Map):
    def __init__(self):
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
        return "Level: 1"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0
    
    def get_lock(self):
        return 0

class Map2(Map):
    def __init__(self):
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)], 
            [road(r), road(e), road(e), road(e), road(e), road(r), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(r), road(r), road(e), road(e), road(e), road(r), road(s), road(r)],
            [road(r), road(e), road(e), road(r), road(r), road(r), road(e), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(s), road(r), road(e), road(r)],
            [road(r), road(e), road(e), road(r), road(e), road(e), road(r), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(e), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(e), road(e), road(e), road(r), road(e), road(p), road(r), road(r)],
            [road(r), road(s), road(e), road(r), flag(e), road(e), road(e), road(e), road(r), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
    ]
    def get_name(self):
        return "Level: 2"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)
    
    def get_key(self):
        return 0

    def get_lock(self):
        return 0

class Map3(Map):
    def __init__(self):
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)], 
            [road(r), road(s), road(e), road(e), road(r), road(e), road(e), road(e), road(s), road(r)],
            [road(r), road(r), road(r), road(e), road(e), road(e), road(r), door(e), road(r), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(r), road(r), road(e), road(r), road(r)],
            [road(r), road(e), road(r), road(r), road(r), flag(e), road(r), road(e), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(r), road(e), road(s), road(r), road(e), road(r)],
            [road(r), road(e), road(r), door(e), road(r), road(e), road(r), road(e), road(e), road(r)],
            [road(r), road(e), road(r), road(e), road(e), door(e), road(r), road(e), road(r), road(r)],
            [road(r), road(e), road(s), road(r), road(p), road(e), road(e), road(e), road(r), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
    ]
    def get_name(self):
        return "Level: 3"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)
    
    def get_key(self):
        return 0
    
    def get_lock(self):
        return 0

class Map4(Map):
    def __init__(self):
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)], 
            [road(r), flag(e), road(e), road(e), road(e), road(r), road(r), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(e), road(s), road(r), road(e), door(e), door(e), road(r)],
            [road(r), road(r), road(e), road(e), road(r), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(r), road(e), road(r), road(e), road(p), road(r), road(e), road(e), road(r)],
            [road(r), road(e), road(e), road(r), road(e), road(r), road(r), road(e), road(r), road(r)],
            [road(r), road(e), road(r), door(e), door(e), road(s), road(e), road(e), road(r), road(r)],
            [road(r), road(e), road(r), road(e), road(r), door(r), door(e), door(e), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(r), road(e), road(e), door(s), road(s), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
    ]
    def get_name(self):
        return "Level: 4"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0
    
class Map5(Map):
    def __init__(self):
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)], 
            [road(r), flag(e), road(e), road(e), road(e), road(r), road(r), road(e), road(e), road(r)],
            [road(r), road(r), road(r), road(e), road(s), road(r), road(e), door(e), door(e), road(r)],
            [road(r), road(r), road(e), road(e), road(r), road(e), road(e), road(r), road(e), road(r)],
            [road(r), road(r), road(e), road(r), road(e), road(p), road(r), road(e), road(e), road(r)],
            [road(r), road(e), road(e), road(r), road(e), road(r), road(r), road(e), road(r), road(r)],
            [road(r), road(e), road(r), door(e), door(e), road(s), road(e), road(e), road(r), road(r)],
            [road(r), road(e), road(r), road(e), road(r), door(r), door(e), door(e), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(r), road(e), road(e), door(s), road(s), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
    ]
    def get_name(self):
        return "Level: 5"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0

class Map6(Map):
    def __init__(self):
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)], 
            [road(r), road(e), road(k), road(s), road(r), road(e), road(e), road(e), road(r), road(r)],
            [road(r), road(l), road(r), road(r), road(r), road(s), road(r), road(e), road(e), road(r)],
            [road(r), road(e), road(e), road(e), road(e), road(l), road(r), road(r), road(e), road(r)],
            [road(r), road(r), road(r), road(r), road(e), road(r), road(r), road(r), flag(e), road(r)],
            [road(r), road(r), road(e), road(e), road(l), road(e), road(e), road(e), road(r), road(r)],
            [road(r), road(s), road(k), road(r), road(r), road(r), road(k), road(k), road(e), road(r)],
            [road(r), road(r), road(r), road(e), road(e), road(e), road(r), road(r), road(e), road(r)],
            [road(r), road(s), road(e), road(e), road(r), road(e), road(l), road(e), road(p), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
    ]
    def get_name(self):
        return "Level: 6"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 4

    def get_lock(self):
        return 4

class Map7(Map):
    def __init__(self):
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
        return "Level: 7"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 5

    def get_lock(self):
        return 6

class Map8(Map):
    def __init__(self):
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)], 
            [road(r), flag(e), road(e), road(r), road(e), road(l), door(k), road(l), door(s), road(r)],
            [road(r), road(r), road(l), road(l), road(e), door(k), road(l), door(e), road(l), road(r)],
            [road(r), road(k), road(r), road(r), road(e), road(r), door(s), road(r), door(k), road(r)],
            [road(r), road(e), road(e), road(e), road(e), door(e), road(l), door(e), road(l), road(r)],
            [road(r), road(r), road(r), road(e), road(r), road(r), door(k), road(r), door(e), road(r)],
            [road(r), road(e), road(e), door(e), road(p), road(e), door(e), road(r), road(e), road(r)],
            [road(r), road(e), road(r), road(r), road(r), road(r), road(e), door(e), road(e), road(r)],
            [road(r), road(s), road(e), door(e), door(e), road(e), road(e), road(r), road(k), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
    ]
    def get_name(self):
        return "Level: 8"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 6

    def get_lock(self):
        return 8

class Map9(Map):
    def __init__(self):
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
        return "Level: 9"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 5

    def get_lock(self):
        return 9

class Map10(Map):
    def __init__(self):
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)], 
            [road(r), road(s), road(r), flag(e), road(r), road(r), road(l), road(s), road(k), road(r)],
            [road(r), road(e), door(l), road(k), door(e), door(e), door(e), road(r), door(l), road(r)],
            [road(r), road(e), road(r), door(e), road(r), road(r), door(k), road(l), road(e), road(r)],
            [road(r), road(e), door(e), road(l), road(e), door(e), road(e), road(r), road(e), road(r)],
            [road(r), road(r), road(r), door(e), road(r), road(e), door(s), road(r), road(e), road(r)],
            [road(r), road(e), door(e), door(s), door(l), road(e), door(k), door(s), road(e), road(r)],
            [road(r), road(s), road(r), road(r), door(k), road(r), door(e), road(r), door(e), road(r)],
            [road(r), door(l), road(s), door(k), door(e), road(l), road(e), road(e), road(p), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
    ]
    def get_name(self):
        return "Level: 10"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 6

    def get_lock(self):
        return 8

class Map11(Map):
    
    def __init__(self):
        self.level = [
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)], 
            [road(r), flag(e), road(b), hole(e), road(r), road(r), road(r), road(r)],
            [road(r), road(e), road(e), hole(e), hole(e), road(p), road(r), road(r)],
            [road(r), road(e), road(e), road(r), road(r), road(b), road(r), road(r)],
            [road(r), road(r), road(e), road(e), road(r), road(e), road(e), road(r)],
            [road(r), road(r), road(b), road(e), road(e), road(e), road(e), road(r)],
            [road(r), road(r), road(e), road(e), road(r), road(r), road(r), road(r)],
            [road(r), road(r), road(r), road(r), road(r), road(r), road(r), road(r)]
    ]
    def get_name(self):
        return "Level: 11"

    def get_width(self):
        return len(self.level[0])

    def get_height(self):
        return len(self.level)

    def get_key(self):
        return 0

    def get_lock(self):
        return 0