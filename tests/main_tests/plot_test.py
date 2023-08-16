import sys
import unittest

import matplotlib.pyplot as plt
import pandas as pd

sys.path.append("tests")
sys.path.append("..src")
from src.utils.helper_functions import plot_histogram


class TestPlot(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(
            {
                "feature": [1, 3, 5, 7, 9],
                "image_name": ["image1", "image2", "image3", "image4", "image5"],
            }
        )
        self.feature_name = "feature"
        self.image_name_column = "image_name"
        self.row_name = "image1"
        self.bins = 50

    def test_plot(self):

        plot = plot_histogram(
            self.df,
            self.feature_name,
            self.image_name_column,
            self.row_name,
            show=True,
        )


if __name__ == "__main__":
    unittest.main()
