from Modules.DataReader import DataReader


# assume input in the form of:
# inputConf: [k]
# inputSeries: ['0.0','0.1' ...] basically a list of floats cast into a str
def ConstantSeries(inputConf: list[str], inputSeries: list[str]) -> list[float]:
    k: float = float(inputConf[0])
    A: list[float] = list(map(lambda x: float(x), inputSeries))
    B: list[float] = [k] * len(A)
    return B


# assume input in the form of:
# inputSeries: [ ['0.0','0.1' ...], ['0.01','2.3',...] ], list of 2 lists of floats cast into str
def CrossAbove(inputSeries: list[str]) -> list[int]:
    A_1: list[float] = list(map(lambda x: float(x), inputSeries[0]))
    A_2: list[float] = list(map(lambda x: float(x), inputSeries[1]))
    B: list[int] = [0] * len(A_1)
    B[0] = 0
    for t in range(1, len(B)):
        B[t] = 1 if (A_1[t - 1] < A_2[t - 1] and A_1[t] > A_2[t]) else 0
    return B


# assume input in the form of:
# inputConf: [alpha]
# inputSeries: ['0.0','0.1' ...] basically a list of floats cast into a str
def ExponentialMovingAverage(
    inputConf: list[str], inputSeries: list[str]
) -> list[float]:
    A: list[float] = list(map(lambda x: float(x), inputSeries))
    B: list[float] = [0.0] * len(A)
    alpha: int = int(inputConf[0])
    for t in range(len(B)):
        if t == 0:
            B[t] = A[t]
        else:
            B[t] = alpha * A[t] + (1 - alpha) * B[t - 1]
    return B


# assume input in the form of:
# inputConf: [datasource]
def Fetch(inputConf: list[str]) -> list[float]:
    """Fetches the series located at the row labeled $datasource$ within the inputConf in fetch_transformation_data.csv"""
    return DataReader().read(dataseries=inputConf[0])


# assume input in the form of:
# inputConf: [balance]
# inputSeries: [price:[], entry:[], exit:[]] basically a list of floats cast into a str
def PortfolioSimulation(inputConf: list[str], inputSeries: list[str]) -> list[float]:
    balance = float(inputConf[0])
    price: list[float] = list(map(lambda x: float(x), inputSeries[0]))
    entry: list[float] = list(map(lambda x: float(x), inputSeries[1]))
    exit: list[float] = list(map(lambda x: float(x), inputSeries[2]))
    n = len(price)
    positions_held = 0

    portfolio = [0.0] * n
    for i in range(n):
        if exit[i] == 1:
            balance += positions_held * price[i]
        elif entry[i] == 1:
            positions_held += 1
            balance -= price[i]
        portfolio[i] = balance + positions_held * price[i]
    return portfolio


# assume input in the form of:
# inputConf: [period]
# inputSeries: ['0.0','0.1' ...] basically a list of floats cast into a str
def RateOfChange(inputConf: list[str], inputSeries: list[str]) -> list[float]:
    A: list[float] = list(map(lambda x: float(x), inputSeries))
    B: list[float] = [0.0] * len(A)
    period: int = int(inputConf[0])
    for t in range(len(B)):
        if A[t - period] == 0:
            B[t] = float("nan")
        else:
            B[t] = (A[t] - A[t - period]) / A[t - period]
    return B


# assume input in the form of:
# inputConf: [window]
# inputSeries: ['0.0','0.1' ...] basically a list of floats cast into a str
def SimpleMovingAverage(inputConf: list[str], inputSeries: list[str]) -> list[float]:
    A: list[float] = list(map(lambda x: float(x), inputSeries))
    B: list[float] = [0.0] * len(A)
    window: int = int(inputConf[0])
    for t in range(len(B)):
        if t < window - 1:
            B[t] = float("nan")
        else:
            for i in range(t - window + 1, t + 1):
                B[t] += A[i] / window
    return B
