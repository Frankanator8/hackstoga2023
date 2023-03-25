from TextureSet import TextureSet
from lifeform import LifeForm
from stats import Stats
from weapon.weapon import Weapon

class Lightsaber(Weapon):
    def __init__(self, lifeform, entityMaster):
        super().__init__(lifeform, TextureSet.load_from_folder("lightsaber"), Stats(0, 0, 20, 20, 5, 5, 0, 0), 2, entityMaster)
        self.animationCycle = 0
        self.timeSinceLastAnimation = 0
        self.prevMouseClicked = False
        self.attacking = True
        self.entityMaster = entityMaster
        self.attacked = set()

    def tick(self, dt):
        self.y = self.lifeform.y
        if self.lifeform.direction in ["n", "e"]:
            self.direction = "e"
            self.x = self.lifeform.x + self.lifeform.size[0]/2 + self.size[0]/2

        else:
            self.direction = "w"
            self.x = self.lifeform.x - self.lifeform.size[0]/2 - self.size[0]/2

        if self.cooldown > 0:
            self.cooldown -= dt
            if (self.cooldown <= 0):
                self.cooldown = 0

        if self.attacking:
            self.timeSinceLastAnimation += dt
            if self.timeSinceLastAnimation > 0.1:
                self.timeSinceLastAnimation = 0
                self.animationCycle += 1

            if self.animationCycle == 4:
                self.animationCycle = 0
                self.attacking = False
                self.attacked = set()
                self.cooldown = 1

            for entity in self.entityMaster.entities:
                if isinstance(entity, LifeForm):
                    if entity.collides_with(self):
                        if entity not in self.attacked:
                            if entity != self.lifeform:
                                self.attacked.add(entity)
                                entity.deal_damage(self)


    def get_current_texture(self):
        return self.textures.textures[f"{self.direction}{self.animationCycle}"]


    def handle_mouse(self, mousePos, mousePressed, dt):
        if mousePressed:
            if not self.prevMouseClicked:
                if not self.attacking:
                    if self.cooldown == 0:
                        self.attacking = True

        self.prevMouseClicked = mousePressed

