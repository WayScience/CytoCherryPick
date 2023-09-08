#!/usr/bin/env python
# coding: utf-8

import pathlib

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
import seaborn as sns


def generate_test_data(output_file_path: str, num_of_rows: int = 100):
    # Define paths
    test_output_path = output_file_path.split("/")[-1]
    test_output_path = pathlib.Path(test_output_path)
    # make directory if not exist
    test_output_path.parent.mkdir(parents=True, exist_ok=True)
    test_output_path = pathlib.Path(output_file_path)

    # set seed
    np.random.seed(0)
    df = pd.DataFrame(
        {
            "feature1": np.random.rand(num_of_rows),
            "feature2": np.random.rand(num_of_rows),
            "feature3": np.random.normal(-3, 1, num_of_rows),
            "image_name": ["image_" + str(i) for i in range(num_of_rows)],
        }
    )
    # save the dataframe to a csv file
    df.to_csv(test_output_path, index=False)

    return df
