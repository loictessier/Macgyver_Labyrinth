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

    def __init__(self):
        self.game = ga.Game()
        self.ecran = pygame.display.set_mode((300, 300))
        self.image_wall = pygame.image.load(".\img\wall.png").convert_alpha()
        self.image_wall = pygame.transform.scale(self.image_wall, (20, 20))
        self.image_path = pygame.image.load(".\img\path.png").convert_alpha()
        self.image_path = pygame.transform.scale(self.image_path, (20, 20))
        self.image_main_char = pygame.image.load(".\img\macgyver.png").convert_alpha()
        self.image_main_char = pygame.transform.scale(self.image_main_char, (20, 20))
        self.image_guard = pygame.image.load(".\img\guard.png").convert_alpha()
        self.image_guard = pygame.transform.scale(self.image_guard, (20, 20))
        self.image_loot = pygame.image.load(".\img\loot.png").convert_alpha()
        self.image_loot = pygame.transform.scale(self.image_loot, (20, 20))

    def game_loop(self):
        pygame.init()

        game_continue = True

        self.display_screen(self.TYPE_SCREEN["OK"])

        while game_continue:
            # event listen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    game_response = "OK"

                    # user interaction
                    if event.key == pygame.K_UP:
                        game_response = self.game.move_main_character("up")
                    elif event.key == pygame.K_DOWN:
                        game_response = self.game.move_main_character("down")
                    elif event.key == pygame.K_RIGHT:
                        game_response = self.game.move_main_character("right")
                    elif event.key == pygame.K_LEFT:
                        game_response = self.game.move_main_character("left")
                    elif event.key == pygame.K_ESCAPE:
                        game_response = "QUIT"
                        game_continue = False

                    # display manager
                    if game_response in ["LOSE", "WIN"]:
                        self.display_screen(self.TYPE_SCREEN["OK"])
                        self.display_screen(self.TYPE_SCREEN[game_response])
                        game_continue = False
                    elif game_response == "QUIT":
                        self.display_screen(self.TYPE_SCREEN["QUIT"])
                    else:
                        self.display_screen(self.TYPE_SCREEN["OK"])

            pygame.display.flip()

    def display_screen(self, type_screen):
        if type_screen == "Game continue":
            i, j = 0, 0
            for row in self.game.board.board_map:
                for col in row:
                    if col.name == "Wall":
                        self.ecran.blit(self.image_wall, (j*20, i*20))
                    elif col.name == "Guard":
                        self.ecran.blit(self.image_path, (j*20, i*20))
                        self.ecran.blit(self.image_guard, (j*20, i*20))
                    elif col.name in self.game.loot_names_list:
                        self.ecran.blit(self.image_path, (j*20, i*20))
                        self.ecran.blit(self.image_loot, (j*20, i*20))
                    else:
                        self.ecran.blit(self.image_path, (j*20, i*20))
                    j += 1
                i += 1
                j = 0
            self.ecran.blit(self.image_main_char, (self.game.main_char_pos_y * 20, self.game.main_char_pos_x * 20))

        else:
            print(type_screen)

    def display_screen_console(self, type_screen):
        if type_screen == "Game continue":
            # get the level composition
            screen_list = []
            for row in self.game.board.board_map:
                screen_list.append("".join(col.representation for col in row))

            # update with main character position
            screen_list[self.game.main_char_pos_x] = (
                screen_list[self.game.main_char_pos_x][0:self.game.main_char_pos_y]
                + "M"
                + screen_list[self.game.main_char_pos_x][self.game.main_char_pos_y+1:])

            # print result
            for row in screen_list:
                print(row)

        elif type_screen == "Game over":
            #display Game Over screen
            screen = """
                #######################
                #######################
                ###                 ###
                ###    YOU DIED     ###
                ###                 ###
                #######################
                #######################
            """
            print(screen)

        elif type_screen == "Level completed":
            #display win screen
            screen = """
                #############################
                #############################
                ###                       ###
                ###    LEVEL COMPLETED    ###
                ###                       ###
                #############################
                #############################
            """
            print(screen)

        elif type_screen == "Quit game":
            #display win screen
            screen = """
                ###############################
                ###############################
                ###                         ###
                ###    YOU QUIT THE GAME    ###
                ###                         ###
                ###############################
                ###############################
            """
            print(screen)

        else:
            log.critical('Error : screen type non recognized')


def main():
    lab = Labyrinth()
    lab.game_loop()
    #TESTS
    # lab.display_screen(lab.TYPE_SCREEN["OK"])
    # print(lab.game.board.board_map)

if __name__ == "__main__":
    main()
