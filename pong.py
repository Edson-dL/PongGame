import pygame

#SETUP
pygame.init()
clock = pygame.time.Clock()

screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width. screen_height))
pygame.display.set_caption("Juego de pong")

#RECTANGLES
ball = pygame.React(screen_width/2 -11, screen_height - 11,22,22)
player = pygame.React(screen_width/2 -20, screen_height/2 -60, 10, 120)
enemy = pygame.React(10, screen_height/2 -60,10,120)

bgColor = (25,25,25) #RGB RED, GREE, BLUE
objectColor = (115, 115, 115) #RGB

#LOOP
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill(bgColor)
	pygame.draw.rect(screen, objectColor, player) #Donde se va a mostrar
	pygame.draw.rect(screen, objectColor, enemy)
	pygame.draw.ellipse(screen, objectColor, ball)
	pygame.draw.aaline(screen, objectColor, (screen_width/2, 0), (screen_width/2, screen_width))#donde se va a poner, color, donde va a estar

	pygame.display.flip()
	clock.tick(60) #60 FPS
