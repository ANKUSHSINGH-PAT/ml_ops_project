import os
import pandas as pd

# Define the expected schema
EXPECTED_COLUMNS = [
    "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
    "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density",
    "pH", "sulphates", "alcohol", "quality"
]

def test_file_exists():
    """Test if the dataset file exists."""
    assert os.path.exists("artifacts/data_ingestion/winequality-red.csv"), "Dataset file does not exist."

def test_column_names():
    """Test if the dataset has the expected columns."""
    df = pd.read_csv("artifacts/data_ingestion/winequality-red.csv")
    assert list(df.columns) == EXPECTED_COLUMNS, f"Columns do not match. Expected: {EXPECTED_COLUMNS}, Got: {list(df.columns)}"

def test_no_missing_values():
    """Test if the dataset has no missing values."""
    df = pd.read_csv("artifacts/data_ingestion/winequality-red.csv")
    assert df.isnull().sum().sum() == 0, "Dataset contains missing values."

def test_data_types():
    """Test if the dataset columns have the correct data types."""
    df = pd.read_csv("artifacts/data_ingestion/winequality-red.csv")
    expected_types = {
        "fixed acidity": float,
        "volatile acidity": float,
        "citric acid": float,
        "residual sugar": float,
        "chlorides": float,
        "free sulfur dioxide": float,
        "total sulfur dioxide": float,
        "density": float,
        "pH": float,
        "sulphates": float,
        "alcohol": float,
        "quality": int,
    }
    for column, dtype in expected_types.items():
        assert df[column].dtype == dtype, f"Column {column} has incorrect type. Expected: {dtype}, Got: {df[column].dtype}"

if __name__ == "__main__":
    test_file_exists()
    test_column_names()
    test_no_missing_values()
    test_data_types()
    print("All tests passed!")