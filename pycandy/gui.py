import pygame
from pygame.locals import *
from pycandy import *

class Button:
    def __init__(self, text, pos):
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render(text, True, BLACK)
        self.rect = self.text.get_rect()
        self.rect.topleft = pos
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
        pygame.draw.rect(screen, GRAY, self.rect, 3)
        screen.blit(self.text, self.rect)

    def clicked(self, pos):
        return self.rect.collidepoint(pos)