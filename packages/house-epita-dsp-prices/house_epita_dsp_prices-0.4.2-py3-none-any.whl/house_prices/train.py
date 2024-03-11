
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_log_error
from sklearn.linear_model import LinearRegression
from .preprocess import process_data, make_encoder, make_scaler
from sklearn.model_selection import train_test_split


def build_model(data_train: pd.DataFrame, categorical_columns: list,
                continuous_columns: list, path: str) -> dict[
    str, float]:
    X_train, X_test, y_train, y_test = get_train_data(data_train)
    make_encoder(X_train, categorical_columns, path)
    make_scaler(X_train, continuous_columns, path)
    X_train = process_data(X_train, categorical_columns, continuous_columns, path)
    X_test = process_data(X_test, categorical_columns, continuous_columns, path)
    model = make_model(X_train, y_train, path)
    y_pred = abs(model.predict(X_test))
    rmsle = compute_rmsle(y_test, y_pred)

    return {"rmsle": round(rmsle, 2)}


def get_train_data(data: pd.DataFrame) -> (pd.DataFrame, pd.DataFrame):
    X, y = (data.loc[:, data.columns != "SalePrice"],
            data["SalePrice"])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0
    )
    for data in [X_train, X_test, y_train, y_test]:
        data.reset_index(drop=True, inplace=True)
    return X_train, X_test, y_train, y_test


def make_model(X_train: pd.DataFrame, y_train: pd.DataFrame, path: str) \
        -> LinearRegression:
    model_path = path + "lreg.model"
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    return model


def compute_rmsle(y_test: np.ndarray, y_pred: np.ndarray, precision: int = 2) -> float:
    rmsle = np.sqrt(mean_squared_log_error(y_test, y_pred))
    return round(rmsle, precision)
