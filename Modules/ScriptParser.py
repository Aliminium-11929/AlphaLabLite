from LineParser import parse_line
from Reader import Reader

from Model.InstructionOutput import InstructionOutput
from Model.RegEx import RegEx
from Model.ScriptOutput import ScriptOutput
from Transformations.ConstantSeries import ConstantSeries as cs
from Transformations.CrossAbove import CrossAbove as ca
from Transformations.ExponentialMovingAverage import ExponentialMovingAverage as ema
from Transformations.Fetch import Fetch as fetch
from Transformations.PortfolioSimulation import PortfolioSimulation as ps
from Transformations.RateOfChange import RateOfChange as roc
from Transformations.SimpleMovingAverage import SimpleMovingAverage as sma


class ScriptParser(object):
    var_to_call = {}
    csv_reader = Reader()

    def __init__(self) -> None:
        pass

    def execute(self, script: str):
        """Reads the script from stdin as raw string input, and returns the ID of the executed query."""

        try:  # Placeholder for advanced error checking implementation later, maybe specific detection of syntax error location
            scriptLines = script.splitlines()
            regex_list: list[RegEx] = []
            for scriptLine in scriptLines:
                regex_list.append(parse_line(scriptLine))
            output_list: list[InstructionOutput] = []
            for regex in regex_list:
                match regex.callname:
                    # Possible callnames: [Fetch, SimpleMovingAverage, ExponentialMovingAverage, RateOfChange, CrossAbove, ConstantSeries, PortfolioSimulation]
                    case "Fetch":
                        output_list.append(fetch(inputConf=regex.inputConf))
                    case "SimpleMovingAverage":
                        output_list.append(
                            sma(
                                inputConf=regex.inputConf, inputSeries=regex.inputSeries
                            )
                        )
                    case "ExponentialMovingAverage":
                        output_list.append(
                            ema(
                                inputConf=regex.inputConf, inputSeries=regex.inputSeries
                            )
                        )
                    case "RateOfChange":
                        output_list.append(
                            roc(
                                inputConf=regex.inputConf, inputSeries=regex.inputSeries
                            )
                        )
                    case "CrossAbove":
                        output_list.append(ca(inputSeries=regex.inputSeries))
                    case "ConstantSeries":
                        output_list.append(
                            cs(inputConf=regex.inputConf, inputSeries=regex.inputSeries)
                        )
                    case "PortfolioSimulation":
                        output_list.append(
                            ps(inputConf=regex.inputConf, inputSeries=regex.inputSeries)
                        )
            script_result = ScriptOutput(outputs_list=output_list)
        except:
            return "Script syntax error. Query not executed."
