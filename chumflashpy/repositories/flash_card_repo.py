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

    def get_random(self, category_id=-1):
        # filter the cards using dictionary comprehension
        if category_id == -1:
            filtered = self.flash_cards
        else:
            filtered = {
                key: value
                for (key, value) in self.flash_cards.items()
                if value.category_id == category_id
            }

        # get a random
        if len(filtered) == 0:
            return None
        keys = list(filtered.keys())

        # key = keys[random.randint(0, len(keys) - 1)]
        key = random.choice(keys)

        return self.flash_cards[key]
