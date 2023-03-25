from lifeform import LifeForm
import pygame

class Monster(LifeForm):
    def __init__(self, x, y, dir, textures, stats, player):
        super().__init__(x, y, dir, textures, stats)
        self.player = player

    def render_health_bar(self, surface):
        newSurface = pygame.Surface((surface.get_width(), surface.get_height()+30), flags=pygame.SRCALPHA)
        newSurface.blit(surface, (0, 30))
        pygame.draw.rect(newSurface, (255, 0, 0), pygame.Rect(0, 0, surface.get_width(), 20))
        pygame.draw.rect(newSurface, (0, 255, 0), pygame.Rect(0, 0, surface.get_width() * self.stats.hp / self.stats.defaultHP, 20))
        return newSurface
