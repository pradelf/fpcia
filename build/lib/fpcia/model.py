import pandas as pd


def score_model(model, x_train, y_train, x_test, y_test):
    """
    Give the score of a model on training and testing data.
    """
    output = "Score de modèle : \n"
    output += model.score(x_train, y_train)
    output += model.score(x_test, y_test)
    return output
