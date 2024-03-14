import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("3D Ball Rendering")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define ball properties
BALL_RADIUS = 50
BALL_X = WINDOW_WIDTH // 2
BALL_Y = WINDOW_HEIGHT // 2

# Main function to render the ball
def render_ball():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        WINDOW.fill(WHITE)

        # Draw the ball
        pygame.draw.circle(WINDOW, RED, (BALL_X, BALL_Y), BALL_RADIUS)

        # Update the display
        pygame.display.update()

# Main function
def main():
    render_ball()

# Run the program
if __name__ == "__main__":
    main()
