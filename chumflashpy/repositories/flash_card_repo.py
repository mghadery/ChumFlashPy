# from models.flash_card import FlashCard
import random


class FlashCardRepo:
    def __init__(self):
        self.flash_cards = {}

    def add(self, flash_card):
        index = max(self.flash_cards.keys(), default=0) + 1
        flash_card.id = index
        self.flash_cards[index] = flash_card

    def get_by_front(self, front):
        generator = (f for f in self.flash_cards.values() if f.front == front)
        card = next(generator, None)
        return card

    def get_random(self):
        keys = list(self.flash_cards.keys())
        key = keys[random.randint(0, len(keys) - 1)]
        return self.flash_cards[key]
