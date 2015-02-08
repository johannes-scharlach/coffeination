import random


global world
global offsets


world = [None]
offsets = [None]


def randomRoom():
    return random.choice(roomTypes)


def extendList(l, i, e):
    l[i] = e
    l.insert(i + (i >= 0), None)
    return l


def mapping(xCoord, yCoord):
    global world
    global offsets
    if world[xCoord] is None:
        world = extendList(world, xCoord, [None])
        offsets = extendList(offsets, xCoord, yCoord)
    if world[xCoord][yCoord - offsets[xCoord]] is None:
        newRoom = randomRoom()
        world[xCoord] = extendList(world[xCoord],
                                   yCoord - offsets[xCoord],
                                   newRoom(xCoord, yCoord))

    return world[xCoord][yCoord - offsets[xCoord]]


def getNeighbouringRooms(xCoord, yCoord):
    northernRoom = mapping(xCoord + 1, yCoord)
    easternRoom = mapping(xCoord, yCoord + 1)
    southernRoom = mapping(xCoord - 1, yCoord)
    westernRoom = mapping(xCoord, yCoord - 1)
    return northernRoom, easternRoom, \
        southernRoom, westernRoom


class AbstractRoom(object):
    """The map is made up of rooms that the player can access.

    Parameters
    ----------
    xCoord : int
        The x coordinate of the room
    xCoord : int
        The y coordinate of the room

    """
    _descriptions = None
    _numCoffeePads = 0

    def __init__(self, xCoord, yCoord):
        self._x, self._y = xCoord, yCoord
        self.shortDesc, self.longDesc = self._getDesc()

    def north():
        doc = "Room to the North of the current one"

        def fget(self):
            return self._north
        return locals()
    north = property(**north())

    def south():
        doc = "Room to the South of the current one"

        def fget(self):
            return self._south
        return locals()
    south = property(**south())

    def east():
        doc = "Room to the East of the current one"

        def fget(self):
            return self._east
        return locals()
    east = property(**east())

    def west():
        doc = "Room to the West of the current one"

        def fget(self):
            return self._west
        return locals()
    west = property(**west())

    def x():
        doc = "The x coordinate."

        def fget(self):
            return self._x
        return locals()
    x = property(**x())

    def y():
        doc = "The y coordinate."

        def fget(self):
            return self._y
        return locals()
    y = property(**y())

    def canConsumeCoffee():
        doc = "Can the user cosume coffee here?"

        def fget(self):
            return self._numCoffeePads > 0
        return locals()
    canConsumeCoffee = property(**canConsumeCoffee())

    shortDesc = None
    longDesc = None
    takeable = None
    equipment = None

    def printRoom(self):
        description = ('\n\n' + self.name + '\n========\n\n\n' +
                       self.shortDesc + '\n' + self.longDesc + '\n\n' +
                       'There are ' + str(self._numCoffeePads) +
                       ' Coffee Pads here\n\n' +
                       'Northern Room: ' + self.north.name + '\n' +
                       'Eastern Room: ' + self.east.name + '\n' +
                       'Southern Room: ' + self.south.name + '\n' +
                       'Western Room: ' + self.west.name)
        print(description)

    def visit(self):
        """Visit this room with a player"""
        self._north, self._east, self._south, self._west = \
            getNeighbouringRooms(self.x, self.y)
        self.printRoom()

    def consumeCoffee(self):
        """Consume some of the delicious coffee here"""
        if self.canConsumeCoffee:
            self._numCoffeePads -= 1
            return True
        else:
            return False

    def _getDesc(self):
        if self._descriptions is None:
            raise NotImplemented('No Descriptions for this room available')
        return random.choice(self._descriptions)


class Kitchen(AbstractRoom):
    """The room where most coffee can be found"""
    name = "kitchen"
    _descriptions = [
        ("This is a plain kitchen", "Nothing fancy to see here. You're "
         "surprised that somebody must have cleaned this place lately"),
        ("This is a dirty kitchen", "You see dirty dishes and many used "
         "glasses and mugs. Somebody should clean them.")
    ]

    def __init__(self, *arg):
        super(Kitchen, self).__init__(*arg)
        self._numCoffeePads = random.randrange(1, 4)


class Hallway(AbstractRoom):
    """A common room through which you move on"""
    name = "hallway"
    _descriptions = [
        ("A very slim hallway", "It seems so crowded here. Hard to "
         "explore, you might as well move on"),
        ("A huge hallway", "Are you sure you can see to the other "
         "side of the room? Why is this room so big?")
    ]

    def __init__(self, *arg):
        super(Hallway, self).__init__(*arg)


roomTypes = [Kitchen, Hallway]
