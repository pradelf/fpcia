import pandas as pd
from pydantic import BaseModel, ConfigDict


class MyPandaDataset(BaseModel):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def load_data(self) -> pd.DataFrame:
        """Load data from a CSV file."""
        self.data = pd.read_csv(self.filepath)
        return self.data

    def summary(self):
        """Print a summary of the dataset."""
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
