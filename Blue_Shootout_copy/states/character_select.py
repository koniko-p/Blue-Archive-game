import pygame
import os  # For path operations

class CharacterSelect:
    # Initialization and other methods as before...
    def __init__(self, game_settings):
        # Initialization code as before...
        self.game_settings = game_settings
        self.bg_color = (255, 255, 255)  # White background

        # Sample list of characters for demonstration
        self.characters = ["Character 1", "Character 2", "Character 3"]
        
        # Initialize empty list for character images
        self.character_images = []
        # Image file paths
        image_paths = ['yaoxiang.jpg', 'toki.jpg', 'nilu.jpg']
        # Desired height for the images to fit in the selection list
        desired_height = 100  # You can adjust this value as needed

        
        # Load and resize images for each character, maintaining aspect ratio
        for image_path in image_paths:
            full_path = os.path.join('assets/images', image_path)
            image = pygame.image.load(full_path)
            # Calculate the new size maintaining the aspect ratio
            aspect_ratio = image.get_width() / image.get_height()
            new_size = (int(desired_height * aspect_ratio), desired_height)
            resized_image = pygame.transform.scale(image, new_size)
            self.character_images.append(resized_image)

        self.font = pygame.font.Font(None, 40)  # Font for character names

        self.player1_selection = 0
        self.player2_selection = 0

        list_width = game_settings.screen_width * 0.3
        self.list1_pos_x = game_settings.screen_width * 0.05
        self.list2_pos_x = game_settings.screen_width - list_width - game_settings.screen_width * 0.05

        self.selection_height = desired_height + 50  # Adjust based on image height + padding for text
        self.list_height = len(self.characters) * self.selection_height
        
        # Add an attribute to track the currently selected character for each player
        self.currently_selected_player1 = None
        self.currently_selected_player2 = None

        # Light blue color for emphasis
        self.emphasis_color = (173, 216, 230)  # Light blue
        self.continue_clicked = False
        self.continue_button_rect = pygame.Rect(0, 0, 150, 50) 

    def handle_clicks(self, mouse_click_position):
        if self.continue_button_rect.collidepoint(mouse_click_position):
            self.continue_clicked = True
            print("Continue clicked, transitioning to the game...")
        else:
            # For debugging: Print the position to verify click detection
            print("Click position:", mouse_click_position) # Assuming a single-player selection for simplicity

        
    def draw_list(self, screen, list_pos_x, current_selection, player_number):
        list_width = self.game_settings.screen_width * 0.3
        list_rect = pygame.Rect(list_pos_x, (self.game_settings.screen_height - self.list_height) / 2, list_width, self.list_height)
        pygame.draw.rect(screen, (200, 200, 200), list_rect)

        for index, character in enumerate(self.characters):
            image = self.character_images[index]
            # Calculate the position for the image
            image_rect = image.get_rect(center=(list_pos_x + list_width / 2, list_rect.top + self.selection_height * index + self.selection_height / 2))

            # Draw the character image
            screen.blit(image, image_rect)

            # Render the character's name and calculate its position
            text_surface = self.font.render(character, True, (0, 0, 0))
            text_rect = text_surface.get_rect(midtop=(image_rect.centerx, image_rect.bottom + 10))
            screen.blit(text_surface, text_rect)

            # Check if this character is the current selection and highlight it
            if index == current_selection:
                # Inflate the emphasis rect to cover both the image and the caption
                emphasis_rect = pygame.Rect(image_rect.left - 10, image_rect.top - 10, 
                                            image_rect.width + 20, image_rect.height + text_rect.height + 20)
                pygame.draw.rect(screen, self.emphasis_color, emphasis_rect, 2)  # Draw emphasis border
            

            if index == current_selection:
                pygame.draw.rect(screen, self.emphasis_color, image_rect.inflate(20, 20), 2) 

        # If player_number is being used to differentiate between player1 and player2, ensure it's integrated correctly

    def draw_continue_button(self, screen):
        # Update continue_button_rect's position before drawing
        self.continue_button_rect.bottomright = (self.game_settings.screen_width - 20, self.game_settings.screen_height - 20)
        pygame.draw.rect(screen, self.emphasis_color, self.continue_button_rect)
        text_surface = self.font.render('Continue', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.continue_button_rect.center)
        screen.blit(text_surface, text_rect)
    
    def update_selection(self, mouse_click_position, player_number):
        list_pos_x = self.list1_pos_x if player_number == 1 else self.list2_pos_x
        for index, character in enumerate(self.characters):
            image_rect = pygame.Rect(list_pos_x, self.game_settings.screen_height // 2 - self.list_height // 2 + index * self.selection_height, self.game_settings.screen_width * 0.3, self.selection_height)
            if image_rect.collidepoint(mouse_click_position):
                if player_number == 1:
                    self.player1_selection = index
                else:
                    self.player2_selection = index
                return

    def run(self, screen, events):
        self.continue_clicked = False
        screen.fill(self.bg_color)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_clicks(event.pos)

        self.draw_list(screen, self.list1_pos_x, self.player1_selection, 1)
        self.draw_list(screen, self.list2_pos_x, self.player2_selection, 2)
        self.draw_continue_button(screen)

        pygame.display.flip()
        return 'game_screen' if self.continue_clicked else None


