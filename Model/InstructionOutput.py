# Placeholder


class InstructionOutput(object):
    varname = ""
    output = None

    def __init__(self, varname: str = "", output=None) -> None:
        self.varname = varname
        self.output = output
