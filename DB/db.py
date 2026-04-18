from typing import Annotated
from uuid import UUID

from dotenv import load_dotenv
from pydantic import PlainSerializer
from pymongo import AsyncMongoClient

UUIDstr = Annotated[UUID, PlainSerializer(lambda x: str(x), return_type=str)]


def initialize(
    username: str,
    password: str,
    mongo_uri_part_2: str,
) -> AsyncMongoClient:
    load_dotenv()
    mongo_uri_part_1 = "mongodb+srv://"
    mongo_uri = get_mongo_uri(
        username=username,
        password=password,
        mongo_uri_part_1=mongo_uri_part_1,
        mongo_uri_part_2=mongo_uri_part_2,
    )

    return AsyncMongoClient(mongo_uri)


def get_mongo_uri(
    username: str,
    password: str,
    mongo_uri_part_1: str,
    mongo_uri_part_2: str,
) -> str:
    return mongo_uri_part_1 + username + ":" + password + mongo_uri_part_2
