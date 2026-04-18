import os

from dotenv import load_dotenv

from DB.mongo import init_database
from Modules.Reader import Reader


async def main():
    load_dotenv()

    username = os.getenv("DB_USER")
    passwd = os.getenv("DB_PASS")
    mongo_uri_part_1 = os.getenv("MONGO_URI_PART_1")
    mongo_uri_part_2 = os.getenv("MONGO_URI_PART_2")

    csv_reader = Reader()
    assert (
        username is str
        and passwd is str
        and mongo_uri_part_1 is str
        and mongo_uri_part_2 is str
    ), print("Couldn't read database info from .env file.")
    await init_database(
        username=username, password=passwd, mongo_uri_part_2=mongo_uri_part_2
    )
