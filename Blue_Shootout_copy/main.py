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

    current_state = "start_screen"

    running = True
    while running:
        # Collect all events once at the start of the loop
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen for the current frame

        # Pass events to the current state's run method
        if current_state == "start_screen":
            start_pressed = start_screen.run(screen, events)
            if start_pressed:
                current_state = "character_select"
        elif current_state == "character_select":
            next_state = character_select.run(screen, events)
            if next_state == 'game_screen':
                current_state = "game_screen"
        elif current_state == "game_screen":
            game_screen.run(screen, events)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
