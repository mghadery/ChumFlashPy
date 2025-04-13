from repositories.flash_card_repo import FlashCardRepo
from repositories.category_repo import CategoryRepo
from presentation.flash_ctrl import add_flash, test_flash_rand
from presentation.cat_ctrl import add_cat, list_cats


flash_cards = FlashCardRepo()
categories = CategoryRepo()


while True:
    command = input(
        "Give command(lc:list categories, ac:add cat, af:add flash, t:test, e:end):"
    ).lower()
    match command:
        case "lc":
            list_cats(categories)
        case "af":
            add_flash(categories, flash_cards)
        case "ac":
            add_cat(categories)
        case "t":
            test_flash_rand(categories, flash_cards)
        case "e":
            print("Bye!")
            break
