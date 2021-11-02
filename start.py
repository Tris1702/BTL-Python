import pygame
from menu import Menu
import nextbutton
from settings import Settings


class Start:
    def __init__(self, surf):
        self.surf = surf
        self.setting = Settings()

        #load button images
        self.start_img = pygame.image.load('assets/start_btn.png')
        self.exit_img = pygame.image.load('assets/exit_btn.png')

        #create button instances
        self.start_button = nextbutton.Nextbutton(100, 200, self.start_img, 0.8)
        self.exit_button = nextbutton.Nextbutton(450, 200, self.exit_img, 0.8)
        self.select()
        

    def run(self, surf):
        surf.fill(self.setting.background_color)

        if self.start_button.draw(surf):
            Menu(surf)
        if self.exit_button.draw(surf):
            pygame.quit()
        
        pygame.display.update()
    
    def select(self):
        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
            self.run(self.surf)
        
        

    