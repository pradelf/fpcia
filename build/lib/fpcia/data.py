import pandas as pd
from pydantic import BaseModel, ConfigDict


class MyPandaDataset(BaseModel):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def load_data(self) -> pd.DataFrame:
        """
        Load data from a CSV file.
        """
        self.data = pd.read_csv(self.filepath)
        return self.data

    def print_summary(self):
        """
        Print a summary of the dataset.
        """
        print("________________________________________________")
        print("Data Start")
        print(self.data.head(10))
        print("Data End")
        print(self.data.tail(10))
        print("shape of the dataset : ")
        print(self.data.shape)
        print("columns of the dataset : ")
        print(self.data.columns)
        print("data describe : ")
        print(self.data.describe(include="all"))
        print("types in dataset :")
        print(self.data.dtypes)
        print("________________________________________________")

    model_config = ConfigDict(str_max_length=10)


def explode_date(df: pd.DataFrame, datename: str) -> pd.DataFrame:
    """
    Expand a datetime column into separate columns for year, month, day, etc.
    """
    df[datename] = pd.to_datetime(df[datename])
    df["Year"] = df[datename].dt.year.astype("Int64")
    df["Month"] = df[datename].dt.month.astype("Int64")
    df["Day"] = df[datename].dt.day.astype("Int64")
    df["Hour"] = df[datename].dt.hour.astype("Int64")
    df["Minute"] = df[datename].dt.minute.astype("Int64")
    df["second"] = df[datename].dt.second.astype("Int64")
    return df
