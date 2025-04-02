class FlashCard:
    def __init__(
        self, id, front, back, tags, category_id, last_practiced, creation_at, username
    ):
        self.id = id
        self.front = front
        self.back = back
        self.tags = tags
        self.category_id = category_id
        self.last_practiced = last_practiced
        self.creation_at = creation_at
        self.username = username
