from uuid import uuid4

from Model.InstructionOutput import InstructionOutput


class ScriptOutput(object):
    id = uuid4()
    outputs_list: list[InstructionOutput] = []

    def __init__(self, outputs_list: list[InstructionOutput] = []) -> None:
        self.outputs_list = outputs_list

    def toDict(self):
        return {
            "id": str(self.id),
            "outputs_list": [
                instruction_output.toDict() for instruction_output in self.outputs_list
            ],
        }
