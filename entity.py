class Entity:
    def __init__(self, x, y, direction, textures):
        self.x = x
        self.y = y
        self.direction = direction
        self.textures = textures

    def get_current_texture(self):
        return self.textures.defaultTexture()

    @property
    def size(self):
        return (self.get_current_texture().get_width(), self.get_current_texture().get_height())

    def tick(self, dt):
        pass

    def handle_keys(self, keys, dt):
        pass