# from models.flash_card import FlashCard
from database import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import or_
from models.flash_card import FlashCard
import random


class FlashCardRepo:
    def __init__(self):
        # self.flash_cards = {}
        self.Session = sessionmaker(bind=engine)
        self.Session = self.Session()

    def check_card(self, front: str) -> bool:
        """
        Checks if a front term has been used exactly in the stored flash cards.

        Parameters
        -------------
        front: str
            The front side term.

        Returns
        -------------
        bool
            True if the input front term is available, False otherwise.
        """
        e = (
            self.Session.query(FlashCard)
            .filter(func.lower(FlashCard.front) == front.lower())
            .first()
        )
        return not not e

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

    def get_list(self, category_id: int = -1) -> list[FlashCard]:
        """
        Returns all cards in the specified category.

        Parameters
        -------------
        category_id: int
            The specified category id.

        Returns
        -------------
        list[FlashCard]
            List of flash cards.
        """
        filtered = (
            self.Session.query(FlashCard)
            .filter(category_id == -1 or FlashCard.category_id == category_id)
            .all()
        )
        filtered.sort(key=lambda card: card.front)
        return filtered

    def search(self, search_phrase: str) -> list[FlashCard]:
        """
        Returns the cards with the specified phrase in their front or back side.

        Parameters
        -------------
        search_phrase: str
            The specified search phrase.

        Returns
        -------------
        list[FlashCard]
            List of flash cards.
        """
        search_phrase = search_phrase.strip().lower()
        print("qqq")
        filtered = (
            self.Session.query(FlashCard)
            .filter(
                or_(
                    func.lower(FlashCard.front).contains(search_phrase),
                    func.lower(FlashCard.back).contains(search_phrase),
                )
            )
            .all()
        )  # TODO case insensitive

        print("sss")
        filtered.sort(key=lambda card: card.front)
        return filtered

    def remove_card(self, id: int) -> bool:
        """
        Deletes a card with the specified id.

        Parameters
        -------------
        front: id
            The specified id.

        Returns
        -------------
        bool
            True if the existing card is deleted successfully.
        """
        fc = self.Session.get(FlashCard, id)
        self.Session.delete(fc)
        self.Session.commit()
        return True
