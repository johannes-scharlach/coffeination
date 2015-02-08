from __future__ import print_function
import cmd


class TextCoffeCmd(cmd.Cmd):
    """Command line interface for coffeination"""
    prompt = '\n> '
    player = None

    def default(self, arg):
        print('You cannot do this right now. To see a list of available '
              'commands type "help" or read the readme.')

    def do_quit(self, arg):
        """Quit the game."""
        return True  # exit command for the loop

    def do_fight(self, arg):
        """Fighting is exhausting. Get some coffee first."""
        print('Fighting is exhausting. Get some coffee first.')

    def moveTo(self, dest):
        self.player.currentRoom = dest

    def do_north(self, arg):
        """Move to the northern room."""
        self.moveTo(self.player.currentRoom.north)

    def do_east(self, arg):
        """Move to the eastern room."""
        self.moveTo(self.player.currentRoom.east)

    def do_south(self, arg):
        """Move to the southern room."""
        self.moveTo(self.player.currentRoom.south)

    def do_west(self, arg):
        """Move to the western room."""
        self.moveTo(self.player.currentRoom.west)

    do_n = do_north
    do_e = do_east
    do_s = do_south
    do_w = do_west
