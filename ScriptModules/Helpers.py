from Compute import Transformer as Transformer
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
        match line[i]:
            case "=":
                separator = i
            case "{":
                if flag:
                    seriesStart = i + 1
                    continue
                confStart = i + 1
            case "}":
                if flag:
                    seriesEnd = i
                    break
                confEnd = i
                flag = True
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
            return Transformer.fetch(inputConf=inputConf)
        case "SimpleMovingAverage":
            return Transformer.SimpleMovingAverage(
                inputConf=inputConf, inputSeries=inputSeries
            )
        case "ExponentialMovingAverage":
            return Transformer.ExponentialMovingAverage(
                inputConf=inputConf, inputSeries=inputSeries
            )
        case "RateOfChange":
            return Transformer.RateOfChange(
                inputConf=inputConf, inputSeries=inputSeries
            )
        case "CrossAbove":
            return Transformer.CrossAbove(inputSeries=inputSeries)
        case "ConstantSeries":
            return Transformer.ConstantSeries(
                inputConf=inputConf, inputSeries=inputSeries
            )
        case "PortfolioSimulation":
            return Transformer.PortfolioSimulation(
                inputConf=inputConf, inputSeries=inputSeries
            )
        case _:
            raise SyntaxError
