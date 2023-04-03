import random
import sys
import pygame

pygame.init()
# parametres screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
# parametres game
STEP = 5
ENEMTY_STEP = 5
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# score
cnt = 0
SCORE = 0
kk = True
SCORE_COINS = 0
score_font = pygame.font.SysFont("Verdana", 20)
# fps
FPS = 60
clock = pygame.time.Clock()
# sounds

# screen
SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer by Dima v1.0")
pygame.display.set_icon(pygame.image.load('images\main_icon.jpg'))
bg = pygame.image.load("images/AnimatedStreet.png")

# enemy parametres


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):
        global SCORE, ENEMTY_STEP, kk
        self.rect.move_ip(0, ENEMTY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# player parametres


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 550)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_a]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_d]:
                self.rect.move_ip(STEP, 0)

        if self.rect.top > 0:
            if pressed_keys[pygame.K_w]:
                self.rect.move_ip(0, -STEP)

        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[pygame.K_s]:
                self.rect.move_ip(0, STEP)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images\coin_icon.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 350), random.randint(250, 500))

    def update(self):
        global cnt
        if cnt == 0:
            self.rect.center = (random.randint(50, 350),random.randint(250, 500))
        elif cnt % 5 == 0:
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect.center = (random.randint(50, 350),random.randint(250, 500))
        else:
            self.image = pygame.transform.scale(self.image, (30, 30))
            self.rect.center = (random.randint(50, 350),random.randint(250, 500))

    def draw(self, surface):
        surface.blit(self.image, self.rect)


basic_sound = pygame.mixer.music.load(
    'sounds\Lil Jon & The Eastside Boyz - Get Low (Ost Need For Speed - Underground).mp3')
pygame.mixer.music.play(-1)


P1 = Player()
E1 = Enemy()
C1 = Coins()
enemies = pygame.sprite.Group()
enemies.add(E1)
en_c = pygame.sprite.Group()
en_c.add(C1)

# cycle
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.update()

    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound = pygame.mixer.music.load('sounds\w10_street racer_sounds_crash.wav')
        pygame.mixer.music.play(-1)
        pygame.quit()
        sys.exit()

    if cnt == 0 and pygame.sprite.spritecollideany(P1, en_c):
        SCORE_COINS += 1
        cnt += 1
        C1.update()
    elif pygame.sprite.spritecollideany(P1, en_c) and cnt % 5 == 0:
        SCORE_COINS += 5
        cnt += 1
        C1.update()
    elif pygame.sprite.spritecollideany(P1, en_c):
        SCORE_COINS += 1
        cnt += 1
        C1.update()

    if SCORE_COINS % 10 == 0 and SCORE_COINS != 0 and kk:
        ENEMTY_STEP += 2
        kk = False
    elif pygame.sprite.spritecollideany(P1, en_c):
        kk = True

    SURF.blit(bg, (0, 0))

    E1.draw(SURF)
    P1.draw(SURF)
    C1.draw(SURF)

    score_img = score_font.render(str(SCORE_COINS), True, BLACK)
    SURF.blit(score_img, (10, 10))

    pygame.display.update()
    clock.tick(FPS)
