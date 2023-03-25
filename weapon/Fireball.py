import tools
from TextureSet import TextureSet
from lifeform import LifeForm
from stats import Stats
from weapon.weapon import Weapon

class Fireball(Weapon):
    def __init__(self, lifeForm, target, entityMaster):
        super().__init__(lifeForm, "fireball", Stats(0, 0, 1, 1, 0, 0, 250, 250), 0, entityMaster)
        self.target = target

    def get_current_texture(self):
        return self.textures.textures[self.direction]

    def tick(self, dt):
        self.direction = tools.nearest_90(tools.direction(self.x, self.y, *self.target))
        if self.direction == "n":
            self.y -= self.stats.speed * dt

        if self.direction == "e":
            self.x += self.stats.speed * dt

        if self.direction == "s":
            self.y += self.stats.speed * dt

        if self.direction == "w":
            self.x -= self.stats.speed * dt

        if tools.direction(self.x, self.y, *self.target) < self.stats.speed:
            self.remove = True
            for entity in self.entityMaster.entities:
                if isinstance(entity, LifeForm):
                    if entity.collides_with(self):
                        if entity not in self.attacked:
                            entity.deal_damage(self)