
class GameObject:
    """
    """

    def __init__(self):
        self.name = none
        self.visible = none
        self.can_be_crossed = none
        self.can_be_picked_up = none
        self.is_end_point = none
        #add text_display properties

    def __repr__(self):
        return self.name


class Wall(GameObject):

    def __init__(self):
        self.name = "Wall"
        self.visible = True
        self.can_be_crossed = False
        self.can_be_picked_up = False
        self.is_end_point = False


class Path(GameObject):

    def __init__(self):
        self.name = "Path"
        self.visible = True
        self.can_be_crossed = True
        self.can_be_picked_up = False
        self.is_end_point = False


class StartPoint(GameObject):

    def __init__(self):
        self.name = "StartPoint"
        self.visible = False
        self.can_be_crossed = True
        self.can_be_picked_up = False
        self.is_end_point = False


class EndPoint(GameObject):

    def __init__(self):
        self.name = "EndPoint"
        self.visible = False
        self.can_be_crossed = True
        self.can_be_picked_up = False
        self.is_end_point = True


class Guard(GameObject):

    def __init__(self):
        self.name = "Guard"
        self.visible = True
        self.can_be_crossed = False
        self.can_be_picked_up = False
        self.is_end_point = False


class Loot(GameObject):

    def __init__(self):
        self.name = "Loot"
        self.visible = True
        self.can_be_crossed = True
        self.can_be_picked_up = True
        self.is_end_point = False


# Test
def main():
    my_wall = Wall()
    print("Wall can be crossed ? {}".format(my_wall.can_be_crossed))

if __name__ == "__main__":
    main()
