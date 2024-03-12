import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import sklearn
# 1. Data Reading:
def read_file(file_path):
    """
    Reads data from different file formats based on the file extension.
    Supports CSV, Excel, and JSON file formats.

    Args:
        file_path (str): The path to the file.

    Returns:
        DataFrame: The loaded data.

    Raises:
        ValueError: If the file format is not supported.
    """
    if file_path.endswith('.csv'):
        return read_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        return read_excel(file_path)
    elif file_path.endswith('.json'):
        return read_json(file_path)
    else:
        raise ValueError("Unsupported file format")
    
def read_csv(file_path):
    """
    Reads data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        DataFrame: The loaded data.
    """
    return pd.read_csv(file_path)

def read_excel(file_path):
    """
    Reads data from an Excel file.

    Args:
        file_path (str): The path to the Excel file.

    Returns:
        DataFrame: The loaded data.
    """
    return pd.read_excel(file_path)

def read_json(file_path):
    """
    Reads data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        DataFrame: The loaded data.
    """
    return pd.read_json(file_path)

# 2. Data Summary:
def get_summary_statistics(data):
    """
    Calculates summary statistics of the data.

    Args:
        data (DataFrame): The input data.

    Returns:
        DataFrame: The summary statistics.
    """
    return data.describe()

def get_mode(data):
    """
    Calculates the mode of the data.

    Args:
        data (DataFrame): The input data.

    Returns:
        Series: The mode of the data.
    """
    return data.mode().iloc[0]

def get_average(data):
    """
    Calculates the average of the data.

    Args:
        data (DataFrame): The input data.

    Returns:
        Series: The average of the data.
    """
    return data.mean()

def get_summary(data):
    """
    Generates a summary of the data including summary statistics, mode, and average.

    Args:
        data (DataFrame): The input data.

    Returns:
        dict: The summary information.
    """
    summary = {
        'Summary Statistics': get_summary_statistics(data),
        'Mode': get_mode(data),
        'Average': get_average(data)
    }
    return summary

# 3. Handling Missing Values:
def remove_missing_values(data):
    """
    Removes rows with missing values from the data.

    Args:
        data (DataFrame): The input data.

    Returns:
        DataFrame: The data with missing values removed.
    """
    return data.dropna()

def impute_missing_values(data, strategy='mean'):
    """
    Imputes missing values in the data based on the specified strategy.

    Args:
        data (DataFrame): The input data.
        strategy (str): The imputation strategy. Options: 'mean', 'median', 'mode' (default: 'mean').

    Returns:
        DataFrame: The data with missing values imputed.
    """
    if strategy == 'mean':
        return data.fillna(data.mean())
    elif strategy == 'median':
        return data.fillna(data.median())
    elif strategy == 'mode':
        return data.fillna(data.mode().iloc[0])
    else:
        raise ValueError("Invalid imputation strategy")

def handle_missing_values(data, strategy='remove'):
    """
    Handles missing values in the data based on the specified strategy.

    Args:
        data (DataFrame): The input data.
        strategy (str): The missing value handling strategy. Options: 'remove', 'mean', 'median', 'mode' (default: 'remove').

    Returns:
        DataFrame: The data with missing values handled.
    """
    if strategy == 'remove':
        return remove_missing_values(data)
    elif strategy in ['mean', 'median', 'mode']:
        return impute_missing_values(data, strategy)
    else:
        raise ValueError("Invalid missing value handling strategy")


# 4. Categorical Data Encoding:
# Method 1: One-Hot Encoding
def one_hot_encode(data, columns):
    """
    Performs one-hot encoding on categorical columns of the data.

    Args:
        data (DataFrame): The input data.
        columns (list): The list of categorical columns to encode.

    Returns:
        DataFrame: The data with one-hot encoded columns.
    """
    return pd.get_dummies(data, columns=columns)

# Method 2: Label Encoding
def label_encode(data, columns):
    """
    Performs label encoding on categorical columns of the data.

    Args:
        data (DataFrame): The input data.
        columns (list): The list of categorical columns to encode.

    Returns:
        DataFrame: The data with label encoded columns.
    """
    encoder = LabelEncoder()
    for column in columns:
        data[column] = encoder.fit_transform(data[column])
    return data

# Method 3: Target Encoding
def target_encode(data, target_column, categorical_columns):
    """
    Performs target encoding on categorical columns of the data.

    Args:
        data (DataFrame): The input data.
        target_column (str): The target column to encode.
        categorical_columns (list): The list of categorical columns to encode.

    Returns:
        DataFrame: The data with target encoded columns.
    """
    for column in categorical_columns:
        target_means = data.groupby(column)[target_column].mean()
        data[column] = data[column].map(target_means)
    return data