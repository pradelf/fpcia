import pandas as pd


def how_null_is_it(df: pd.DataFrame) -> str:
    output = "________________________________________________\n"
    output += f"Overall missing values in dataset : {df.isnull().sum().sum()}\n"
    output += "\n"
    output += "missing values in dataset per column :\n"
    output += str(df.isnull().sum()) + "\n"
    output += "________________________________________________\n"
    return output


def inShape(df: pd.DataFrame) -> str:
    """Return the shape of the dataset as a string."""
    output = "________________________________________________\n"
    output += f"The shape of the dataset is: {df.shape}\n"
    output += "________________________________________________\n"
    return output


def summary(df: pd.DataFrame) -> str:
    """Print a summary of the dataset."""
    output = "________________________________________________\n"
    output += "Data Start\n"
    output += str(df.head(10)) + "\n"
    output += "Data End\n"
    output += str(df.tail(10)) + "\n"
    output += "________________________________________________\n"
    output += inShape(df)
    output += "columns of the dataset : \n"
    output += str(df.columns) + "\n"
    output += "data describe : \n"
    output += str(df.describe(include="all")) + "\n"
    output += "data info : \n"
    output += str(df.info()) + "\n"
    output += "types in dataset :\n"
    output += str(df.dtypes) + "\n"
    output += how_null_is_it(df)
    output += "________________________________________________\n"
    return output


def score_model(model, x_train, y_train, x_test, y_test):
    """Give the score of a model on training and testing data."""
    output = "Score de modèle : \n"
    output += model.score(x_train, y_train)
    output += model.score(x_test, y_test)
    return output


def how_null_is_it(df: pd.DataFrame) -> str:  # noqa: F811
    """Print missing values in the dataset."""
    chaine = f"""________________________________________________
            Overall missing values in dataset : {df.isnull().sum().sum()}
            missing values in dataset per column 
            {df.isnull().sum()}
            ________________________________________________"""
    return chaine
