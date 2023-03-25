import pygame
import sys
# import GUI
from entityHandler import EntityHandler
from camera import Camera
from entity import Entity
import loader
from TextureSet import TextureSet
from monster.Final import Final
from monster.PlainsGoblins import PlainsGoblin
from player import Player
from cutscene import Cutscene
from weapon.lightsaber import Lightsaber
from monster.FireSpirit import FireSpirit
from world import World
import tools

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Out of this World")

camera = Camera(0, 0)
World.init()
entityHandler = EntityHandler(camera)
player = Player(4000, 4000, "e")
weapon = Lightsaber(player, entityHandler)
final = Final(4000, 4000, player, entityHandler)
entityHandler.add_entity(player)
entityHandler.add_entity(weapon)
clock = pygame.time.Clock()
cutscene = Cutscene("assets/cutscenes/france_preview.gif", 0.9)
deathScreenAlpha = 0
deathScreen =loader.load_image("death", size=(800, 600))
world = World("Xargrave", "assets/images/plainsMap.png", (0, 0))
sound = ""
finalBoss = False

running = True
lastPlayer = (0, 0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            
    dt = clock.get_time()/1000
    keys = pygame.key.get_pressed()
    mousePos = pygame.mouse.get_pos()
    mousePressed = pygame.mouse.get_pressed()[0]
    screen.fill((0, 0, 0))
    screen.blit(loader.load_image("space", (800, 600)), (0, 0))
    if not finalBoss:
        world.render(camera, screen)
    entityHandler.render(screen)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, screen.get_height()-30, 100, 30))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, screen.get_height()-30, 100*player.stats.hp/player.stats.defaultHP, 30))
    if not finalBoss:
        if not world.canWalkInto(player.x, player.y):
            player.x = lastPlayer[0]
            player.y = lastPlayer[1]

        else:
            lastPlayer = (player.x, player.y)

    if not player.remove:
        entityHandler.tick(dt)
        entityHandler.handle_keys(keys, dt)
        entityHandler.handle_mouse(mousePos, mousePressed, dt)
        camera.follow(player)
        if not finalBoss:
            world.tick(camera, entityHandler, player)
        # cutscene.play(screen, dt)

    else:
        deathScreenAlpha += 128 * dt
        deathScreen.set_alpha(deathScreenAlpha)
        screen.blit(deathScreen, (0, 0))

    prevSound = sound
    if not finalBoss:
        if tools.dist(player.x, player.y, 4000, 4000) > 100:
            sound = "Ice Theme"

        if tools.dist(player.x, player.y, 4000, 4000) > 1500:
            sound = "Volcano Theme"

        if tools.dist(player.x, player.y, 4000, 4000) > 2500:
            sound = "Forest Theme"


    else:
        sound = "Final"

    if tools.dist(player.x, player.y, 4000, 4000) <= 100:
        if not finalBoss:
            entityHandler.add_entity(final)
        finalBoss = True

    # if sound != prevSound:
    #     pygame.mixer.stop()
    #     pygame.mixer.Sound.play(pygame.mixer.Sound(f'assets/audio/{sound}.wav'), loops=-1)

    clock.tick()
    pygame.display.flip()

pygame.quit()
sys.exit()