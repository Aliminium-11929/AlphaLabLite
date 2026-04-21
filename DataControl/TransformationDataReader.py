import pandas as pd


class DataReader(object):
    """Object that loads the csv file into a dataframe as a member variable."""

    df = pd.DataFrame()

    def __init__(self) -> None:
        self.df = pd.read_csv(
            "Data/fetch_transformation_data.csv", header=None, index_col=0
        )

    def read(self, dataseries: str):
        """Outputs the row labeled $dataseries$ in list form."""
        rawList = self.df.loc[dataseries, 1:].tolist()
        return list(map(lambda x: float(x), rawList))
