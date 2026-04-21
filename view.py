from Modules import ScriptDataControl


def view(id: str, varnames: list[str]) -> dict[str, list[float]]:
    """Orchastrates the viewing of the results of a given script ID."""
    try:
        JSON_DICT = ScriptDataControl.get(str_id=id)
        requested_data = {}
        for varname in varnames:
            requested_data[varname] = JSON_DICT[varname]
        return requested_data
    except FileNotFoundError:
        raise FileNotFoundError
