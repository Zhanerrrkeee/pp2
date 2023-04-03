import pygame
import math

#init 
pygame.init()

#screen
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Paint by Dima")
#tickrate
clock = pygame.time.Clock()

#colors
COLOR = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN  = (0,255,0)
BLUE = (0,0,255)
HZ = (0,255,255)
#cycle
screen.fill((255,255,255))
draw =  False 
shape = None
#icon
black_icon = pygame.image.load('icons\BLACK.png')
black_icon = pygame.transform.scale(black_icon,(30,30))
red_icon = pygame.image.load('icons\RED.png')
red_icon = pygame.transform.scale(red_icon,(30,30))
green_icon = pygame.image.load('icons\GREEN.png')
green_icon = pygame.transform.scale(green_icon,(30,30))
blue_icon = pygame.image.load('icons\BLUE.png')
blue_icon = pygame.transform.scale(blue_icon,(30,30))
circle_icon = pygame.image.load('icons\circle.png')
circle_icon = pygame.transform.scale(circle_icon,(30,30))
rect_icon = pygame.image.load('icons\square.png')
rect_icon = pygame.transform.scale(rect_icon,(30,30))
eraser_icon = pygame.image.load('icons\eraser.jpg')
eraser_icon = pygame.transform.scale(eraser_icon,(30,30))
#while loop
while True:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #control with mouse        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            color_pos = pygame.mouse.get_pos()
            if 30 >= color_pos[0] >= 0 and 30 >= color_pos[1] > 0:
                COLOR = RED
            elif  30 >= color_pos[0] >= 0 and 60 >= color_pos[1] > 30:
                COLOR = GREEN
            elif 30 >= color_pos[0] >= 0 and 90 >= color_pos[1] > 60:
                COLOR = BLUE
            elif 30 >= color_pos[0] >= 0 and 120 >= color_pos[1] > 90:
                    COLOR = BLACK 
            elif 30 >= color_pos[0] >= 0 and 150 >= color_pos[1] > 120:
                    shape = 1
            elif 30 >= color_pos[0] >= 0 and 180 >= color_pos[1] > 150:
                    shape = 2
            elif 30 >= color_pos[0] >= 0 and 210 >= color_pos[1] > 180:
                shape = 3
                                    
        #draw rectangle                       
        if shape == 1:      
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                draw = True
                pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEMOTION:
                if draw:
                    current_pos = pygame.mouse.get_pos()
                    width = abs(current_pos[0] - pos[0])
                    heigth = abs(current_pos[1] - pos[1])
                    pygame.draw.rect(screen,COLOR,(min(pos[0],current_pos[0]),min(pos[1],current_pos[1]),width,heigth))
            elif event.type == pygame.MOUSEBUTTONUP:
                draw = False
        #draw circle        
        if shape == 2:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                draw = True
                pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEMOTION:
                if draw:
                    current_pos = pygame.mouse.get_pos()
                    width = abs(current_pos[0] - pos[0])
                    heigth = abs(current_pos[1] - pos[1])
                    cx = (current_pos[0] + pos[0])/2
                    cy = (current_pos[1] + pos[1])/2
                    rc = math.sqrt((cx-current_pos[0])**2 + (cy-color_pos[1])**2)
                    pygame.draw.circle(screen,COLOR,(cx,cy),int(rc))
                    # pygame.draw.ellipse(screen,COLOR,(min(pos[0],current_pos[0]),min(pos[1],current_pos[1]),width,heigth))
            elif event.type == pygame.MOUSEBUTTONUP:
                draw = False
        #eraser        
        if shape == 3:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                draw = True
                pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEMOTION:
                if draw:
                    current_pos = pygame.mouse.get_pos()
                    width = abs(current_pos[0] - pos[0])
                    heigth = abs(current_pos[1] - pos[1])
                    
                    pygame.draw.ellipse(screen,(255,255,255),(min(pos[0],current_pos[0]),min(pos[1],current_pos[1]),width,heigth))
            elif event.type == pygame.MOUSEBUTTONUP:
                draw = False    

                                     
                
    #main screen 
    screen.blit(red_icon,(0,0))
    screen.blit(green_icon,(0,30))
    screen.blit(blue_icon,(0,60))
    screen.blit(black_icon,(0,90))
    screen.blit(rect_icon,(0,120))
    screen.blit(circle_icon,(0,150))
    screen.blit(eraser_icon,(0,180))
    
                   
    #flip
    pygame.display.flip()
    clock.tick(60)
pygame.quit()  
