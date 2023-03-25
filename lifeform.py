from entity import Entity

class LifeForm(Entity):
    def __init__(self, x, y, dir, textures, stats):
        super().__init__(x, y, dir, textures)
        self.stats = stats
