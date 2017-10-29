#! /usr/bin/env python3
# coding: utf-8

"""This is the file that lauch the program and handle all interaction
    with the player. This version uses Pygame for controls and graphical
    display.
"""


import pygame
import logging as log
import classes.Game as ga


# log.basicConfig(level=log.DEBUG)
log.basicConfig(level=log.CRITICAL)


class Labyrinth:
    """Class which represents the starting point of the program:
        - instantiate class Game()
        - handle player inputs and gui"""

    TYPE_SCREEN = {
        "OK": "Game continue",
        "LOSE": "Game over",
        "WIN": "Level completed",
        "QUIT": "Quit game"
    }

    HEIGHT_WINDOW = 600
    WIDTH_WINDOW = 600

    def __init__(self):
        self.game = ga.Game()
        self.screen = pygame.display.set_mode((self.WIDTH_WINDOW, self.HEIGHT_WINDOW))
        pygame.display.set_caption("MacGyver's Labyrinth")
        self.image_wall = pygame.image.load(".\img\wall.png").convert_alpha()
        self.image_wall = pygame.transform.scale(self.image_wall, (self.WIDTH_WINDOW//15, self.HEIGHT_WINDOW//15))
        self.image_path = pygame.image.load(".\img\path.png").convert_alpha()
        self.image_path = pygame.transform.scale(self.image_path, (self.WIDTH_WINDOW//15, self.HEIGHT_WINDOW//15))
        self.image_main_char = pygame.image.load(".\img\macgyver.png").convert_alpha()
        self.image_main_char = pygame.transform.scale(self.image_main_char, (self.WIDTH_WINDOW//15, self.HEIGHT_WINDOW//15))
        self.image_guard = pygame.image.load(".\img\guard.png").convert_alpha()
        self.image_guard = pygame.transform.scale(self.image_guard, (self.WIDTH_WINDOW//15, self.HEIGHT_WINDOW//15))
        self.image_loot = pygame.image.load(".\img\loot.png").convert_alpha()
        self.image_loot = pygame.transform.scale(self.image_loot, (self.WIDTH_WINDOW//15, self.HEIGHT_WINDOW//15))

    def game_loop(self):
        """The game loop, keep the game running while end condition is not
            completed. Read all the player controls and call the display 
            corresponding.
        """
        pygame.init()
        pygame.font.init()

        game_continue = True
        game_end_screen = False

        self._display_screen(self.TYPE_SCREEN["OK"])

        while game_continue:
            # event listen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    game_response = "OK"

                    # user interaction
                    if event.key == pygame.K_UP and not game_end_screen:
                        game_response = self.game.move_main_character("up")
                    elif event.key == pygame.K_DOWN and not game_end_screen:
                        game_response = self.game.move_main_character("down")
                    elif event.key == pygame.K_RIGHT and not game_end_screen:
                        game_response = self.game.move_main_character("right")
                    elif event.key == pygame.K_LEFT and not game_end_screen:
                        game_response = self.game.move_main_character("left")
                    elif event.key == pygame.K_ESCAPE:
                        game_response = "QUIT"
                        game_continue = False

                    # display manager
                    if game_response in ["LOSE", "WIN"]:
                        self._display_screen(self.TYPE_SCREEN["OK"])
                        self._display_screen(self.TYPE_SCREEN[game_response])
                        game_end_screen = True
                    elif game_response == "QUIT":
                        self._display_screen(self.TYPE_SCREEN["QUIT"])
                    else:
                        if not game_end_screen:
                            self._display_screen(self.TYPE_SCREEN["OK"])

            pygame.display.flip()

    def _display_screen(self, type_screen):
        """Method used to generate all the screens viewed by the player.
        """
        width_rect = 2 * self.WIDTH_WINDOW // 3
        height_rect = self.HEIGHT_WINDOW // 3
        my_font1 = pygame.font.SysFont('centurygothic', 30)
        my_font2 = pygame.font.SysFont('centurygothic', 20)

        if type_screen == "Game continue":
            i, j = 0, 0
            for row in self.game.board_map:
                for col in row:
                    if col.name == "Wall":
                        self.screen.blit(self.image_wall, (j*self.WIDTH_WINDOW//15, i*self.HEIGHT_WINDOW//15))
                    elif col.name == "Guard":
                        self.screen.blit(self.image_path, (j*self.WIDTH_WINDOW//15, i*self.HEIGHT_WINDOW//15))
                        self.screen.blit(self.image_guard, (j*self.WIDTH_WINDOW//15, i*self.HEIGHT_WINDOW//15))
                    elif col.name in self.game.loot_names_list:
                        self.screen.blit(self.image_path, (j*self.WIDTH_WINDOW//15, i*self.HEIGHT_WINDOW//15))
                        self.screen.blit(self.image_loot, (j*self.WIDTH_WINDOW//15, i*self.HEIGHT_WINDOW//15))
                    else:
                        self.screen.blit(self.image_path, (j*self.WIDTH_WINDOW//15, i*self.HEIGHT_WINDOW//15))
                    j += 1
                i += 1
                j = 0
            self.screen.blit(self.image_main_char, (self.game.main_char_pos_y*self.WIDTH_WINDOW//15, self.game.main_char_pos_x*self.HEIGHT_WINDOW//15))

        elif type_screen == "Game over":
            pygame.draw.rect(self.screen, (255, 255, 255), ((self.WIDTH_WINDOW - width_rect) // 2, (self.HEIGHT_WINDOW - height_rect) // 2, width_rect, height_rect))
            game_over_message = my_font1.render("YOU DIED", False, (0, 0, 0))
            game_over_submessage = my_font2.render("Press 'esc' to quit the game", False, (0, 0, 0))
            self.screen.blit(game_over_message, (230, 270))
            self.screen.blit(game_over_submessage, (165, 320))
            print(type_screen)
        elif type_screen == "Level completed":
            pygame.draw.rect(self.screen, (255, 255, 255), ((self.WIDTH_WINDOW - width_rect) // 2, (self.HEIGHT_WINDOW - height_rect) // 2, width_rect, height_rect))
            game_complete_message = my_font1.render("LEVEL COMPLETED", False, (0, 0, 0))
            game_complete_submessage = my_font2.render("Press 'esc' to quit the game", False, (0, 0, 0))
            self.screen.blit(game_complete_message, (165, 270))
            self.screen.blit(game_complete_submessage, (165, 320))
            print(type_screen)
        elif type_screen == "Quit game":
            print(type_screen)
        else:
            log.critical('Error : screen type non recognized')


def main():
    lab = Labyrinth()
    lab.game_loop()

if __name__ == "__main__":
    main()
