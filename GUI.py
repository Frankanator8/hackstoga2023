import pygame
import loader
loadingImage = loader.loadImage("loadingImage.py")
startingImage = loader.loadImage("startingImage.py")
def draw(screen, mode):
    font = pygame.font.SysFont('Times new Roman', 30)
    buttons = []
    if(mode=='loading'):
        screen.blit(loadingImage, (500,500))
    elif(mode=='starting'):
        buttons = []
        start = pygame.draw.rect(screen, 'green', (500,500,100,100))
        buttons.append(start)