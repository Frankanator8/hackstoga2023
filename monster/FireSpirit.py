from TextureSet import TextureSet
from monster.monster import Monster
from stats import Stats
import tools
from weapon.Fireball import Fireball


class FireSpirit(Monster):
    def __init__(self, x, y, player, entityHandler):
        super().__init__(x, y, "e", TextureSet.load_from_folder("firespirit", size=(81, 81)), Stats(15, 15, 5, 5, 2, 2, 500, 500), player)
        self.animationCycle = 1
        self.timeSinceLastAnimationChange = 0
        self.entityHandler = entityHandler
        self.cooldown = 0
        self.timeSinceDirChange = 0

    def get_current_texture(self):
        return super().render_health_bar(self.textures.textures["fire spirit"])

    def tick(self, dt):
        self.timeSinceLastAnimationChange += dt
        if self.timeSinceLastAnimationChange > 0.1:
            self.animationCycle += 1

        if self.animationCycle >= 5:
            self.animationCycle = 1

        self.timeSinceDirChange += dt
        if tools.distEntity(self, self.player) > 1500:
            self.remove = True

        if tools.distEntity(self, self.player) > 200:
            if self.timeSinceDirChange > 1:
                self.direction = tools.nearest_90(tools.direction(self.x, self.y, self.player.x, self.player.y))
                self.timeSinceDirChange = 0

            if self.direction == "n":
                self.y -= self.stats.speed * dt

            if self.direction == "e":
                self.x += self.stats.speed * dt

            if self.direction == "s":
                self.y += self.stats.speed * dt

            if self.direction == "w":
                self.x -= self.stats.speed * dt

        else:
            if self.cooldown == 0:
                self.entityHandler.add_entity(Fireball(self, (self.player.x, self.player.y), self.entityHandler))
                self.cooldown = 1

            else:
                self.cooldown -= dt
                if self.cooldown <= 0:
                    self.cooldown = 0




