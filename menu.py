import pygame
import maps 
import map_run
import buttons
from settings import Settings

class Menu:
    def __init__(self, surf):
        self.settings = Settings()
        self.surf = surf
        self.buttons = []
        self.maps = [maps.Map1(), maps.Map2(), maps.Map3(), maps.Map4(), maps.Map5(), maps.Map6(), maps.Map7(), maps.Map8(), maps.Map9(), maps.Map10(), maps.Map11()]
        self.create_menu() 
        
        while True:
            self.selected_level = self.select_level()
            self.run_game(self.selected_level)

    def create_menu(self): 
        for i, m in enumerate(self.maps):
            button_width = self.settings.button_width
            spacing_width = self.settings.spacing_width
            if i < 5:
                tmp = i % 5
                spacing_height = self.settings.spacing_height
                self.buttons.append(buttons.Button(button_width, button_width, (1.5*tmp*button_width + spacing_width, spacing_height), m.get_name(), m))
            elif i < 10:
                tmp = i % 5
                spacing_height = self.settings.spacing_height + 200
                self.buttons.append(buttons.Button(button_width, button_width, (1.5*tmp*button_width + spacing_width, spacing_height), m.get_name(), m))
            elif i < 15:
                tmp = i % 5
                spacing_height = self.settings.spacing_height + 400
                self.buttons.append(buttons.Button(button_width, button_width, (1.5*tmp*button_width + spacing_width, spacing_height), m.get_name(), m)) 

    def select_level(self):
        not_selected = True
        sel_map = None
        while not_selected:
            pos = self.get_mouse_input()
            if pos:
                for butt in self.buttons:
                    sel_map = butt.check(pos)
                    if sel_map:
                        sel_map.__init__()
                        return sel_map
            self.re_make_selection_window(self.surf)


    def re_make_selection_window(self, surf):
        surf.fill((255, 255, 255))
        self.make_buttons(surf)
        pygame.display.update()
        

    def make_buttons(self, surf):
        for butt in self.buttons:
            butt.draw(surf)
            
    def run_game(self, map_to_play):
        map_run.RunMap(map_to_play, self.surf).run_map()
    
    def get_mouse_input(self):
        pos = None
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
        return pos