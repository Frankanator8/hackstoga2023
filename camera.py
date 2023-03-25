class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def follow(self, entity):
        self.x = entity.x
        self.y = entity.y