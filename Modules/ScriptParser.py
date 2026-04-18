from LineParser import parse_line

from Model.RegEx import RegEx


class ScriptParser(object):
    def __init__(self) -> None:
        pass

    def parse(self, script: str) -> list[RegEx]:
        """Reads the script from stdin as raw string input, and returns the ID of the executed query."""
        try:  # Placeholder for advanced error checking implementation later, maybe specific detection of syntax error location
            scriptLines = script.splitlines()
            regex_list: list[RegEx] = []
            for scriptLine in scriptLines:
                regex_list.append(parse_line(scriptLine))
            return regex_list
        except:
            raise SyntaxError
