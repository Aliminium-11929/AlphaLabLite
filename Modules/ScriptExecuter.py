from Model.InstructionOutput import InstructionOutput
from Model.RegEx import RegEx
from Modules.Transformer import ConstantSeries as cs
from Modules.Transformer import CrossAbove as ca
from Modules.Transformer import ExponentialMovingAverage as ema
from Modules.Transformer import Fetch as fetch
from Modules.Transformer import PortfolioSimulation as ps
from Modules.Transformer import RateOfChange as roc
from Modules.Transformer import SimpleMovingAverage as sma


def exists(alias: str, instruction_list: list[InstructionOutput]) -> InstructionOutput:
    """Returns the InstructionOutput object associated with the given alias."""
    for instruction in instruction_list:
        if alias == instruction.varname:
            return instruction
    raise SyntaxError


def execute(
    regex: RegEx, instruction_history: list[InstructionOutput]
) -> InstructionOutput:
    """Executes a regular expression by taking into consideration variables from previous lines of the script."""
    regex_output = InstructionOutput(varname=regex.varname)
    local_inputSeries = []
    # RegEx:
    # varname: str
    # callname: str
    # inputConf: list[str]
    # inputSeries: list[str]
    for alias in regex.inputSeries:
        local_inputSeries.append(exists(alias, instruction_history).output)

    match regex.callname:
        # Possible callnames: [Fetch, SimpleMovingAverage, ExponentialMovingAverage, RateOfChange, CrossAbove, ConstantSeries, PortfolioSimulation]
        case "Fetch":
            regex_output.output = fetch(
                inputConf=regex.inputConf,
            )
        case "SimpleMovingAverage":
            regex_output.output = sma(
                inputConf=regex.inputConf, inputSeries=local_inputSeries
            )
        case "ExponentialMovingAverage":
            regex_output.output = ema(
                inputConf=regex.inputConf, inputSeries=local_inputSeries
            )
        case "RateOfChange":
            regex_output.output = roc(
                inputConf=regex.inputConf, inputSeries=local_inputSeries
            )
        case "CrossAbove":
            regex_output.output = ca(
                inputSeries=local_inputSeries,
            )
        case "ConstantSeries":
            regex_output.output = cs(
                inputConf=regex.inputConf, inputSeries=local_inputSeries
            )
        case "PortfolioSimulation":
            regex_output.output = ps(
                inputConf=regex.inputConf, inputSeries=local_inputSeries
            )
        case _:
            raise SyntaxError
    return regex_output
