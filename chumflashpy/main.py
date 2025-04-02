from models.flash_card import FlashCard
from repositories.flash_card_repo import FlashCardRepo

flash_cards = FlashCardRepo()


def add():
    front = input("Give me the front word or phrase:")
    back = input("Give me the back:")
    flash_card = FlashCard(1, front, back, "italian", 1, "now", "now", "me")
    flash_cards.add(flash_card)


def test():
    front = input("Give me the front word or phrase:")
    card = flash_cards.get_by_front(front)
    if card is None:
        print("Card not found")
        return

    back = input("Give me the back:")

    if card.back == back:
        print("You did well!")
    else:
        print("Try again!")


def test_rand():
    card = flash_cards.get_random()
    if card is None:
        print("Card not found")
        return

    print("front:", card.front)
    back = input("Give me the back:")

    if card.back == back:
        print("You did well!")
    else:
        print("Try again!")


while True:
    command = input("Give command(a:add, t:test, e:end):").lower()
    match command:
        case "a":
            add()
        case "t":
            test_rand()
        case "e":
            print("Bye!")
            break
