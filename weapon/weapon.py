from TextureSet import TextureSet
from entity import Entity


class Weapon(Entity):
    def __init__(self, lifeform, texture, stats, cooldown, entityMaster):
        super().__init__(lifeform.x, lifeform.y, lifeform.direction, TextureSet.load_from_folder(texture))
        self.lifeform = lifeform
        self.stats = stats
        self.cooldown = 0
        self.defaultCooldown = cooldown
        self.entityMaster = entityMaster
    





