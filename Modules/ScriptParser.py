from Model.RegEx import RegEx
from Modules.LineParser import parse_line


def parse(scriptLines: list[str]) -> list[RegEx]:
    """Reads the script from stdin as raw string input, and returns the ID of the executed query."""
    try:  # Placeholder for advanced error checking implementation later, maybe specific detection of syntax error location
        regex_list: list[RegEx] = []
        for scriptLine in scriptLines:
            regex_list.append(parse_line(scriptLine))
        return regex_list
    except:
        raise SyntaxError
