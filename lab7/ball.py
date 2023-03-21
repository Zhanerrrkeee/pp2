import pygame 
 
 
pygame.init() 


size = width, height = (500, 500) 
screen = pygame.display.set_mode(size) 

clock = pygame.time.Clock() 

done = False 
 
coordinats = [0, 0] 
radius = 25 
 
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: 
            coordinats[1] -= 20 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN: 
            coordinats[1] += 20 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: 
            coordinats[0] -= 20 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: 
            coordinats[0] += 20 
     
    coordinats[1] = max(radius, min(coordinats[1], height - radius)) 
    coordinats[0] = max(radius, min(coordinats[0], width - radius)) 
     
    screen.fill((255, 255, 255)) 
    pygame.draw.circle(screen, (255, 0, 0), coordinats, radius) 
    pygame.display.flip() 
    clock.tick(60)
