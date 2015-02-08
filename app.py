#! python3

from rooms import mapping
from player import CreateCharacterCmd
from cli import TextCoffeCmd

if __name__ == '__main__':
    print('=======================')
    print('Welcome to Coffeintaion')
    print('=======================')
    print('')
    print('Type "help" to see a list of commands.')
    print('')
    print('First create your Character')
    ccc = CreateCharacterCmd()
    ccc.cmdloop()
    player = ccc.player
    print('')
    print('Great! You\'re now ready to explore, ' + player.name)

    player.currentRoom = mapping(0, 0)

    tcc = TextCoffeCmd()
    tcc.player = player
    tcc.cmdloop()
    print('If you have enjoyed playing this game, please rate on the AppStore')
    print('')
    print('Just kidding, your pure love is enough')
