from entity import Entity

class World(Entity):
    def __init__(self, id, texture, collision_texture, spawn_point):
        super().__init__(0, 0, texture, "e")
        self.spawn_point = spawn_point
        self.collision_texture = collision_texture
        self.id = id