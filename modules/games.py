# Создайтьконсольную игру, в которой игрок сможет управлять персонажем с помощью команд.
# Возможности, которые должны быть в игре:
#
# - перемещение;
# - атака;
# - получение опыта за победу над врагами;
# - повышение уровня и здоровья персонажа.

class Charaster:
    """Персонаж игры"""
    def __init__(self, level, health):
        self.level = level
        self.health = health

    def move(self, direction):
        """Перемещение персонажа: up, down, left, right"""
        if direction == 'up':
            print('Walk Up')
        elif direction == 'down':
            print('Walk Down')
        elif direction == 'left':
            print('Walk Left')
        elif direction == 'right':
            print('Walk Right')
        else:
            print('Direction wrong')

    def assault(self):
        """Нападение"""
        print('Attack on the enemy')

    def experience(self):
        """Получение опыта"""
        print('Your expirience up')

    def levelUp(self):
        self.level += 1
        print('Level: ', self.level)

    def healthUp(self):
        self.health += 1
        print('health: ', self.health)

