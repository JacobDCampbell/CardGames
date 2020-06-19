#!/usr/bin/env python

# This file contains POC for all methods exposed by the PlayingCards module.
#
# TODO: Separate these into grouped example files that are easier to digest and use.
import sys
[sys.path.append(_path) for _path in [
    './lib', '../lib'
]]

from PlayingCards import NewDeck

def main():
    deck = NewDeck()
    card_pos = 46

    # Display Summary of all cards in deck
    print('--- All Cards ---')
    list_all_cards(deck)
    print('\n')

    # List cards, by suit
    print('--- Cards By Suit ---')
    list_cards_by_suit(deck)
    print('\n')

    # Pick a card from the deck by its index
    print('--- Pull A Card From Deck By Index ---')
    pulled_card = deck.pull_card(card_pos)
    print(f'The {pulled_card.long_name} has been pulled from the deck')
    list_all_cards(deck)
    print('\n')

    # Insert card to known position of the the deck
    print('--- Insert Card To Known Location ---')
    ins_pos = deck.insert_card(pulled_card, card_pos)
    print(f'The {pulled_card.long_name} has been inserted at position {ins_pos} in the deck')
    list_all_cards(deck)
    print('\n')

    # Pick a random card from the deck
    print('--- Pull A Random Card From Deck ---')
    rand_card = deck.pull_card()
    print(f'The {rand_card.long_name} has been pulled from the deck')
    list_cards_by_suit(deck)
    print('\n')

    # Insert card to random position of the the deck
    print('--- Insert Card To Random Location ---')
    ins_pos = deck.insert_card(rand_card)
    print(f'The {pulled_card.long_name} has been inserted at position {ins_pos} in the deck')
    list_all_cards(deck)
    print('\n')


def list_all_cards(deck):
    for idx in range(0, len(deck.cards)):
        clr_reset = "\033[0m"
        if deck.cards[idx].color == "red":
            clr_code = "\033[38;5;1m\033[48;5;15m"
        elif deck.cards[idx].color == "black":
            clr_code = "\033[38;5;0m\033[48;5;15m"
        else:
            clr_code = "\033[38;5;55m\033[48;5;15m"

        str_idx = str(idx).ljust(2)
        face = deck.cards[idx].face
        l_name = deck.cards[idx].long_name
        val = deck.cards[idx].value

        print(f'{str_idx}| {clr_code}{face.rjust(3)}{clr_reset} | {l_name} [value: {val}]')

def list_cards_by_suit(deck):
    sorted_deck = deck.sort_cards_by_suit()
    for suit in sorted_deck:
        print(f'{suit} : {", ".join(card.rank for card in sorted_deck[suit])}')


if __name__ == '__main__':
    main()