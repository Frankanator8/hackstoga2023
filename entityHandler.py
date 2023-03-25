class EntityHandler:
    def __init__(self, camera):
        self.entities = []
        self.camera = camera

    def add_entity(self, e):
        self.entities.append(e)

    def render(self, screen):
        camera = self.camera
        for entity in self.entities:
            trueX = entity.x - camera.x + screen.get_width()/2 - entity.size[0]/2
            trueY = entity.y - camera.y + screen.get_height()/2 - entity.size[1]/2
            screen.blit(entity.get_current_texture(), (trueX, trueY))

    def tick(self, dt):
        good = []
        for entity in self.entities:
            entity.tick(dt)
            if not entity.remove:
                good.append(entity)

        self.entities = good


    def handle_keys(self, keys, dt):
        for entity in self.entities:
            entity.handle_keys(keys, dt)

    def handle_mouse(self, mousePos, mousePressed, dt):
        for entity in self.entities:
            print(type(entity))
            entity.handle_mouse(mousePos, mousePressed, dt)

