#! /usr/bin/env python3
# coding: utf-8

"""This file contains the class with the properties of the main character
"""


import logging as log

# log.basicConfig(level=log.DEBUG)
log.basicConfig(level=log.CRITICAL)


class MainCharacter:
    """Class that define the main character properties :
        - name
        - position
        - inventory"""

    NAME = "MacGyver"

    def __init__(self, pos_x, pos_y):
        self.position_x = pos_x
        self.position_y = pos_y
        self.inventory = []

    def move(self, dest_x, dest_y):
        """Method used to move the main character
        """
        self.position_x = dest_x
        self.position_y = dest_y

    def add_item(self, item):
        """Method used to add an item to the inventory of the main character
        """
        self.inventory.append(item)


def main():
    pass

if __name__ == "__main__":
    main()
