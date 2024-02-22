import pygame
import sys
from settings import Settings
from states.start_screen import StartScreen
from states.character_select import CharacterSelect
from states.game_screen import GameScreen
# Assuming GameScreen is correctly defined but not used for this transition
# from states.game_screen import GameScreen

def main():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Game")

    # Initialize screens
    start_screen = StartScreen(game_settings)
    character_select = CharacterSelect(game_settings)
    game_screen = GameScreen(game_settings)
    # game_screen = GameScreen(game_settings)  # Placeholder for future use

    # State management
    current_state = "start_screen"  # Initial state

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))  # Clear the screen for the current frame

        # Transition logic based on the current state
        if current_state == "start_screen":
            if start_screen.run(screen):
                current_state = "character_select"  # Transition to character select screen
        elif current_state == "character_select":
            next_state = character_select.run(screen)
            if next_state == 'game_screen':  # Check for transition signal
                current_state = "game_screen"
        elif current_state == "game_screen":
            game_screen.run(screen)  # Run the game screen
            # Additional state transitions can be managed here

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
