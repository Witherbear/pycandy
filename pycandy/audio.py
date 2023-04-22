import pygame

# define a function to play the sound
def play_sound(sound_path):
    sound = pygame.mixer.Sound(sound_path)
    sound.play()

# define a function to stop the sound
def stop_sound(sound_path):
    sound = pygame.mixer.Sound(sound_path)
    sound.stop()