import pygame, sys, threading
from menu import Menu
from settings import Settings
from start import Start

pygame.init()
setting = Settings()

# Screen and font
screen = pygame.display.set_mode(setting.screen_size)
pygame.display.set_caption("BTL Diep - Trang - Hoa")

FONT = pygame.font.SysFont("Roboto", 100)

# Clock
CLOCK = pygame.time.Clock()

# Work
WORK = 20000000

# Loading BG
LOADING_BG = pygame.image.load('assets/Loading Bar Background.png')
LOADING_BG_RECT = LOADING_BG.get_rect(center=(540, 360))

# Loading Bar and variables
loading_bar = pygame.image.load('assets/Loading Bar.png')
loading_bar_rect = loading_bar.get_rect(midleft=(180, 360))
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

	if not loading_finished:
		loading_bar_width = loading_progress / WORK * 720

		loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
		loading_bar_rect = loading_bar.get_rect(midleft=(180, 360))

		screen.blit(LOADING_BG, LOADING_BG_RECT)
		screen.blit(loading_bar, loading_bar_rect)
	else:
		Start(screen)

	pygame.display.update()
	CLOCK.tick(60)
