
# buttons https://pythonprogramming.altervista.org/buttons-in-pygame/?doing_wp_cron=1666639051.2411849498748779296875
# - I altered the buttons heavily and debugged screen flashing errors
# sources
# getting mouse position: https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pos
# shorthand for loops (used in getting mouse collision with sprite): https://stackoverflow.com/questions/6475314/python-for-in-loop-preceded-by-a-variable


# import libraries and modules
# from platform import platform

from arcade import PointList
import pygame
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import sys

vec = pg.math.Vector2
MOB_FRICK = 0.1
multiplier = 1

# game settings 
WIDTH = 600
HEIGHT = 800
FPS = 30
mpos = (0,0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
fpsClock = pygame.time.Clock()

# player settings
PLAYER_GRAV = 0.9
PLAYER_FRIC = 0.1
SCORE = 0
MOB_FRIC = 0.1
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#added variables, speed is not used, speedVar is used in buttons to change class settings
SPEED = vec(0,0)
speedVar = 1


#initiates the font function to create the buttons

pygame.init()

font = pygame.font.SysFont('arial', 10)

objects = []

# cretes button class and establishs attributes
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

#method for reading whether or not the button is pressed
    def process(self):
#gets mouse position
        mousePos = pygame.mouse.get_pos()
        #changes button ui based on if you're hovering
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
#reads for mouse press
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
#one click = ine click 
                if self.onePress:
                    self.onclickFunction()
# checks if it is already pressed
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

#different button functions
def speedUp():
    global speedVar
    global SCORE
    if SCORE >= 1:
        print('Speed Increased!')
        speedVar += 1
        SCORE -= 1
#called when button pressed, checks for neccesary score, adds a mob, removes score (cost)
def spawnMob():
    global SCORE
    global m
    if SCORE >= 20:
        m = Mob(randint(0,WIDTH), randint(0,HEIGHT), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
        all_sprites.add(m)
        mobs.add(m) 
        SCORE -= 20
    
# increasese multiplier - same process as above
def multUp():
    global multiplier
    global SCORE 
    if SCORE == 10:
        multiplier += 1
        SCORE -= 10
    
    

#instantiates buttons 
customButton = Button(30, 30, WIDTH/3, HEIGHT/12, 'Upgrade Speed! +(1) COST: 1', speedUp)
customButton = Button(30, 140, WIDTH/3, HEIGHT/12, 'Spawn 1 Mob! COST: 20!', spawnMob)
customButton = Button(30, 250, WIDTH/3, HEIGHT/12, 'Upgrade Spawn Multiplier! COST: 10', multUp)

#function for text on button
def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

def colorbyte():
    return random.randint(0,255)

# sprites...
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = SPEED
        self.speed = 5
    def controls(self):
        keys = pg.key.get_pressed()
        # if keys[pg.K_w]:
        #     self.acc.y = -5
        if keys[pg.K_a]:
            self.acc.x = -speedVar
        # if keys[pg.K_s]:
        #     self.acc.y = 5
        if keys[pg.K_d]:
            self.acc.x = speedVar
        if keys[pg.K_w]:
            self.acc.y = -speedVar
        if keys[pg.K_s]:
            self.acc.y = speedVar
    #not used
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, all_plats, False)
        self.rect.x += -1
        if hits:
            self.vel.y = -25
        
        

#update function
    def update(self):
       
        self.acc = vec(0,0)
        self.controls()
        # friction
        self.acc.x += self.vel.x * -0.1
        # self.acc.y += self.vel.y * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.rect.midbottom = self.pos
# creates my borders 
        if self.rect.x > WIDTH:
            #self.rect.x -= 1
            self.vel.x -= 5
        if self.rect.x <= 0:
            self.vel.x = 5
        if self.rect.y > HEIGHT:
            self.vel.y -= 5
        if self.rect.y < 0:
            self.vel.y = 5
        

    

        
        

# platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# enemy class 
class Mob(Sprite):
    def __init__(self, x, y, w, h, color,):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.acc = vec(0,0)
        self.speed = 5
    
    def update(self):
        
        self.rect.x += self.speed 
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.speed *= -1

        self.rect.y += self.speed
        if self.rect.y > HEIGHT or self.rect.y < 0:
            self.speed *= -1
        
        if hits:
            pass
        

        
        
# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
# create groups
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()

# instantiate classes
player = Player()
plat = Platform(WIDTH/200, HEIGHT/30, 800, 10)
#plat2 = Platform(WIDTH/500, HEIGHT/700, 200, 10)


for i in range(1):
    m = Mob(randint(0,WIDTH), randint(0,HEIGHT), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
    all_sprites.add(m)
    mobs.add(m)
    # print(m)

# add player to all sprites group
all_sprites.add(player)
all_plats.add(plat)

# add platform to all sprites group
all_sprites.add(plat)
#all_sprites.add(plat2)

# add things to their respective groups



# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)

    hits = pg.sprite.spritecollide(player, all_plats, False)
    #if hits:
        # print("ive struck a plat")
        #player.vel.y = 0
    mobhits = pg.sprite.spritecollide(player, mobs, True)
    
    if mobhits:
        print("ive struck a mob")
        SCORE += 1
        for i in range(multiplier):
            m = Mob(randint(0,WIDTH), randint(0,HEIGHT), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
            all_sprites.add(m)
            mobs.add(m) 
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for object in objects:
        object.process()

    pygame.display.flip()
    fpsClock.tick(FPS)
        
        
    
    
        

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
        # check for mouse
        if event.type == pg.MOUSEBUTTONUP:
            mpos = pg.mouse.get_pos()
            print(mpos)
            # get a list of all sprites that are under the mouse cursor
            clicked_sprites = [s for s in mobs if s.rect.collidepoint(mpos)]
            for m in mobs:
                if m.rect.collidepoint(mpos):
                    print(m)
                    m.kill()
            # print(clicked_sprites)k 
        # check for keys
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()
        
    ############ Update ##############
    # update all sprites
    all_sprites.update()

    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    # draw text
    draw_text("POINTS: " + str(SCORE), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    # draw all sprites
    all_sprites.draw(screen)

    # buffer - after drawing everything, flip display
    
pg.display.flip()
pg.quit()