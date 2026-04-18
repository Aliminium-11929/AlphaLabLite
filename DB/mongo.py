from beanie import init_beanie

from DB.db import (
    initialize,
)
from Model.ScriptOutput import ScriptOutput

DATABASE_NAME: str = "my_db"


async def init_database(
    username: str,
    password: str,
    mongo_uri_part_2: str,
) -> None:
    """Initialize Beanie with all models using the real database."""
    async_client = initialize(
        username=username,
        password=password,
        mongo_uri_part_2=mongo_uri_part_2,
    )

    models = [ScriptOutput]

    await init_beanie(
        database=async_client["script_outputs"],
        document_models=models,
    )
