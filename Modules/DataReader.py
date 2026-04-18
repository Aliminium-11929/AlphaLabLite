import pandas as pd


class DataReader(object):
    df = None
    OneMinuteGoldPrices = []

    def __init__(self) -> None:
        self.df = pd.read_csv("Data/fetch_transformation_data.csv", header=None)
        self.OneMinuteGoldPrices = self.df.iloc[0]
