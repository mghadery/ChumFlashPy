from repositories.flash_card_repo import FlashCardRepo
from repositories.category_repo import CategoryRepo

# from presentation.flash_ctrl import add_flash, test_flash_rand
import presentation.flash_ctrl as flash_ctrl

# from presentation.cat_ctrl import add_cat, list_cats
import presentation.cat_ctrl as cat_ctrl

from database import create_tables

create_tables()

flash_cards = FlashCardRepo()
categories = CategoryRepo()


while True:
    command = input(
        "Give command(lc:list categories, ac:add cat, af:add flash, t:test, e:end):"
    ).lower()
    match command:
        case "lc":
            cat_ctrl.list_cats(categories)
        case "af":
            flash_ctrl.add_flash(categories, flash_cards)
        case "ac":
            cat_ctrl.add_cat(categories)
        case "t":
            flash_ctrl.test_flash_rand(categories, flash_cards)
        case "e":
            print("Bye!")
            break
