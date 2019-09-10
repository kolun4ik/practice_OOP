import sys
from modules.games import *

def main():
    hero = Charaster(1, 100)

    print('Getting Started: Manage Your Character with Teams')
    print('Command for manage:')
    print('- move (up, down, left, right) for relocation')
    print('- assault for enemy attack')
    print('- experience')
    print('- health up')
    print('- level up')
    print('- quit for exit games')

    while True:
        command = input('Input commands --> ')
        if command in ('up', 'down', 'left', 'right'):
            hero.move(command)
        elif command == 'assault':
            hero.assault()
        elif command == 'experience':
            hero.experience()
        elif command == 'health up':
            hero.healthUp()
        elif command == 'level up':
            hero.levelUp()
        elif command == 'quit':
            sys.exit(0)
        else:
            print('Command wrong')


if __name__ == '__main__':
    main()