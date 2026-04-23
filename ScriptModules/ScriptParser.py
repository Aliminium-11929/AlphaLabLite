from Model.RegEx import RegEx
from ScriptModules.Scripts import SelectCallComponents


def parse_line(scriptLine: str) -> RegEx:
    """Parses a line into the defined regular expression."""
    # Assuming line is in form: "varname = callname{inputConf}{inputSeries}"
    varname, callname, inputConf, inputSeries = SelectCallComponents(line=scriptLine)
    if varname and callname:  # To make sure the syntax is valid.
        return RegEx(
            varname=varname,
            callname=callname,
            inputConf=inputConf,
            inputSeries=inputSeries,
        )
    raise SyntaxError


def parse(scriptLines: list[str]) -> list[RegEx]:
    """Reads the script from stdin as raw string input, and returns the ID of the executed query."""
    try:  # Placeholder for advanced error checking implementation later, maybe specific detection of syntax error location
        regex_list: list[RegEx] = []
        for scriptLine in scriptLines:
            regex_list.append(parse_line(scriptLine))
        return regex_list
    except SyntaxError:
        raise SyntaxError
