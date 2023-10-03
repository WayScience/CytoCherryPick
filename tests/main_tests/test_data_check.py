"""
This script tests the data check function. This is a test.
"""
import pathlib

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

from src.utils.helper_functions.generate_test_data import data_generation


def test_data_check():
    """
    check to ensure that the test data is generated correctly
    """
    file_out_path = "tests/data/test_data.csv"
    assert pathlib.Path(file_out_path).exists()


def test_data_check_identity():
    """
    check to ensure that the test data is generated correctly
    """
    file_out_path = "tests/data/test_data.csv"
    num_of_rows = 100
    df = data_generation(output_file_path=file_out_path, num_of_rows=num_of_rows)
    assert len(df) == num_of_rows
    np.random.seed(0)
    new_df = pd.DataFrame(
        {
            # random distribution of data for testing
            "feature1": np.random.rand(num_of_rows),
            "feature2": np.random.rand(num_of_rows),
            # normal distribution of data for testing with a skewed mean
            "feature3": np.random.normal(-3, 1, num_of_rows),
            # image names for testing purposes
            "image_name": ["image_" + str(i) for i in range(num_of_rows)],
        }
    )
    assert_frame_equal(df, new_df)
