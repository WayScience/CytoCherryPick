"""
This script generates a test dataset for the unit tests.
"""
import pathlib

import numpy as np
import pandas as pd


def data_generation(output_file_path: str, num_of_rows: int = 100) -> pd.DataFrame:
    """
    This function generates a test dataset for the unit tests.

    Parameters
    ----------
    output_file_path : str
        Output file path for the test dataset csv file
    num_of_rows : int, optional
        Number of rows of mock data to generate, by default 100

    Returns
    -------
    pandas.DataFrame
        Mock DataFrame
    """
    # Define paths
    output_file_path = pathlib.Path(output_file_path)
    # make directory if not exist
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
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
    df.to_csv(output_file_path, index=False)

    return df
