from modules.fraction import Fraction


def main():
    A = Fraction(2, 3)
    B = Fraction(4, 7)

    print('Дано: ', repr(A), ' и ', repr(B))
    print('Сумма дробей: ', A + B)
    print('Разница: ', A - B)
    print('Умножение: ', A * B)
    print('Деление : ', A / B)
    print('Сумма дроби и целого (5): ', A + 5)
    print('Сумма целого (5) и дроби: ', 5 + A)


if __name__ == '__main__':
    main()
