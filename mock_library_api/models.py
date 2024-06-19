from beanie import Document


class Book(Document):
    title: str
    author: str
    publisher: str
    publish_date: str

    class Settings:
        name = "books"
