import pygame

title = "PyCandy"
width = 800
height = 600

def run():
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the game window
    screen_width = width
    screen_height = height
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set the title of the game window
    pygame.display.set_caption(title)

    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update the screen
        pygame.display.flip()

if __name__ == "__main__":
    run()
