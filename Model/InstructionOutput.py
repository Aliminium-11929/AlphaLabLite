class InstructionOutput(object):
    """Instruction Ouptut model for the application"""

    varname = ""
    output = []

    def __init__(self, varname: str = "", output: list[float] = []) -> None:
        self.varname = varname
        self.output = output
