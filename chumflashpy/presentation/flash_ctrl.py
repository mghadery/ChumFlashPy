from repositories.category_repo import CategoryRepo
from repositories.flash_card_repo import FlashCardRepo
from models.flash_card import FlashCard
import datetime
from langdetect import detect_langs


def add_flash(categories: CategoryRepo, flash_cards: FlashCardRepo):
    if not categories.get_list():
        print("No category is defined")
        return
    print("Select Category from the list below:")
    cat_id = -1
    while cat_id < 0:
        for c in categories.get_list():
            print(c.id, c.name, sep=": ")
        try:
            cat_id = int(input("Category id: "))
        except ValueError:
            pass
    front = input("Give me the front word or phrase:")
    back = input("Give me the back:")
    now = datetime.datetime.now()

    print("Give me the tags. Press ^D(Linux) or ^Z+Enter(Win) to terminate the list!")
    tag_list = []
    while True:
        try:
            tag_list.append(input().strip().lower())
        except EOFError:
            break
    tag = ",".join(tag_list)
    front_langs = detect_langs(front)
    back_langs = detect_langs(back)

    if len(front_langs) == 1:
        front_lang = front_langs[0].lang
        x = input(
            f"Detected front lang is {front_lang}. If not correct, enter correct value otherwise press enter: "
        )
        if x:
            front_lang = x
    else:
        front_lang = input("front language code: ").strip()

    if len(back_langs) == 1:
        back_lang = back_langs[0].lang
        x = input(
            f"Detected back lang is {back_lang}. If not correct, enter correct value otherwise press enter: "
        )
        if x:
            back_lang = x
    else:
        back_lang = input("front language code: ").strip()
    # print(front_lang, back_lang)

    flash_card = FlashCard(
        front=front,
        back=back,
        tags=tag,
        category_id=cat_id,
        username="me",
        front_lang=front_lang,
        back_lang=back_lang,
    )
    flash_cards.add(flash_card)


def print_flash(card: FlashCard, categories: CategoryRepo):
    card_cat = categories.get_by_id(card.category_id)
    card_cat_name = card_cat.name if card_cat else ""
    print("Category:", card_cat_name)
    print("Tags:", card.tags)
    print("Created:", card.creation_at.strftime("%d/%m/%Y %H:%M:%S"))


def test_flash_rand(categories: CategoryRepo, flash_cards: FlashCardRepo):
    if not categories.get_list():
        print("No category is defined")
        return
    print("Select Category from the list below. Enter for all!")
    cat_id = -1
    while cat_id < 0:
        for c in categories.get_list():
            print(c.id, c.name, sep=": ")
        try:
            cat_id = int(input("Category id: "))
        except:
            break

    card = flash_cards.get_random(cat_id)
    if card is None:
        print("Card not found")
        return

    print("front:", card.front)
    back = input("Give me the back:")

    if card.back == back:
        print("You did well!")
        print_flash(card, categories)
    else:
        print("Try again!")
