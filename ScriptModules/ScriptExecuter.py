from Model.InstructionOutput import InstructionOutput
from Model.RegEx import RegEx
from ScriptModules.Scripts import matchTransformation, parseAlias


def execute(
    regex: RegEx, instruction_history: list[InstructionOutput]
) -> InstructionOutput:
    """Executes a regular expression by taking into consideration set variables from previous lines of the script."""
    regex_output = InstructionOutput(varname=regex.varname)
    local_inputSeries = []

    def alias_output_finder():
        """Parses the inputSeries from variable names into their previous results."""
        if regex.inputSeries:
            for alias in regex.inputSeries:
                local_inputSeries.append(parseAlias(alias, instruction_history))

    alias_output_finder()
    regex_output.output = matchTransformation(
        regex.callname, regex.inputConf, local_inputSeries
    )
    return regex_output
