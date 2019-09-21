from collections import namedtuple
from argparse import Namespace
from types import SimpleNamespace
import logging

# Card = namedtuple('Card', ('rank', 'suit'))


SUITS = '\u2660,\u2661\u2662\u2663'
Spades, Hearts, Diamond, Clubs = SUITS  # Пики, Черви, Бубны, Кресты


class Card:
    __slots__ = ['rank', 'suit']

    def __init__(self, rank, suit):
        super().__init__()
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return '{rank:2d}{suit}'.format(
            rank=self.rank,
            suit=self.suit
        )


class AceCard(Card):
    """Туз"""
    def __repr__(self):
        return 'A {suit}'.format(
            rank=self.rank,
            suit=self.suit
        )


class FaceCard(Card):
    """Валет, Дама, Король, Джокер"""
    def __repr__(self):
        names = {11: 'J', 12: 'Q', 13: 'K'}
        return '{name}{suit}'.format(
            rank=self.rank,
            suit=self.suit,
            name=names[self.rank]
        )


class CribbagePoints:
    """Типа весовые очки"""
    def points(self):
        return self.rank


class CribbageFacePoints(CribbagePoints):

    def points(self):
        return 10


class CribbageAce(AceCard, CribbagePoints):
    pass


class CribbageCard(Card, CribbagePoints):
    pass


class CribaggeFaceCard(FaceCard, CribbageFacePoints):
    pass


def make_card(rank, suit):
    if rank == 1:
        return CribbageAce(rank, suit)
    if 2 <= rank < 11:
        return CribbageCard(rank, suit)
    if 11 <= rank:
        return CribaggeFaceCard(rank, suit)


# class Player:
#     pass
#
# p = Player()
# p.stake = 100
#
# Player = SimpleNamespace
#
#
# class Hand:
#
#     __slots__ = ['hand', 'bet']
#
#     def __init__(self, bet, hand=None):
#         self.hand = hand or []
#         self.bet = bet
#
#     def deal(self, card):
#         self.hand.append(card)
#
#     def __repr__(self):
#         return '{class_}({0}, {1})'.format(
#             self.bet, self.hand,
#             class_ = self.__class__.__name__
#         )
