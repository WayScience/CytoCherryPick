"""
This script tests the data check function. This is a test.
"""
import pathlib
import sys
import unittest

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

sys.path.append("tests")
sys.path.append("..src")
from src.utils.helper_functions.generate_test_data import generate_test_data


class TestDataCheck(unittest.TestCase):
    def test_data_check(self):
        """
        check to ensure that the test data is generated correctly

        returns:
            None
        """

        file_out_path = "tests/data/test_data.csv"
        self.df = generate_test_data(file_out_path, 100)
        assert pathlib.Path(file_out_path).exists()

    def test_data_check_identity(self):
        """
        check to ensure that the test data is generated correctly

        returns:
            None
        """
        self.test_data_check()
        num_of_rows = 100
        np.random.seed(0)
        df = pd.DataFrame(
            {
                "feature1": np.random.rand(num_of_rows),
                "feature2": np.random.rand(num_of_rows),
                "feature3": np.random.normal(-3, 1, num_of_rows),
                "image_name": ["image_" + str(i) for i in range(num_of_rows)],
            }
        )
        assert_frame_equal(self.df, df)
