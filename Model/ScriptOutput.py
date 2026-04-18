from uuid import uuid4

from beanie import Document
from pydantic import Field

from DB.db import UUIDstr
from Model.InstructionOutput import InstructionOutput


class ScriptOutput(Document):
    uuid: UUIDstr = Field(default_factory=uuid4)
    outputs_list: list[InstructionOutput] = Field(
        default_factory=list,
        description="Instruction outputs associated with the Script",
    )
