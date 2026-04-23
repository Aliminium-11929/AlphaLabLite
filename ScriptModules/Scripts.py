from Compute.Transformer import ConstantSeries as cs
from Compute.Transformer import CrossAbove as ca
from Compute.Transformer import ExponentialMovingAverage as ema
from Compute.Transformer import Fetch as fetch
from Compute.Transformer import PortfolioSimulation as ps
from Compute.Transformer import RateOfChange as roc
from Compute.Transformer import SimpleMovingAverage as sma
from Model.InstructionOutput import InstructionOutput


def SelectCallComponents(
    line: str,
) -> tuple[str | None, str | None, list[str] | None, list[str] | None]:
    """Returns the callname, inputConf, and inputSeries of a line."""
    separator = 0
    confStart = 0
    confEnd = 0
    seriesStart = 0
    seriesEnd = 0
    flag = False
    for i in range(len(line)):
        if not flag:
            match line[i]:
                case "=":
                    separator = i
                case "{":
                    confStart = i + 1
                case "}":
                    confEnd = i
                    flag = True
        else:
            match line[i]:
                case "{":
                    seriesStart = i + 1
                case "}":
                    seriesEnd = i
                    break
    varname: str | None = None if separator == 0 else line[:separator].strip()
    callname: str | None = (
        None
        if separator == confStart - 1
        else line[separator + 1 : confStart - 1].strip().rstrip()
    )
    inputConf: list[str] | None = (
        None
        if confStart == confEnd
        else [component.strip() for component in line[confStart:confEnd].split(",")]
    )
    inputSeries: list[str] | None = (
        None
        if seriesStart == seriesEnd
        else [component.strip() for component in line[seriesStart:seriesEnd].split(",")]
    )
    return varname, callname, inputConf, inputSeries


def parseAlias(alias: str, instruction_list: list[InstructionOutput]) -> list[float]:
    """Returns the output of the instruction associated with the given alias."""
    for instruction in instruction_list:
        if alias == instruction.varname:
            return instruction.output
    raise SyntaxError


def matchTransformation(
    callname: str, inputConf: list[str], inputSeries: list[list[float]]
) -> list[float]:
    """Performs the case matching between the callname and the transformation and returns the result."""
    # Possible callnames: [Fetch, SimpleMovingAverage, ExponentialMovingAverage, RateOfChange, CrossAbove, ConstantSeries, PortfolioSimulation]
    match callname:
        case "Fetch":
            return fetch(inputConf=inputConf)
        case "SimpleMovingAverage":
            return sma(inputConf=inputConf, inputSeries=inputSeries)
        case "ExponentialMovingAverage":
            return ema(inputConf=inputConf, inputSeries=inputSeries)
        case "RateOfChange":
            return roc(inputConf=inputConf, inputSeries=inputSeries)
        case "CrossAbove":
            return ca(inputSeries=inputSeries)
        case "ConstantSeries":
            return cs(inputConf=inputConf, inputSeries=inputSeries)
        case "PortfolioSimulation":
            return ps(inputConf=inputConf, inputSeries=inputSeries)
        case _:
            raise SyntaxError
