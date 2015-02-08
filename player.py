import cmd


class CreateCharacterCmd(cmd.Cmd):
    """Command line interface to create a character"""
    prompt = '\n> '
    player = None

    def preloop(self):
        self.player = Player()

    def default(self, arg):
        print('You cannot do this right now. Type "ready" when your '
              'character is finished and you\'re ready to explore '
              'or type "help" for a list of available commands')

    def do_name(self, arg):
        """Set a name for your Character"""
        self.player.name = arg

    def do_profession(self, arg):
        professions = ['developer', 'sales rep', 'designer']
        if arg in professions:
            self.player.profession = arg
        else:
            print('Sorry, this is not a valid profession. '
                  'Try one of the following:\n')
            for profession in professions:
                print('- ' + profession)

    def do_ready(self, arg):
        """Quit creating your character and start exploring"""
        try:
            name = self.player.name
        except:
            name = None
        if not name:
            print('Please set a name before you continue')
            return False
        return True


class Player(object):
    """docstring for Player"""

    def currentRoom():
        doc = "The currentRoom property."

        def fget(self):
            return self._currentRoom

        def fset(self, room):
            try:
                self._lastRoom = self._currentRoom
            except AttributeError:
                pass
            self._currentRoom = room
            self._currentRoom.visit()

        def fdel(self):
            del self._currentRoom
        return locals()
    currentRoom = property(**currentRoom())
