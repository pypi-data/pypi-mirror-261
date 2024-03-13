import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, OneHotEncoder

class DataPrepKitz:
    def __init__(self, filepath):
        self._df = self.read_data(filepath)
        self._file_path = filepath

    def read_data(self, filepath):
        file_extension = os.path.splitext(filepath)[1].lower()

        try:
            if file_extension == ".csv":
                return pd.read_csv(filepath)
            elif file_extension == ".xlsx" or file_extension == ".xls":
                return pd.read_excel(filepath)
            elif file_extension == ".json":
                return pd.read_json(filepath)
            else:
                print(f"Unsupported file type: {file_extension}")
                return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def summarize(self):
        print(self._df.info())
        print("\nHead of data:")
        print(self._df.head())
        print("\nKey statistical summaries:")

        print("\nCategorical summaries\n")
        for col in self._df.columns:
            if not pd.core.dtypes.common.is_numeric_dtype(self._df[col]):
                print(f"Column: {col}")
                print("Most Frequent Value:", self._df[col].mode().iloc[0])
                print("Value Counts:\n", self._df[col].value_counts())

    def drop_duplicates(self):
        self._df.drop_duplicates(inplace=True)

    def drop_rows_cols(self, rows=None, columns=None):
        if rows is not None:
            self._df.drop(rows, inplace=True)
        if columns is not None:
            self._df.drop(columns, axis=1, inplace=True)

    def drop_empty_columns(self):
        non_null_counts = self._df.notna().sum()
        empty_columns = non_null_counts[non_null_counts == 0].index
        self._df = self._df.drop(columns=empty_columns)

    def impute_avg(self):
        numeric_cols = self._df.select_dtypes(include=[np.number]).columns

        for col in numeric_cols:
            col_mean = self._df[col].mean()
            self._df[col] = self._df[col].fillna(col_mean)

    def impute_zero(self):
        numeric_cols = self._df.select_dtypes(include=[np.number]).columns

        for col in numeric_cols:
            self._df[col] = self._df[col].fillna(0)

    def encode_categorical(self, columns, method):
        if not set(columns).issubset(set(self._df.columns)):
            raise KeyError(f"{columns} are incorrect column names.")

        if method == "label":
            encoder = LabelEncoder()
        elif method == "ordinal":
            encoder = OrdinalEncoder()
        elif method == "one-hot":
            encoder = OneHotEncoder(handle_unknown='ignore')
        else:
            raise ValueError("Encoding method is not available")

        self._df[columns] = encoder.fit_transform(self._df[columns])