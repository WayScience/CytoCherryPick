"""
This is the main script for the cherry pick function.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from cytocherrypick.calculations import find_median
from cytocherrypick.generate_test_data import data_generation
from cytocherrypick.plot_distribution import plot_dist


def cherry_pick(
    df: pd.DataFrame,
    feature_name: str,
    image_name: str = None,
    save_path: str = None,
    show: bool = False,
) -> None:
    """
    This function operates similar to the helper function plot_dist, but this function contains logic to determine if the median image has been provided or not
    ----------
    df : pd.DataFrame
        the dataframe that contains the data to be plotted
    feature_name : str
        the name of the feature that is wanted to be plotted
    median : float
        the median of the feature
    median_index : int
        the index of the median of the feature
    image_name : str
        the name of the image that is wanted to be plotted
    save_path : str, optional
        the path to save the plot to, by default None and plot will not be saved
    show : bool, optional
        the boolean that determines if the plot is shown to the device, by default False
    Returns
    -------
    None, unless show is set to True, then the plot is shown
    """

    # determine if the image name is provided
    if image_name is not None:
        plot_dist(df, feature_name, image_name, show, save_path)
    else:
        median, median_index = find_median(df, feature_name)
        image_name = df["image_name"][median_index]
        plot_dist(df, feature_name, image_name, show, save_path)
