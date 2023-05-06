import pygame
import opensimplex

from pygame.locals import *
#Important global variables
TILE_SIZE = 16
ZOOM_LEVEL = 0.1
SCREEN_HEIGHT = 640
SCREEN_WIDTH = 1280
SHIFT_VERTICAL = 0
SHIFT_HORIZONTAL = 0
SHIFT_STEP = 5

#HELPER METHODS
def getCoords(x, y):
    return (x * TILE_SIZE, y * TILE_SIZE)

def drawMap():
    for x in range(int(SCREEN_WIDTH/TILE_SIZE)):
        for y in range(int(SCREEN_HEIGHT/TILE_SIZE)):
            #water
            win.blit(waterImg, getCoords(x, y))
            noiseResult = opensimplex.noise2((x + SHIFT_HORIZONTAL)*ZOOM_LEVEL, (y + SHIFT_VERTICAL)*ZOOM_LEVEL)
            #deep water
            if (noiseResult < -0.3):
                win.blit(darkenImg, getCoords(x, y))
            #normal dirt
            if (noiseResult > 0):
                win.blit(dirtImg, getCoords(x, y))
                #light dirt
                if (noiseResult > 0.18):
                    win.blit(lightenImg, getCoords(x,y))
                    #dark grass
                    if(noiseResult > 0.35):
                        win.blit(grassImg, getCoords(x,y))
                        win.blit(darkenImg, getCoords(x,y))
                        #light grass
                        if(noiseResult > 0.45):
                            win.blit(grassImg, getCoords(x,y))

#INIT PYGAME
pygame.init()
# (1280x1280) for 20(64x64) squares
win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("open noise test")

#LOAD ASSETS
waterImg = pygame.image.load("assets/water.png")
dirtImg = pygame.image.load("assets/dirt.png")
grassImg = pygame.image.load("assets/grass.png")
lightenImg = dirtImg.copy()
darkenImg = dirtImg.copy()
darkenImg.fill(pygame.Color(0,0,0,20))
lightenImg.fill(pygame.Color(255,255,255, 15))

#init simplex
opensimplex.random_seed()
drawMap()
            
pygame.display.flip()
status = True

while (status):
    for i in pygame.event.get():
        #handle keyboard input
        if i.type == KEYDOWN:
            if i.key == K_r:
                opensimplex.random_seed()
            elif i.key == K_w:
                SHIFT_VERTICAL -= SHIFT_STEP
            elif i.key == K_s:
                SHIFT_VERTICAL += SHIFT_STEP
            elif i.key == K_a:
                SHIFT_HORIZONTAL -= SHIFT_STEP
            elif i.key == K_d:
                SHIFT_HORIZONTAL += SHIFT_STEP
            elif i.key == K_e:
                ZOOM_LEVEL += 0.01
            elif i.key == K_q:
                ZOOM_LEVEL -= 0.01
                
            
            drawMap()
            pygame.display.flip()
        #quit game
        if i.type == pygame.QUIT:
            status = False
        
pygame.quit()