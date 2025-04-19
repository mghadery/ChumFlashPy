from repositories.category_repo import CategoryRepo
from models.category import Category


def add_cat(categories: CategoryRepo):
    name = input("Give me the category name:")
    cat = Category(id=1, name=name)
    try:
        r = categories.add(cat)
    except ValueError:
        print("Category name exists")


def list_cats(categories: CategoryRepo):
    for c in categories.get_list():
        print(c.id, c.name, sep=": ")
