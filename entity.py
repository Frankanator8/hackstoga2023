class Entity:
    def __init__(self, x, y, direction, textures):
        self.x = x
        self.y = y
        self.direction = direction
        self.textures = textures
        self.remove = False
    def get_current_texture(self):
        return self.textures.defaultTexture()

    @property
    def size(self):
        return (self.get_current_texture().get_width(), self.get_current_texture().get_height())

    def tick(self, dt):
        pass

    def handle_keys(self, keys, dt):
        pass

    def handle_mouse(self, mousePos, mousePressed, dt):
        pass

    def collides_with(self, entity):
        if self.x + self.size[0]/2 < entity.x - entity.size[0]/2 or self.x - self.size[0]/2 > entity.x + entity.size[0]/2 or \
            self.y + self.size[1]/2 < entity.y - entity.size[1]/2 or self.y - self.size[1]/2 > entity.y + entity.size[1]/2:
            return False

        else:
            return True




