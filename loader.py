import pygame

def load_image(name, size=None):
    image = pygame.image.load(f"assets/images/{name}.png").convert_alpha()
    if size != None:
        image = pygame.transform.scale(image, size)
    return image
def load_audio(name):
    sound = pygame.mixer.Sound(f'assets/audio/{name}.wav')
    return sound
def play_audio(sound):
    pygame.mixer.Sound.play(sound)
def pause_audio():
    pygame.mixer.pause()
def resume_audio():
    pygame.mixer.unpause()