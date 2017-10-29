#! /usr/bin/env python3
# coding: utf-8

"""This file contains the class Board which is used to contains all the
    elements which composes the level of the game and the methods to
    manipulates these elements.
"""


from os import path
import random
import logging as log
from . import GameObject as go

# log.basicConfig(level=log.DEBUG)
log.basicConfig(level=log.CRITICAL)


class Board:
    """Class that defines the game's board, contains:
    - the Height and width of the board
    - the objects which compose the level"""

    HEIGHT_BOARD = 15
    WIDTH_BOARD = 15
    OBJECTS_TYPES = {
        "w": "Wall",
        "p": "Path",
        "s": "StartPoint",
        "e": "EndPoint",
        "g": "Guard",
        "l": "Loot"
    }

    LOOT_NAMES = ["Needle", "Plastic tube", "Ether flask"]

    def __init__(self, filename):
        self.path_counter = 0
        self.board_map = [[0 for y in range(self.WIDTH_BOARD)] for x in range(self.HEIGHT_BOARD)]
        self._create_board_map_from_file(filename)

    def _create_board_map_from_file(self, filename):
        """This methods generates all the objects of the level 
            except the main character. It reads a file to set all 
            the walls, paths, ending and starting point and the 
            position of the guard. Then it places the loot objects
            at random positions among the paths objects.
        """
        directory = path.dirname(path.dirname(__file__))  # we get the right path
        path_to_file = path.join(directory, "maps", filename)  # we go inside folder "maps" and get the file

        # read the file to create objects that compose level
        try:
            row = 0
            with open(path_to_file, "r") as f:
                for line in f:
                    for col in range(self.WIDTH_BOARD):
                        self.board_map[row][col] = self._create_object(self.OBJECTS_TYPES[line[col]])
                    row += 1
        except FileNotFoundError as e:
            log.critical('Error: {}'.format(e))

        # Add 3 loots type objects at randoms positions
        for it in range(3):
            path_rand = random.randint(0, self.path_counter)

            # convert the relative position (the nth path) into a general position (the nth positions on the map)
            loot_pos = 0
            for row in self.board_map:
                for item in row:
                    if path_rand > 0:
                        if item.name == "Path":
                            path_rand -= 1
                        loot_pos += 1

            # create a loot object at the position randomly generated
            self.board_map[loot_pos // 15][(loot_pos % 15) - 1] = self._create_object(self.OBJECTS_TYPES["l"], self.LOOT_NAMES[it])

    def _create_object(self, type_object, loot_name=None):
        """This method is used to create all objects that 
            we need when we generate the level map list and 
            when we manipulate it.
        """
        if type_object == "Wall":
            return go.create_wall()
        elif type_object == "Path":
            self.path_counter += 1
            return go.create_path()
        elif type_object == "Loot":
            self.path_counter -= 1
            return go.create_loot(loot_name)
        elif type_object == "StartPoint":
            return go.create_startpoint()
        elif type_object == "EndPoint":
            return go.create_endpoint()
        elif type_object == "Guard":
            return go.create_guard()
        else:
            log.critical('Error : object type non recognized')

    def get_object_by_coordinates(self, pos_x, pos_y):
        """Returns an objectscorresponding to
            the coordinates passed in parameters.
        """
        return self.board_map[pos_x][pos_y]

    def replace_picked_up_object(self, pos_x, pos_y):
        """When a object is picked up we call this
            with the coordinates of the objects. This
            methods replaces it with a new "Path" object.
        """
        self.board_map[pos_x][pos_y] = self._create_object("Path")

    def get_startpoint_coordinates(self):
        """Get the coordinate with the coordinates
            of the unique "StartPoint" object of the level.
        """
        i, j = 0, 0
        for row in self.board_map:
            for col in row:
                if col.name == "StartPoint":
                    return i, j
                j += 1
            i += 1
            j = 0


# Test
def main():
    my_test_board = Board("level1.map")
    for row in my_test_board.board_map:
        for col in row:
            print(col)

if __name__ == "__main__":
    main()
