from uuid import uuid4

from Model.InstructionOutput import InstructionOutput


class ScriptOutput(object):
    id = uuid4()
    outputs_list: list[InstructionOutput] = []

    def __init__(self, outputs_list: list[InstructionOutput] = []) -> None:
        self.outputs_list = outputs_list

    def toDict(self) -> dict[str, list[float]]:
        Dict = {}
        for instruction in self.outputs_list:
            Dict[instruction.varname] = instruction.output
        return Dict
