# Абстрактный тип данных - Дробь
# Реализуем действия над дробями: add, sub, eq, gr, le, div, mul


class Fraction:
    """Базовый класс Fraction - дробь"""

    def __init__(self, top, bottom):
        self.num = top // self._gcd(top, bottom)
        self.den = bottom // self._gcd(top, bottom)

    def __str__(self):
        if self.num > self.den:
            integer = self.num // self.den
            remain = self.num % self.den
            if remain:
                return str(integer) + '(' + str(remain) + '/' + str(self.den) + ')'
            else:
                return str(integer)

        elif self.num == self.den:
            return '1'
        else:
            return str(self.num) + '/' + str(self.den)

    def _gcd(self, m, n):
        """Наименьший общий делитель: наименьшее число,
        которое делится на каждый из знаменателей"""
        while m % n != 0:
            tmpn = n
            tmpm = m

            m = tmpn
            n = tmpm % tmpn
        return n