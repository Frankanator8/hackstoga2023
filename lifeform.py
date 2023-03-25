from entity import Entity

class LifeForm(Entity):
    def __init__(self, x, y, dir, textures, stats):
        super().__init__(x, y, dir, textures)
        self.stats = stats

    def deal_damage(self, weapon):
        self.stats.hp -= 1 # round(weapon.stats.atk + weapon.lifeform.stats.atk * 0.2 - self.stats.defense)
        if self.stats.hp <= 0:
            self.remove = True
