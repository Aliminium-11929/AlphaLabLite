class InstructionOutput(object):
    """Instruction Ouptut model for the application"""

    varname = ""
    output = None

    def __init__(self, varname: str = "", output=None) -> None:
        self.varname = varname
        self.output = output

    def toDict(self):
        return {"varname": self.varname, "output": self.output}
