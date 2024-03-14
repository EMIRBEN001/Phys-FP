import pygame
import sys
import ball # Import the ball module

# Initialize Pygame
pygame.init()

# Set up window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Main Menu")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
FONT = pygame.font.SysFont(None, 40)

# Function to display main menu
def main_menu():
    while True:
        WINDOW.fill(WHITE)
        draw_text("Main Menu", FONT, BLACK, WINDOW_WIDTH // 2, 100)
        start_button = draw_button("Start", 300, 200)
        instructions_button = draw_button("Instructions", 300, 300)
        quit_button = draw_button("Quit", 300, 400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(pygame.mouse.get_pos()):
                    return "start"
                elif instructions_button.collidepoint(pygame.mouse.get_pos()):
                    return "instructions"
                elif quit_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Function to draw text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    WINDOW.blit(text_surface, text_rect)

# Function to draw a button on the screen
def draw_button(text, x, y):
    button_rect = pygame.Rect(x - 100, y - 25, 200, 50)
    pygame.draw.rect(WINDOW, BLACK, button_rect, 2)
    draw_text(text, FONT, BLACK, x, y)
    return button_rect

# Main function
def main():
    while True:
        option = main_menu()
        if option == "start":
            ball.render_ball(WINDOW)  # Pass the window surface to the render_ball function
        elif option == "instructions":
            # Display instructions
            print("Showing instructions...")
        else:
            pygame.quit()
            sys.exit()

# Run the program
if __name__ == "__main__":
    main()
