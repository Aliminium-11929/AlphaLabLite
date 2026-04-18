import pandas as pd


class DataReader(object):
    df = pd.DataFrame()

    def __init__(self) -> None:
        self.df = pd.read_csv("Data/fetch_transformation_data.csv", header=None)

    def OneMinuteGoldPrices(self):
        rawList = self.df.iloc[0, 1:].tolist()
        return list(map(lambda x: float(x), rawList))

    def OneMinuteSilverPrices(self):
        rawList = self.df.iloc[1, 1:].tolist()
        return list(map(lambda x: float(x), rawList))

    def OneMinuteBitcoinPrices(self):
        rawList = self.df.iloc[2, 1:].tolist()
        return list(map(lambda x: float(x), rawList))

    def OneMinuteEthereum(self):
        rawList = self.df.iloc[3, 1:].tolist()
        return list(map(lambda x: float(x), rawList))

    def OneMinuteEURUSD(self):
        rawList = self.df.iloc[4, 1:].tolist()
        return list(map(lambda x: float(x), rawList))

    def OneMinuteUSDJPY(self):
        rawList = self.df.iloc[5, 1:].tolist()
        return list(map(lambda x: float(x), rawList))


# # Test Code:
# rd = DataReader()
# L = rd.OneMinuteGoldPrices()
# print(L)
