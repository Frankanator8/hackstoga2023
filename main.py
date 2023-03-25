import pygame
import sys
# import GUI
from entityHandler import EntityHandler
from camera import Camera
from entity import Entity
import loader
from TextureSet import TextureSet
from player import Player
from cutscene import Cutscene

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Out of this World")

camera = Camera(0, 0)
entityHandler = EntityHandler(camera)
player = Player(0, 0, "e")
entityHandler.add_entity(player)
entityHandler.add_entity(Entity(0, 0, "n", TextureSet.load_from_folder("player")))
clock = pygame.time.Clock()
cutscene = Cutscene("assets/cutscenes/france_preview.gif", 0.9)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    dt = clock.get_time()/1000
    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    screen.blit(loader.load_image("space", (800, 600)), (0, 0))
    entityHandler.render(screen)
    entityHandler.tick(dt)
    entityHandler.handle_keys(keys, dt)
    camera.follow(player)
    cutscene.play(screen, dt)
    clock.tick()
    pygame.display.flip()

pygame.quit()
sys.exit()