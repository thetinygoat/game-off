import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('test game')
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)

carImg = pygame.image.load('car.png')

def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def gameloop():
	x = (display_width * .45)
	y = (display_height * .45)
	x_change = 0
	car_width = 50
	game_exit = False
	while not game_exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
			
			x += x_change
			gameDisplay.fill(white)
			car(x,y)
			if x > display_width - car_width or x < 0:
				game_exit = True
			print(event)
			pygame.display.update()
			clock.tick(60)
gameloop()
pygame.quit()
quit()