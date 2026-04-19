import json
import os

from Model.ScriptOutput import ScriptOutput


def write(script_output: ScriptOutput) -> str:
    """Writes a ScriptOutput object into its own JSON file."""
    json_string = json.dumps(script_output.toDict())
    id = str(script_output.id)
    os.makedirs("ScriptData", exist_ok=True)
    with open(f"ScriptData/{id}.json", "w") as JSON:
        json.dump(json_string, JSON)
    return str(script_output.id)


def get(str_id: str) -> dict:
    """Reads a ScriptOutput parsed as a dictionary from a JSON file."""
    jsonData = {}  # in the form of { id: <some-id>, outputs_list: [ {varname, output} ] }
    try:
        with open(f"ScriptData/{str_id}.json", "r") as JSON:
            jsonData = json.load(JSON)
        return jsonData
    except FileNotFoundError:
        raise FileNotFoundError
