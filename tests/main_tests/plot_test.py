"""
This script tests the plot function.
"""
import sys

import matplotlib.pyplot as plt
import pandas as pd

sys.path.append("tests")
sys.path.append("..src")
from src.utils.helper_functions.plot_distribution import plot_dist


def test_plot():
    """
    This function sets up the data for the plot test
    """
    df = pd.DataFrame(
        {
            "feature": [1, 3, 5, 7, 9],
            "image_name": ["image1", "image2", "image3", "image4", "image5"],
        }
    )
    feature_name = "feature"
    image_name = "image1"

    plot = plot_dist(df, feature_name, image_name, show=True)
    plt.show()
    plt.close()
