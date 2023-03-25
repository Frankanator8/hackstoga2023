from TextureSet import TextureSet
from lifeform import LifeForm
from stats import Stats
import weapon
class Lightsaber(weapon.Weapon):
    def __init__(self, lifeform, entityMaster):
        super().__init__(lifeform, TextureSet.load_from_folder("lightsaber"), Stats(0, 0, 10, 10, 5, 5, 0, 0))
        self.animationCycle = 0
        self.timeSinceLastAnimation = 0
        self.prevMouseClicked = False
        self.attacking = True
        self.entityMaster = entityMaster
        self.attacked = []

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
            if self.timeSinceLastAnimation > 0.25:
                self.timeSinceLastAnimation = 0
                self.animationCycle += 1

            if self.animationCycle == 4:
                self.animationCycle = 0
                self.attacking = False
                self.attacked = []
                self.cooldown = 1

            for entity in self.entityMaster.entities:
                if isinstance(entity, LifeForm):
                    if entity.collides_with(self):
                        self.attacked.append(entity)
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

