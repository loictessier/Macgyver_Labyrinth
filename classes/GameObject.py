#! /usr/bin/env python3
# coding: utf-8

"""This file contains the class GameObject which represents
    the model of the objects that compose the level. It contains
    also the 'Factory' fonctions that are used to generates the
    differents types of objects.
"""


class GameObject:
    """This class represent the model of a game objects:
        - gameobjects general properties
        - implementaion of __repr__ method to print the name of the objects (mainly for debug and tests)
    """

    def __init__(self, name, visible, can_be_crossed, can_be_picked_up, is_end_point, representation):
        self.name = name
        self.visible = visible
        self.can_be_crossed = can_be_crossed
        self.can_be_picked_up = can_be_picked_up
        self.is_end_point = is_end_point
        self.representation = representation

    def __repr__(self):
        return self.name


def create_wall():
    return GameObject("Wall", True, False, False, False, "#")


def create_path():
    return GameObject("Path", True, True, False, False, " ")


def create_startpoint():
    return GameObject("StartPoint", False, True, False, False, " ")


def create_endpoint():
    return GameObject("EndPoint", False, True, False, True, " ")


def create_guard():
    return GameObject("Guard", True, False, False, False, "G")


def create_loot(name):
    return GameObject(name, True, True, True, False, "O")


# Test
def main():
    my_wall = create_wall()
    print("Wall can be crossed ? {}".format(my_wall.can_be_crossed))

if __name__ == "__main__":
    main()
