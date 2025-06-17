from database import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models.category import Category


class CategoryRepo:
    def __init__(self):
        # self.categories = {}
        self.Session = sessionmaker(bind=engine)
        self.Session = self.Session()

    def add(self, category):
        # check name existence
        e = (
            self.Session.query(Category)
            .filter(func.lower(Category.name) == category.name.lower())
            .first()
        )
        # e = {k: v for (k, v) in self.categories.items() if v.name == category.name}
        if e:
            raise ValueError()

        # index = max(self.categories.keys(), default=0) + 1
        # category.id = index
        # self.categories[index] = category
        category.id = None
        self.Session.add(category)
        self.Session.commit()
        return self.get_by_name(category)

    def get_by_name(self, name):
        return (
            self.Session.query(Category)
            .filter(func.lower(Category.name) == name.lower())
            .first()
        )

    def get_by_id(self, id):
        try:
            # return self.categories[id]
            return self.Session.get(Category, id)
        except KeyError:
            return None

    def get_list(self):
        # return list(self.categories.values())
        list = self.Session.query(Category).order_by(Category.name).all()
        return list

    # def get_index_list(self):
    #    return list(self.categories.keys())
