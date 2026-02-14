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


def explode_date(df: pd.DataFrame, datename: str, format="%d-%m-%Y") -> pd.DataFrame:
    """
    Expand a datetime column into separate columns for year, month, day, etc.
    """
    df[datename] = pd.to_datetime(df[datename], format=format)
    df["Year"] = df[datename].dt.year.astype("Int64")
    df["Month"] = df[datename].dt.month.astype("Int64")
    df["Week"] = df[datename].dt.week.astype("Int64")
    df["Day"] = df[datename].dt.day.astype("Int64")
    df["Hour"] = df[datename].dt.hour.astype("Int64")
    df["Minute"] = df[datename].dt.minute.astype("Int64")
    df["second"] = df[datename].dt.second.astype("Int64")
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicates from a DataFrame.
    """
    rs, cs = df.shape
    df_model = df.drop_duplicates(inplace=False)
    if df_model.shape == (rs, cs):
        print("\n Pas de doublon dans le jeu de données")
    else:
        print(
            f"\n Nombre de doublons retirés ou coorigé dans le jeu de données  ---> {rs - df_model.shape[0]}"
        )
    return df_model
