from Model.InstructionOutput import InstructionOutput
from Model.RegEx import RegEx
from Modules.Transformer import ConstantSeries as cs
from Modules.Transformer import CrossAbove as ca
from Modules.Transformer import ExponentialMovingAverage as ema
from Modules.Transformer import Fetch as fetch
from Modules.Transformer import PortfolioSimulation as ps
from Modules.Transformer import RateOfChange as roc
from Modules.Transformer import SimpleMovingAverage as sma


def execute(regex: RegEx) -> InstructionOutput:
    match regex.callname:
        # Possible callnames: [Fetch, SimpleMovingAverage, ExponentialMovingAverage, RateOfChange, CrossAbove, ConstantSeries, PortfolioSimulation]
        case "Fetch":
            return fetch(inputConf=regex.inputConf)
        case "SimpleMovingAverage":
            return sma(inputConf=regex.inputConf, inputSeries=regex.inputSeries)
        case "ExponentialMovingAverage":
            return ema(inputConf=regex.inputConf, inputSeries=regex.inputSeries)
        case "RateOfChange":
            return roc(inputConf=regex.inputConf, inputSeries=regex.inputSeries)
        case "CrossAbove":
            return ca(inputSeries=regex.inputSeries)
        case "ConstantSeries":
            return cs(inputConf=regex.inputConf, inputSeries=regex.inputSeries)
        case "PortfolioSimulation":
            return ps(inputConf=regex.inputConf, inputSeries=regex.inputSeries)
        case _:
            raise SyntaxError
