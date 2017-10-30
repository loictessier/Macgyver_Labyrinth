#! /usr/bin/env python3
# coding: utf-8

"""This file contains the logic of the game and instanciates
    the elements that compose the level.
"""


from . import MainCharacter as mc
from . import Board as bo
import logging as log

# log.basicConfig(level=log.DEBUG)
log.basicConfig(level=log.CRITICAL)


class Game:
    """Class which contains the game logic and implements all the components:
        - it is implemented by the starting point/interface
        - it contains all the component of the game itself (main character, board)
        - it contains all the game logic methods (move a character, pick up an object, confront the guard)
    """

    def __init__(self):
        self.board = bo.Board("level1.map")
        pos_x, pos_y = self.board.get_startpoint_coordinates()
        self.main_character = mc.MainCharacter(pos_x, pos_y)

    def move_main_character(self, direction):
        """This method handle the game logic related to movement
            and call all methods linked with post movements actions
            if necessary.
        """
        # verify destination valid
        dest_x, dest_y = self._calculate_move(self.main_char_pos_x, self.main_char_pos_y, direction)
        dest_object = self.board.get_object_by_coordinates(dest_x, dest_y)

        if dest_object.can_be_crossed:
            self.main_character.move(dest_x, dest_y)
            if dest_object.can_be_picked_up:
                return self._pick_up_object(dest_object, dest_x, dest_y)
            elif dest_object.is_end_point:
                return self._confront_guard()
        else:
            print("Can't walk there")
            return "OK"

    @property
    def main_char_pos_x(self):
        return self.main_character.position_x

    @property
    def main_char_pos_y(self):
        return self.main_character.position_y

    @property
    def loot_names_list(self):
        return self.board.LOOT_NAMES

    @property
    def board_map(self):
        return self.board.board_map

    def _calculate_move(self, pos_x, pos_y, direction):
        """This method is used to calculate the coordinates
            of the destinations after a basic movement.
        """
        if direction == "up":
            pos_x -= 1
        elif direction == "down":
            pos_x += 1
        elif direction == "right":
            pos_y += 1
        elif direction == "left":
            pos_y -= 1
        else:
            log.debug("Error: can't move character - direction non recognized")

        return pos_x, pos_y

    def _pick_up_object(self, dest_object, pos_x, pos_y):
        """This method handle the actions when the player has to
            pick up an object.
        """
        self.main_character.add_item(dest_object)
        self.board.replace_picked_up_object(pos_x, pos_y)
        return "OK"

    def _confront_guard(self):
        """This method handle the actions when the player has to
            confront the guard.
        """
        if len(self.main_character.inventory) == 3:
            return "WIN"
        else:
            return "LOSE"


def main():
    pass

if __name__ == "__main__":
    main()
