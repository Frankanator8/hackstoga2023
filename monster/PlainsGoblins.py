import tools
from TextureSet import TextureSet
from monster.monster import Monster
from stats import Stats
from weapon.Punch import Punch


class PlainsGoblin(Monster):
    def __init__(self, x, y, player, entityHandler):
        super().__init__(x, y, "e", TextureSet.load_from_folder("player1"), Stats(30, 30, 15, 15, 15, 15, 125, 125), player)
        self.entityHandler = entityHandler
        self.animationCycle = 1
        self.timeSinceLastAnimationChange = 0

    def get_current_texture(self):
        return super().render_health_bar(self.textures.textures[f"main_{self.direction}{self.animationCycle}"])
    def tick(self, dt):
        self.timeSinceLastAnimationChange += dt
        if self.timeSinceLastAnimationChange > 0.1:
            self.animationCycle += 1

        if self.animationCycle >= 5:
            self.animationCycle = 1

        if tools.distEntity(self, self.player) > 200:
            self.direction = tools.nearest_90(tools.direction(self.x, self.y, self.player.x, self.player.y))
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
                self.entityHandler.add_entity(Punch(self, (self.player.x, self.player.y), self.entityHandler))
                self.cooldown = 0.4

            else:
                self.cooldown -= dt
                if self.cooldown <= 0:
                    self.cooldown = 0
