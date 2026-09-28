import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_regression_model(name, model, X_train, y_train, X_test, y_test):
    """
    Give the score of a model on training and testing data.
    """
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    metrics = {}
    metrics["model"] = name
    metrics["RMSE_train"] = np.sqrt(mean_squared_error(y_train, y_train_pred))
    metrics["RMSE_test"] = np.sqrt(mean_squared_error(y_test, y_test_pred))
    metrics["MAE_train"] = mean_absolute_error(y_train, y_train_pred)
    metrics["MAE_test"] = mean_absolute_error(y_test, y_test_pred)
    metrics["R2_train"] = r2_score(y_train, y_train_pred)
    metrics["R2_test"] = r2_score(y_test, y_test_pred)
    
    return metrics
def score_model(model, x_train, y_train, x_test, y_test):
    """
    Give the score of a model on training and testing data as a string
    """
    output = "Score de modèle : \n"
    output += model.score(x_train, y_train)
    output += model.score(x_test, y_test)
    return output
