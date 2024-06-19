import os

from dotenv import load_dotenv
from beanie import init_beanie
from litestar import Litestar
from motor.motor_asyncio import AsyncIOMotorClient

from librarypy.controller import router
from librarypy.models import Book

load_dotenv()


async def main():
    client = AsyncIOMotorClient(os.environ.get(
        'DATABASE_URL', 'mongodb://localhost:27017'))
    await init_beanie(client[os.environ['DATABASE']], document_models=[Book])

app = Litestar(route_handlers=[router], on_startup=[main])
