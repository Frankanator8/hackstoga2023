import pygame

def load_image(name, size=None):
    image = pygame.image.load(f"assets/images/{name}.png").convert_alpha()
    if size != None:
        image = pygame.transform.scale(image, size)
    return image