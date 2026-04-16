# Placeholder

from Model.InstructionOutput import InstructionOutput


class ScriptOutput(object):
    id = 0
    outputs_list: list[InstructionOutput] = []

    def __init__(self, id=0, outputs_list: list[InstructionOutput] = []) -> None:
        self.id = id
        self.outputs_list = outputs_list
