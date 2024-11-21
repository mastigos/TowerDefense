
import pygame

class Music:
    def __init__(self, music_file):
        self.music_file = music_file
        self.is_paused = False
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_file)

    def play_music(self):
        pygame.mixer.music.play(-1)  # Loop the music indefinitely

    def toggle_pause(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.is_paused = not self.is_paused
