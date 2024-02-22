import pygame

class StartScreen:
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.bg_color = (255, 255, 255)  # White background
        self.font = pygame.font.Font(None, 74)  # Default font, size 74
        self.text_color = (0, 0, 0)  # Black text
        # Adjusted button colors
        self.button_color = (173, 216, 230)  # Light blue
        self.button_hover_color = (135, 206, 250)  # Slightly different shade for hover
        self.button_frame_color = (0, 0, 139)  # Dark blue for frame
        self.button_rect = pygame.Rect(0, 0, 200, 50)  # Button size
        self.button_text = 'Start'
        self.button_rect.center = (game_settings.screen_width // 2, game_settings.screen_height // 2 + 50)
        self.button_clicked = False  # Track if the button has been clicked

    def run(self, screen,events):
        screen.fill(self.bg_color)
        
        # Render the text
        text = self.font.render("Blue Shootout", True, self.text_color)
        text_rect = text.get_rect(center=(self.game_settings.screen_width // 2, self.game_settings.screen_height // 2 - 50))
        screen.blit(text, text_rect)
        
        # Draw the button frame (slightly larger rectangle behind the button)
        frame_rect = self.button_rect.inflate(4, 4)  # Inflate the rect size for the frame
        pygame.draw.rect(screen, self.button_frame_color, frame_rect)
        
        # Draw the start button
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.button_hover_color, self.button_rect)  # Button changes color on hover
            if pygame.mouse.get_pressed()[0] and not self.button_clicked:
                print("Button Clicked!")  # Placeholder for button click action
                self.button_clicked = True
        else:
            pygame.draw.rect(screen, self.button_color, self.button_rect)

        # Reset button_clicked if the mouse is not pressed
        if not pygame.mouse.get_pressed()[0]:
            self.button_clicked = False

        # Button text
        button_text_surface = self.font.render(self.button_text, True, self.text_color)
        button_text_rect = button_text_surface.get_rect(center=self.button_rect.center)
        screen.blit(button_text_surface, button_text_rect)
    # Existing implementation...
    
        if self.button_clicked:
            self.button_clicked = False  # Reset to prevent repeated clicks
            return True  # Indicate that the start button was clicked

        return False  # No state change requested
