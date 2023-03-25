import pygame
import sys
from entityHandler import EntityHandler
from camera import Camera
from entity import Entity
import loader
from TextureSet import TextureSet
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Out of this World")

camera = Camera(0, 0)
entityHandler = EntityHandler(camera)
player = Player(0, 0, "e")
entityHandler.add_entity(player)
entityHandler.add_entity(Entity(0, 0, "n", TextureSet.load_from_folder("player")))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.get_time()/1000
    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    entityHandler.render(screen)
    entityHandler.tick(dt)
    entityHandler.handle_keys(keys, dt)
    camera.follow(player)
    clock.tick()
    pygame.display.flip()

pygame.quit()
sys.exit()