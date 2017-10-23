#! /usr/bin/env python3
# coding: utf-8
import logging as log
import Game as ga

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

    def game_loop(self):
        game_continue = True
        while game_continue:
            # display level
            self.display_screen(self.TYPE_SCREEN["OK"])
            # ask input (listen)
            user_answer = input('Which direction will you go ? (up, down, right, left). Type "quit" to end the game. ')

            if user_answer in ["up", "down", "right", "left"]:
                game_response = self.game.move_main_character(user_answer)
                if game_response in ["LOSE", "WIN"]:
                    self.display_screen(self.TYPE_SCREEN["OK"])
                    self.display_screen(self.TYPE_SCREEN[game_response])
                    game_continue = False

            elif user_answer == "quit":
                self.display_screen(self.TYPE_SCREEN["QUIT"])
                game_continue = False

            else:
                log.debug('Error : user input invalid')

    def display_screen(self, type_screen):
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
