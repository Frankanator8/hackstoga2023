from lifeform import LifeForm


class Monster(LifeForm):
    def __init__(self, x, y, dir, textures, stats):
        super().__init__(x, y, dir, textures, stats)