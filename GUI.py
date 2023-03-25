import pygame
import loader
startingImage = loader.loadImage("startingImage.py")
def draw(screen, mode, frame):
    font = pygame.font.SysFont('Times new Roman', 30)
    buttons = []
    if(mode=='loading'):
        frameGap = 10
        loadingImage1 = loader.loadImage("BackgroundAmimation/loadingImage.py")
        
        screen.blit(loadingImage1, (500,500))
        
        
        
    elif(mode=='starting'):
        buttons = []
        start = pygame.draw.rect(screen, 'green', (500,500,100,100))
        
        buttons.append(start)
        levelSelect = pygame.draw.rect(screen, 'red', (600,600,100,100))
