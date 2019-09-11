# Абстрактный тип данных - Дробь
# Реализуем действия над дробями: add, sub, eq, gr, le, div, mul


class Fraction:
    """Базовый класс Fraction - дробь"""

    def __init__(self, top, bottom):
        abs_bottom = abs(bottom)
        if isinstance(top, int) and isinstance(abs_bottom, int):
            self.num = top // self._gcd(top, abs_bottom)
            self.den = abs_bottom // self._gcd(top, abs_bottom)
        else:
            raise TypeError('Числитель и знаменатель должны быть целыми чис-ми')

    def __str__(self):
        symbol = ''
        if self.num < 0:
            symbol = '-'
        abs_num = abs(self.num)
        if abs_num > self.den:
            integer = abs_num // self.den
            remain = abs_num % self.den
            if remain:
                return symbol + str(integer) + \
                       '(' + str(remain) + '/' + str(self.den) + ')'
            else:
                return symbol + str(integer)
        elif abs_num == self.den:
            return symbol + '1'
        elif self.num == 0:
            return '0'
        else:
            return symbol + str(abs_num) + '/' + str(self.den)

    def __repr__(self):
        return 'Дробь: {}/{}'.format(self.num, self.den)

    def _gcd(self, m, n):
        """Наименьший общий делитель: наименьшее число,
        которое делится на каждый из знаменателей"""
        while m % n != 0:
            tmpn = n
            tmpm = m

            m = tmpn
            n = tmpm % tmpn
        return n

    def getNum(self):
        return str(self.num)

    def getDen(self):
        return str(self.den)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        """Вычитание дробей"""
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __eq__(self, other):
        """Равество дробей"""
        if self.num == other.num and self.den == other.den:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        """Перемножение дробей"""
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        """Деление дробей"""
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __gt__(self, other):
        gcd = self._gcd(self.den, other.den)
        result = self.num * gcd - other.num * gcd
        if result > 0:
            return True
        else:
            return False

    def __ge__(self, other):
        gcd = self._gcd(self.den, other.den)
        result = self.num * gcd - other.num * gcd
        if result >= 0:
            return True
        else:
            return False

    def __lt__(self, other):
        return not self.__gt__(other)

    def __le__(self, other):
        return not self.__ge__(other)
