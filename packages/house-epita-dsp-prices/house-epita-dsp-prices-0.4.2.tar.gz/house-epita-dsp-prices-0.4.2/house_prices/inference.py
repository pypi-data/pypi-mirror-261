import joblib
import numpy as np
import pandas as pd
from .preprocess import process_data


def make_predictions(df: pd.DataFrame,path:str) -> np.array:
    df = process_data(df)
    model_path = path + "lreg.model"
    model = joblib.load(
        model_path
    )
    predictions = model.predict(df)
    return predictions
