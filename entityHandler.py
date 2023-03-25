class EntityHandler:
    def __init__(self, camera):
        self.entities = []
        self.camera = camera

    def add_entity(self, e):
        self.entities.append(e)

    def render(self, screen):
        camera = self.camera
        for entity in self.entities:
            trueX = entity.x - camera.x
            trueY = entity.y - camera.y
            screen.blit(entity.texture, (trueX, trueY))
