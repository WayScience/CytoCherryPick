"""
This script tests the median function.
"""
import pandas as pd

from src.cytocherrypick.calculations import find_median


def test_find_median():
    # test for the median row in the mock data
    df = pd.DataFrame({"feature": [1, 3, 5, 7, 9]})
    # set the column name of interest
    feature_name = "feature"
    # we know the median is 5.0 and the index is 2
    expected_median = 5.0
    expected_index = 2
    # using the find_median function, we can find the median and index
    median, median_index = find_median(df, feature_name)
    # check that the median and index are correct
    assert median == expected_median
    assert median_index == expected_index
