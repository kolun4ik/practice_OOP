from collections import namedtuple
from argparse import Namespace
from types import SimpleNamespace

Card = namedtuple('Card', ('rank', 'suit'))

class Player:
    pass

p = Player()
p.stake = 100

Player = SimpleNamespace


class Hand:

    __slots__ = ['hand', 'bet']

    def __init__(self, bet, hand=None):
        self.hand = hand or []
        self.bet = bet

    def deal(self, card):
        self.hand.append(card)

    def __repr__(self):
        return '{class_}({0}, {1})'.format(
            self.bet, self.hand,
            class_ = self.__class__.__name__
        )
