import pygame 
import datetime 
import os
import math 
import time 
 
pygame.init() 
W = 1600 
H = 900 
screen = pygame.display.set_mode((W, H)) 
 
_image_library = {} 
 
 
def convert_degrees(R, theta): 
    y = math.cos(2*math.pi * theta/ 360) * R 
    x = math.sin(2*math.pi*theta/360) * R 
    return x+400, -(y - 400) 
 
 
def Rotate(surf, image, pos, originPos, angle): 
    angle %= 360 
    
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1])) 
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center 
     
    
    rotated_offset = offset_center_to_pivot.rotate(angle) 
 
   
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y) 
 
    
    rotated_image = pygame.transform.rotate(image, -angle) 
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center) 
 
    
    surf.blit(rotated_image, rotated_image_rect) 
   
   
 
def get_image(path): 
    global _image_library 
    image = _image_library.get(path) 
    if image is None: 
        _path = path.replace('/', os.sep).replace('\\', os.sep) 
        image = pygame.image.load(_path) 
        _image_library[path] = image 
    return image 
 
right_hand = pygame.image.load('right.png') 
 
 
left_hand = pygame.image.load('left.png') 
left_hand = pygame.transform.scale(left_hand, (230, 200)) 
 
angle_seconds = 6 
angle_minutes = 1/10 
 
date = datetime.datetime.now() 
seconds = date.second 
minutes = date.minute 
 
done = False 
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
 
    screen.fill((255, 255, 255)) 
    image = screen.blit(get_image('micky.png'), (150, -30)) 
 
    pos1 = (screen.get_width()/2 + 50, screen.get_height()/2 - 10) 
 
    pos2 = (screen.get_width()/2 - 80, screen.get_height()/2 - 15) 
 
    Rotate(screen, left_hand, pos1, (W/2 - 765, H/2 - 280), angle_seconds) 
 
    Rotate(screen, right_hand, pos2, (W/2 - 470, H/2 - 200), angle_minutes) 
 
    time.sleep(1) 
 
    angle_seconds+=6 
    angle_minutes+=1/10 
 
 
 
    pygame.display.update() 
 
pygame.quit()
