import loader
from entity import Entity
import math
from PIL import Image
import random

from monster.FireSpirit import FireSpirit
from monster.PlainsGoblins import PlainsGoblin


class World:
    TILE_SIZE = 200
    @classmethod
    def init(cls):
        World.CG = loader.load_image("corrupted_grass", size=(World.TILE_SIZE, World.TILE_SIZE))
        World.G = loader.load_image("grass", size=(World.TILE_SIZE, World.TILE_SIZE))
        World.T = loader.load_image("tree", size=(World.TILE_SIZE, World.TILE_SIZE))
        World.R = loader.load_image("rock", size=(World.TILE_SIZE, World.TILE_SIZE))

    def __init__(self, id, texture, spawn_point):
        self.texture = texture
        self.spawn_point = spawn_point
        self.id = id
        self.image = Image.open(texture)
        w, h = self.image.size
        self.imageData = []
        for x in range(h):
            self.imageData.append([])
            for y in range(w):
                self.imageData[-1].append(self.image.getpixel((y, x)))



    def render(self, camera, screen):
        cameraX = camera.x//World.TILE_SIZE
        cameraY = camera.y//World.TILE_SIZE
        for x in range(-5, 6):
            for y in range(-5, 6):
                pixelX = int(cameraX + x)
                pixelY = int(cameraY + y)
                color = self.imageData[pixelY][pixelX]
                if color == (47, 54, 153, 255):
                    img = World.CG

                elif color == (156, 24, 22, 255):
                    img = World.T

                elif color == (255, 163, 177, 255):
                    img = World.R

                else:
                    img = World.G

                trueX = pixelX * World.TILE_SIZE - camera.x + screen.get_width()/2 - img.get_width()/2
                trueY = pixelY * World.TILE_SIZE - camera.y + screen.get_height()/2 - img.get_height()/2
                screen.blit(World.G, (trueX, trueY))
                screen.blit(img, (trueX, trueY))

    def tick(self, camera, entityHandler, player):
        cameraX = camera.x//World.TILE_SIZE
        cameraY = camera.y//World.TILE_SIZE
        for x in range(-2, 3):
            for y in range(-2, 3):
                pixelX = int(cameraX + x)
                pixelY = int(cameraY + y)
                color = self.imageData[pixelY][pixelX]
                if color == (47, 54, 153, 255):
                    if random.randint(1, 1000) == 69:
                        entityHandler.add_entity(PlainsGoblin(pixelX * World.TILE_SIZE+random.randint(-World.TILE_SIZE/2, World.TILE_SIZE/2), pixelY * World.TILE_SIZE+random.randint(-World.TILE_SIZE/2, World.TILE_SIZE/2), player, entityHandler))

                    if random.randint(1, 1000) == 420:
                        entityHandler.add_entity(FireSpirit(pixelX * World.TILE_SIZE+random.randint(-World.TILE_SIZE/2, World.TILE_SIZE/2), pixelY * World.TILE_SIZE+random.randint(-World.TILE_SIZE/2, World.TILE_SIZE/2), player, entityHandler))

    def canWalkInto(self, x, y):
        X = int((x+(World.TILE_SIZE/2))//World.TILE_SIZE)
        Y = int((y+(World.TILE_SIZE/2))//World.TILE_SIZE)
        if X < 0 or X >= len(self.imageData[0]) or Y<0 or Y>=len(self.imageData):
            return False
        return (self.imageData[Y][X] not in [(156, 24, 22, 255), (255, 163, 177, 255)])

