import time
import pygame, sys, threading
from settings import Settings
from start import Start

pygame.init()
setting = Settings()

# Screen and font
screen = pygame.display.set_mode(setting.screen_size)
pygame.display.set_caption("ChiChi World")

# Clock
CLOCK = pygame.time.Clock()

# Work
WORK = 20000000

# Loading BG
LOADING_BG = pygame.image.load('assets/Loading Bar Background.png')
LOADING_BG_RECT = LOADING_BG.get_rect(center=(540, 500))

# Loading Bar and variables
loading_bar = pygame.image.load('assets/Loading Bar.png')
loading_bar_rect = loading_bar.get_rect(midleft=(340, 500))
loading_finished = False
loading_progress = 0
loading_bar_width = 8

def doWork():
	# Do some math WORK amount times
	global loading_finished, loading_progress

	for i in range(WORK):
		loading_progress = i 

	loading_finished = True

# Thread
threading.Thread(target=doWork).start()

# Game loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill(setting.background_color)

	loading = setting.font.render("Loading ...", 1, (255,255,255))
	screen.blit(loading, (435, 400))
    
	if not loading_finished:
		loading_bar_width = loading_progress / WORK * 400

		loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 70))
		loading_bar_rect = loading_bar.get_rect(midleft=(340, 500))

		screen.blit(LOADING_BG, LOADING_BG_RECT)
		screen.blit(loading_bar, loading_bar_rect)
	else:
		time.sleep(0.5)
		Start(screen)

	pygame.display.update()
	CLOCK.tick(60)