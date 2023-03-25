import pygame
import sys
from entityHandler import EntityHandler
from camera import Camera
from entity import Entity

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Out of this World")

camera = Camera(0, 0)
entityHandler = EntityHandler(screen)
entityHandler.add_entity(Entity(0, 0, 0, ))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    entityHandler.render(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()