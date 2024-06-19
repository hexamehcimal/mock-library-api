from typing import Any, List
from litestar import Controller, Router
from litestar import get, post

from mock_library_api.models import Book


class BookController(Controller):
    path = "/"

    @get()
    async def get_books(self) -> List[Book]:
        books = await Book.find_all().to_list()
        return books

    @post()
    async def add_book(self, data: Book) -> Any:
        book = await Book.insert_one(data)
        print(book)
        pass


router = Router(path="/", route_handlers=[BookController])
