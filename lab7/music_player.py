import os 
import pygame  
 
music = [] 
 
for root, dirs, files in os.walk(os.getcwd()): 
 for file in files: 
  if '.mp3' in file: 
   music.append(file) 
 
pygame.init() 
screen = pygame.display.set_mode((400,400)) 
pygame.display.set_caption('Music mixer') 
 
SONG_END = pygame.USEREVENT + 1 
 
pygame.mixer.music.set_endevent(SONG_END) 


 
i = 0 
 
done = False 
while not done: 
 for event in pygame.event.get(): 
  if event.type == pygame.QUIT: 
   done = True 
  if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
   print('Starting playing ...') 
   pygame.mixer.music.load(music[i]) 
   pygame.mixer.music.play() 
  if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: 
   print('Playing next song...') 
   pygame.mixer.music.stop() 
   i += 1 
   if len(music) <= i: 
    i = 0 
 
   pygame.mixer.music.load(music[i]) 
   pygame.mixer.music.play() 
  if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: 
   print('Playing previous song...') 
   pygame.mixer.music.stop() 
   i -= 1 
   if i < 0: 
    i = len(music) - 1 
   pygame.mixer.music.load(music[i]) 
   pygame.mixer.music.play() 
  if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN: 
   print('Music has stopped') 
   pygame.mixer.music.stop() 
 
 screen.fill((255, 255, 255)) 
 
 
 pygame.display.flip() 
 
pygame.quit()


