"""
This script tests the median function.
"""
import pandas as pd

from src.utils.helper_functions.calculations import find_median


def test_find_median():
    df = pd.DataFrame({"feature": [1, 3, 5, 7, 9]})
    feature_name = "feature"
    expected_median = 5.0
    expected_index = 2
    median, median_index = find_median(df, feature_name)
    assert median == expected_median
    assert median_index == expected_index
