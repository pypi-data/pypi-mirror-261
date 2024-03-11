import joblib
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def process_data(df: pd.DataFrame, categorical_columns: list, continuous_columns: list, path: str) -> pd.DataFrame:
    df = select_features(df, categorical_columns, continuous_columns)
    df = encode_categorical(df, categorical_columns, path)
    df = scale_continuous(df, continuous_columns, path)
    return df


def select_features(df: pd.DataFrame, categorical_columns: list, continuous_columns: list) -> pd.DataFrame:
    df = df[categorical_columns].join(df[continuous_columns])
    return df


# Create encoder
def make_encoder(df: pd.DataFrame, categorical_columns: list, path: str) -> joblib:
    encoder_path = path + "encoder.joblib"
    encoder = OneHotEncoder(handle_unknown="ignore", dtype=int)
    encoder.fit(df[categorical_columns])
    joblib.dump(encoder, encoder_path)


# Encode the categorial columns
def encode_categorical(df: pd.DataFrame, categorical_columns: list, path: str) -> pd.DataFrame:
    encoder_path = path + "encoder.joblib"
    encoder = joblib.load(encoder_path)
    encoded_columns = encoder.transform(df[categorical_columns])
    encoded_df = pd.DataFrame(
        encoded_columns.toarray(),
        columns=encoder.get_feature_names_out(categorical_columns),
    )
    df = df.drop(categorical_columns, axis=1).join(encoded_df)
    return df


def make_scaler(df: pd.DataFrame, continuous_columns: list, path: str) -> joblib:
    scaler_path = path + "scaler.joblib"
    scaler = StandardScaler()
    scaler.fit(df[continuous_columns])
    joblib.dump(scaler, scaler_path)


def scale_continuous(df: pd.DataFrame, continuous_columns: list, path: str) -> pd.DataFrame:
    scaler_path = path + "scaler.joblib"
    scaler = joblib.load(scaler_path)
    scaled_columns = scaler.transform(df[continuous_columns])
    scaled_df = pd.DataFrame(
        scaled_columns, columns=scaler.get_feature_names_out(continuous_columns)
    )
    df = df.drop(continuous_columns, axis=1).join(scaled_df)
    return df
