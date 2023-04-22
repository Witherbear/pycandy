import pygame

# define a function to draw a rectangle
def draw_rect(rect):
    pygame.draw.rect(window, (255, 0, 0), rect)

# define a function to draw an ellipse
def draw_circ(circ):
    pygame.draw.ellipse(window, (0, 255, 0), circ)

# define a function to draw a polygon
def draw_poly(poly):
    pygame.draw.polygon(window, (0, 0, 255), poly)