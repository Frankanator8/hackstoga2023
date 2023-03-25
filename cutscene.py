import PIL
import pygame
from PIL import Image, ImageSequence
class Cutscene:
    def __init__(self, gif, frameRate):
        self.frames = []
        self.prepare_gif(gif)
        self.frame = 0
        self.frameRate = frameRate
        self.timeSinceLastFrame = 0
        self.finished = False

    def convert_to_surface(self, pilImage):
        mode, size, data = pilImage.mode, pilImage.size, pilImage.tobytes()
        return pygame.image.fromstring(data, size, mode).convert_alpha()

    def prepare_gif(self, name): # copied from a before
        pilImage = Image.open(name)
        self.frames = []
        if pilImage.format == "GIF" and pilImage.is_animated:
            for frame in ImageSequence.Iterator(pilImage):
                pygameImage = self.convert_to_surface(frame.convert("RGBA"))
                self.frames.append(pygameImage)

        else:
            self.frames.append(self.convert_to_surface(pilImage))

    def reset(self):
        self.frame = 0
        self.timeSinceLastFrame = 0
        self.finished = True
    def play(self, screen, dt):
        if not self.finished:
            screen.blit(pygame.transform.scale(self.frames[self.frame], (screen.get_width(),screen.get_height())), (0, 0))
            self.timeSinceLastFrame += dt
            self.frame += int(self.timeSinceLastFrame // (1/self.frameRate))
            self.timeSinceLastFrame %= (1/self.frameRate)
            if self.frame >= len(self.frames):
                self.finished = True

