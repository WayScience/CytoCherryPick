"""
This module contains helper functions for calculations.
As of now, it only contains one function, find_median.
"""
from typing import Tuple

import numpy as np
import pandas as pd


def find_median(df: pd.DataFrame, feature_name: str) -> Tuple[float, int]:
    """
    Find the index of a dataframe's median value for a given column (feature)

    Parameters
    ----------
    df : pandas.DataFrame
        this dataframe contains the feature column
    feature_name : str
        the name of the column in the dataframe that contains the feature

    Returns
    -------

    median : float
        the median value of the feature column
    median_index : int
        the index of the median value of the feature column

    """
    median = df[feature_name].median()
    median_index = df[feature_name].sub(median).abs().idxmin()
    return median, median_index
