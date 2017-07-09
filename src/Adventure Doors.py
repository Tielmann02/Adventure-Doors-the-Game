import pygame, sys
from pygame.locals import *
pygame.init()
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height)) 
pygame.display.set_caption('Adventure Doors')
white = (255,255,255)
black = (0,0,0)

def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface,textSurface.get_rect()
    
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        mediumText = pygame.font.SysFont("monospace", 20)
        largeText = pygame.font.SysFont("monospace", 20)
        TextSurf, TextRect = text_objects("Adventure Doors", largeText)
        TextSurf, TextRect = text_objects("Enter if you dare..." ,mediumText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)


game_intro()
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
