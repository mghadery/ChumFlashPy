from database import engine
from sqlalchemy.orm import sessionmaker


class CategoryRepo:
    def __init__(self):
        self.categories = {}
        self.Session = sessionmaker(bind=engine)
        self.Session = self.Session()

    def add(self, category):
        # check name existence
        e = {k: v for (k, v) in self.categories.items() if v.name == category.name}
        if e:
            raise ValueError()

        index = max(self.categories.keys(), default=0) + 1
        category.id = index
        self.categories[index] = category
        self.Session.add(category)
        self.Session.commit()

    def get_by_id(self, id):
        try:
            return self.categories[id]
        except KeyError:
            return None

    def get_list(self):
        return list(self.categories.values())

    def get_index_list(self):
        return list(self.categories.keys())
