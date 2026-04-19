class RegEx(object):
    """A class to store a single regular expression in one object with static fields."""

    varname: str = ""
    callname: str = ""
    inputConf: list[str] = []
    inputSeries: list[str] = []

    def __init__(self, varname="", callname="", inputConf=[], inputSeries=[]) -> None:
        self.varname = varname
        self.callname = callname
        self.inputConf = inputConf
        self.inputSeries = inputSeries
