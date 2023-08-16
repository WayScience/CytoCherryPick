import pandas as pd


def find_median(df, feature_name):
    """
    Finds the median of a feature in a pandas DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to search.
        feature_name (str): The name of the feature to find the median of.

    Returns:
        tuple: A tuple containing the median value and the index of the row containing the median.
    """
    median = df[feature_name].median()
    median_index = df[feature_name].searchsorted(median)
    return median, median_index
