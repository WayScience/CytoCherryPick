import sys
import unittest

import pandas as pd

sys.path.append("tests")
sys.path.append("..src")
from src.utils.helper_functions.find_median import find_median


class TestFindMedian(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({"feature": [1, 3, 5, 7, 9]})
        self.feature_name = "feature"

    def test_find_median(self):
        expected_median = 5.0
        expected_index = 2
        median, median_index = find_median(self.df, self.feature_name)
        self.assertEqual(median, expected_median)
        self.assertEqual(median_index, expected_index)


if __name__ == "__main__":
    unittest.main()
