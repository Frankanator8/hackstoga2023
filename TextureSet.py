import os

import loader


class TextureSet:
    def __init__(self, **kwargs):
        self.textures = kwargs

    @classmethod
    def load_from_folder(cls, folder, size=None):
        texs = {}
        for file in os.listdir(f"assets/images/{folder}"):
            name = file.split(".")[0]
            texs[name] = loader.load_image(f"{folder}/{name}", size=size)

        return TextureSet(**texs)

    def defaultTexture(self):
        return self.textures[list(self.textures.keys())[0]]
