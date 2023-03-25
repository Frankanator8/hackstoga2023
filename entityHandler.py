class entityHandler:
    def __init__(self, camera):
        self.entities = []
        self.camera = camera

    def add_entity(self, e):
        self.entities.append(e)

    def render(self, screen):
        pass