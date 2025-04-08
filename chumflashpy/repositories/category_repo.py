class CategoryRepo:
    def __init__(self):
        self.categories = {}

    def add(self, category):
        index = max(self.categories.keys(), default=0) + 1
        category.id = index
        self.categories[index] = category

    def get_by_id(self, id):
        return self.categories[id]

    def get_list(self):
        return list(self.categories.values())

    def get_index_list(self):
        return list(self.categories.keys())
