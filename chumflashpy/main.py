from models.flash_card import FlashCard
from models.category import Category
from repositories.flash_card_repo import FlashCardRepo
from repositories.category_repo import CategoryRepo

flash_cards = FlashCardRepo()
categories = CategoryRepo()


def add():
    front = input("Give me the front word or phrase:")
    back = input("Give me the back:")
    category_id = int(input("Give me the category id:"))
    flash_card = FlashCard(1, front, back, "italian", category_id, "now", "now", "me")
    flash_cards.add(flash_card)


def add_cat():
    name = input("Give me the category name:")
    cat = Category(1, name)
    categories.add(cat)


def test():
    front = input("Give me the front word or phrase:")
    category_id = input("Give me the category id:")
    card = flash_cards.get_by_front(front, category_id)
    if card is None:
        print("Card not found")
        return

    back = input("Give me the back:")

    if card.back == back:
        print("You did well!")
    else:
        print("Try again!")


def test_rand(category_id):
    card = flash_cards.get_random(category_id)
    if card is None:
        print("Card not found")
        return

    print("front:", card.front)
    back = input("Give me the back:")

    if card.back == back:
        print("You did well!")
    else:
        print("Try again!")


def test_menu():
    category_id = -1
    while True:
        command = input("Give command(c:category, t:test, e:main menu):").lower()
        match command:
            case "c":
                category_id = get_category_menu()
            case "t":
                test_rand(category_id)
            case "e":
                break


def get_category_menu():
    print("Select category id from the list below:")
    for c in categories.get_list():
        print(c.id, c.name, sep=": ")
    id = int(input("Input the id: "))
    if id not in categories.get_index_list():
        return -1
    return id


def list_cats():
    print(list_cats)
    for c in categories.get_list():
        print(c.id, c.name, sep=": ")


while True:
    command = input(
        "Give command(lc:list categories, ac:add cat, af:add flash, t:test, e:end):"
    ).lower()
    match command:
        case "lc":
            list_cats()
        case "af":
            add()
        case "ac":
            add_cat()
        case "t":
            test_menu()
        case "e":
            print("Bye!")
            break
