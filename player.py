import pygame

from lifeform import LifeForm
import loader
from TextureSet import TextureSet
from stats import Stats
class Player(LifeForm):
    def __init__(self, x, y, dir):
        super().__init__(x, y, dir, TextureSet.load_from_folder("player3", size=(128, 128)), Stats(40, 40, 10, 10, 10, 10, 100, 100))
        self.animationCycle = 1
        self.timeSinceLastAnimationChange = 0

    def tickAnimation(self):
        self.animationCycle += 1
        if self.animationCycle >= 5:
            self.animationCycle = 1
    def tick(self, dt):
        if self.timeSinceLastAnimationChange >= 0.25:
            self.timeSinceLastAnimationChange = 0
            self.tickAnimation()

    def get_current_texture(self):
        return self.textures.textures[f"main_{self.direction}{self.animationCycle}"]

    def handle_keys(self, keys, dt):
        pressed = False
        if keys[pygame.K_w]:
            self.direction = "n"
            self.y -= self.stats.speed * dt
            self.timeSinceLastAnimationChange += dt
            pressed = True

        if keys[pygame.K_s]:
            self.direction = "s"
            self.y += self.stats.speed * dt
            self.timeSinceLastAnimationChange += dt
            pressed = True

        if keys[pygame.K_a]:
            self.direction = "w"
            self.x -= self.stats.speed * dt
            self.timeSinceLastAnimationChange += dt
            pressed = True

        if keys[pygame.K_d]:
            self.direction = "e"
            self.x += self.stats.speed * dt
            self.timeSinceLastAnimationChange += dt
            pressed = True

        if not pressed:
            self.animationCycle = 1
