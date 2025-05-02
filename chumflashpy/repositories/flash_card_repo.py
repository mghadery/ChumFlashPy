# from models.flash_card import FlashCard
from database import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models.flash_card import FlashCard
import random


class FlashCardRepo:
    def __init__(self):
        # self.flash_cards = {}
        self.Session = sessionmaker(bind=engine)
        self.Session = self.Session()

    def add(self, flash_card: FlashCard):
        # check name exists
        e = (
            self.Session.query(FlashCard)
            .filter(func.lower(FlashCard.front) == flash_card.front.lower())
            .first()
        )
        if e:
            raise ValueError

        # index = max(self.flash_cards.keys(), default=0) + 1
        flash_card.id = None  # index
        # self.flash_cards[index] = flash_card
        self.Session.add(flash_card)
        self.Session.commit()

    def get_by_front(self, front):
        # generator = (f for f in self.flash_cards.values() if f.front == front)
        # card = next(generator, None)
        card = (
            self.Session.query(FlashCard)
            .filter(func.lower(FlashCard.front) == front.lower())
            .first()
        )
        return card

    def get_random(self, category_id=-1):
        # filter the cards using dictionary comprehension
        # if category_id == -1:
        #     filtered = self.flash_cards
        # else:
        #     filtered = {
        #         key: value
        #         for (key, value) in self.flash_cards.items()
        #         if value.category_id == category_id
        #     }

        # get a random
        # if len(filtered) == 0:
        #     return None
        # keys = list(filtered.keys())

        filtered = (
            self.Session.query(FlashCard)
            .filter(category_id == -1 or FlashCard.category_id == category_id)
            .all()
        )
        keys = [f.id for f in filtered]

        # key = keys[random.randint(0, len(keys) - 1)]
        key = random.choice(keys)

        # return self.flash_cards[key]
        f = self.Session.get(FlashCard, key)
        return f
