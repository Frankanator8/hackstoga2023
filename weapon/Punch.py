import tools
from TextureSet import TextureSet
from lifeform import LifeForm
from stats import Stats
from weapon.weapon import Weapon

class Punch(Weapon):
    def __init__(self, lifeForm, target, entityMaster):
        super().__init__(lifeForm, TextureSet.load_from_folder("punch", size=(64, 64)), Stats(0, 0, 3, 3, 0, 0, 0, 0), 0, entityMaster)
        self.target = target
        self.wait = False

    def get_current_texture(self):
        return self.textures.textures["punch"]

    def tick(self, dt):
        if not self.wait:
            for entity in self.entityMaster.entities:
                if isinstance(entity, LifeForm):
                    if entity.collides_with(self):
                        if entity != self.lifeform:
                            entity.deal_damage(self)

        if self.wait:
            self.remove = True
        self.wait = True
