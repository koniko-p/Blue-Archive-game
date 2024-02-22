import pygame

class GameScreen:
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.bg_color = (255, 255, 255)  # Set the background color to white

    def run(self, screen):
        # Fill the screen with the background color
        screen.fill(self.bg_color)
        
        # Update the display to reflect the new screen state
        pygame.display.flip()