from Model.InstructionOutput import InstructionOutput
from Model.RegEx import RegEx
from Model.ScriptOutput import ScriptOutput
from Modules import ScriptDataControl, ScriptExecuter, ScriptParser


def execute(script: list[str]) -> str:
    """Orchastrates the execution of an ordered list of script lines."""
    if len(script) == 0:
        return "Empty Script. Nothing to do."
    regex_list: list[RegEx] = ScriptParser.parse(script)
    instruction_history: list[InstructionOutput] = []
    for i in range(len(regex_list)):
        instruction_history.append(
            ScriptExecuter.execute(regex_list[i], instruction_history)
        )
    OutputObject = ScriptOutput(instruction_history)
    local_id = str(OutputObject.id)
    ScriptDataControl.write(OutputObject)
    return "Script successfully executed: " + local_id
