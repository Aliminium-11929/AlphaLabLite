from DataControl.TransformationDataReader import DataReader


def ConstantSeries(inputConf: list[str], inputSeries: list[list[float]]) -> list[float]:
    """Outputs a constant series of value k of the same size as the input series."""
    k: float = float(inputConf[0])
    A: list[float] = inputSeries[0]
    B: list[float] = [k] * len(A)
    return B


def CrossAbove(inputSeries: list[list[float]]) -> list[float]:
    """Checks and returns a list of floats representing whether or not 2 input series intersected.
    1 means they have intersected at the point of its index, 0 means they haven't."""
    A_1: list[float] = inputSeries[0]
    A_2: list[float] = inputSeries[1]
    B: list[float] = [0.0] * len(A_1)
    B[0] = 0.0
    for t in range(1, len(B)):
        B[t] = 1.0 if (A_1[t - 1] < A_2[t - 1] and A_1[t] > A_2[t]) else 0.0
    return B


def ExponentialMovingAverage(
    inputConf: list[str], inputSeries: list[list[float]]
) -> list[float]:
    """Calculates and outputs a series forming an exponential moving average."""
    A: list[float] = inputSeries[0]
    B: list[float] = [0.0] * len(A)
    alpha: float = float(inputConf[0])
    for t in range(len(B)):
        if t == 0:
            B[t] = A[t]
        else:
            B[t] = alpha * A[t] + (1 - alpha) * B[t - 1]
    return B


def Fetch(inputConf: list[str]) -> list[float]:
    """Fetches the series located at the row labeled $datasource$ within the inputConf in fetch_transformation_data.csv"""
    return DataReader().read(dataseries=inputConf[0])


def PortfolioSimulation(
    inputConf: list[str], inputSeries: list[list[float]]
) -> list[float]:
    """Performs a portfolio simulation and outputs the result as a time series."""
    balance = float(inputConf[0])
    price: list[float] = inputSeries[0]
    entry: list[float] = inputSeries[1]
    exit: list[float] = inputSeries[2]
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


def RateOfChange(inputConf: list[str], inputSeries: list[list[float]]) -> list[float]:
    """Calculates the rate of change of a time series over a specified period."""
    A: list[float] = inputSeries[0]
    B: list[float] = [float("nan")] * len(A)
    period: int = int(inputConf[0])
    for t in range(len(B)):
        if t < period:
            B[t] = float("nan")
            continue
        if A[t - period] == 0:
            B[t] = float("nan")
        else:
            B[t] = (A[t] - A[t - period]) / A[t - period]
    return B


def SimpleMovingAverage(
    inputConf: list[str], inputSeries: list[list[float]]
) -> list[float]:
    """Calculates and outputs a series forming a simple moving average."""
    A: list[float] = inputSeries[0]
    B: list[float] = [0.0] * len(A)
    window: int = int(inputConf[0])
    for t in range(len(B)):
        if t < window - 1:
            B[t] = float("nan")
        else:
            for i in range(t - window + 1, t + 1):
                B[t] += A[i] / window
    return B
