from os import path
import random
import logging as log
import GameObject as go

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

    def __init__(self, filename):
        self.board_map = [[0 for y in range(self.WIDTH_BOARD)] for x in range(self.HEIGHT_BOARD)]
        self.create_board_map_from_file(filename)
        # counter path

    def create_board_map_from_file(self, filename):
        directory = path.dirname(path.dirname(__file__))  # we get the right path
        path_to_file = path.join(directory, "maps", filename)  # we go inside folder "maps" and get the file

        # read the file to create objects that compose level
        try:
            row = 0
            with open(path_to_file, "r") as f:
                for line in f:
                    for col in range(self.WIDTH_BOARD):
                        self.board_map[row][col] = self.create_object(self.OBJECTS_TYPES[line[col]])
                    row += 1
        except FileNotFoundError as e:
            log.critical('Error: {}'.format(e))

        # Add 3 loots type objects at randoms positions
        for it in range(3):

            randseed = 0
            for row in self.board_map:
                randseed += sum(isinstance(cell, go.Path) for cell in row)

            path_counter = random.randint(0, randseed)  # then select a random counter among these positions

            # then convert the relative position (the nth path) into a general position (the nth positions on the map)
            loot_pos = 0
            for row in self.board_map:
                for item in row:
                    if path_counter > 0:
                        if type(item) == go.Path:
                            path_counter -= 1
                        loot_pos += 1

            # create a loot object at the position randomly generated
            self.board_map[loot_pos // 15][(loot_pos % 15) - 1] = self.create_object(self.OBJECTS_TYPES["l"])

    @staticmethod  # pas statique
    def create_object(type_object):
        if type_object == "Wall":
            return go.Wall()
        elif type_object == "Path":
            # increment counter path
            return go.Path()
        elif type_object == "StartPoint":
            return go.StartPoint()
        elif type_object == "EndPoint":
            return go.EndPoint()
        elif type_object == "Guard":
            return go.Guard()
        elif type_object == "Loot":
            # decrement path
            return go.Loot()
        else:
            log.critical('Error : object type non recognized')

    def get_object_by_coordinates(self, pos_x, pos_y):
        return self.board_map[pos_x][pos_y]

    def replace_picked_up_object(self, pos_x, pos_y):
        self.board_map[pos_x][pos_y] = self.create_object("Path")


# Test
def main():
    my_test_board = Board()
    my_test_board.create_board_map_from_file("level1.map")
    print(my_test_board.board_map)
    for row in my_test_board.board_map:
        string = ""
        for col in row:
            if type(col) == go.Wall:
                string += "X"
            elif type(col) == go.Loot:
                string += "O"
            elif type(col) == go.Guard:
                string += "G"
            else:
                string += " "
        print(string)
    # print("number of loots : {}.".format(sum(row.count('l') for row in my_test_board.board_map)))

if __name__ == "__main__":
    main()
