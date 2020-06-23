import random

class NewDeck(object):
    """
    Represents a deck of playing cards with collection of CardObjects to represent individual playing cards and and
    assortment of methods to simulate common deck manipulations (e.g. adding/removing cards, shuffling, sorting, etc)
    """
    def __init__(self):
        self.numeric_cards = list(range(2,11))
        self.face_cards = ["jack", "queen", "king", "ace"]
        self.cards = []

        for _suit in ["hearts", "diamonds", "spades", "clubs"]:
            for _rank in self.numeric_cards + self.face_cards:
                self.cards.append(CardObject(
                    rank=_rank,
                    suit=_suit
                ))

    def sort_cards_by_suit(self):
        """
        Arranges self.cards by CardObject.suit.

        :return: list
        """
        ret_val = {}
        for card in self.cards:
            if card.suit in ret_val:
                ret_val[card.suit].append(card)
            else:
                ret_val[card.suit] = [card]
        return ret_val

    def pull_card(self, pos=None):
        """
        Returns a CardObject object from self.deck and removes that CardObject object from the self.cards list.
        
        :param pos: List index position of card to be extracted. If not defined, a random index will be used.
        :return: CardObject object
        """
        try:
            if pos is None:
                pos = self.get_random_card_index()
            return self.cards.pop(pos)
        except IndexError:
            return None

    def insert_card(self, card, pos=None):
        """
        Inserts <card> into self.cards list and returns the index of the inserted ojject.
        
        :param pos: List index position where <card> is to be inserted. If not defined, a random index will be used.
        :return: int of inserted index
        """
        try:
            if pos is None:
                pos = self.get_random_card_index()
            self.cards.insert(pos, card)
            return pos
        except IndexError:
            self.cards.append(card)
            return len(self.cards)-1

    def get_random_card_index(self):
        """
        Returns the list index for a randomly selected CardObject object in self.cards

        :return: int
        """
        return random.randrange(0, len(self.cards))


class CardObject(object):
    """
    Object representing a single card.
    """
    def __init__(self, rank, suit, **kwargs):
        if suit in ["hearts", "diamonds"]:
            _color = "red"
        elif suit in ["spades", "clubs"]:
            _color = "black"
        else:
            _color = None

        self.rank = str(rank)
        self.suit = suit
        self.rank_abr = kwargs.get("rank_abr", self.rank if isinstance(rank, int) else self.rank[0])
        self.suit_abr = kwargs.get("suit_abr", self.suit[0])
        self.color = kwargs.get("color", _color)
        self.value = kwargs.get("value", self._get_default_value(rank))
        self.wild = kwargs.get("wild", False)
        self.short_name = kwargs.get("short_name", f'{self.rank_abr.upper()}{self.suit_abr}')
        self.long_name = kwargs.get("long_name", f'{self.rank} of {self.suit}')
        self.name = kwargs.get("name", self.short_name)
        self.symbol = kwargs.get("symbol", self._get_default_suit_symbol(self.suit))
        self.face = kwargs.get("face", f'{self.rank_abr.upper()}{self.symbol}')

    def _get_default_value(self, rank):
        face_card_values = {
            "jack" : 11,
            "queen" : 12,
            "king" : 13,
            "ace" : 1,
            "joker" : 0
        }

        if isinstance(rank, int):
            return rank
        elif rank in face_card_values:
            return face_card_values[rank.lower()]
        else:
            return -1

    def _get_default_suit_symbol(self, suit):
        if suit in ["diamonds", "diamond"]:
            return "♦"
        elif suit in ["clubs", "club"]:
            return "♣"
        elif suit in ["hearts", "heart"]:
            return "♥"
        elif suit in ["spades", "spade"]:
            return "♠"
        else:
            return suit[0].upper()
