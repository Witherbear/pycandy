import pygame

# Define a function to draw text on the screen
def draw(screen, text, font, color, x, y):
    # Render the text as a Surface using the given font and color
    text_surface = font.render(text, True, color)
    # Blit the text Surface onto the screen at the given coordinates
    screen.blit(text_surface, (x, y))