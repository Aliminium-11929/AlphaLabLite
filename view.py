from Modules import ScriptDataControl


def view(id: str, varnames: list[str]) -> str:
    """Orchastrates the viewing of the results of a given script ID."""
    try:
        JSON_DICT = ScriptDataControl.get(str_id=id)
        output_str = ""
        for varname in varnames:
            output_str += (
                varname + ": \n" + " " * 4 + str(JSON_DICT[varname]) + "\n\n\n"
            )
        return output_str
    except FileNotFoundError:
        raise FileNotFoundError
