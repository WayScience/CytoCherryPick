import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sys.path.append(".utils")
from utils.helper_functions import find_median


# function to plot a histogram of a column in a dataframe and save the plot as a png file given a row name and column name
def plot_histogram(
    df: pd.DataFrame,
    feature_name: str,
    image_name_column: str,
    row_name=None,
    show=False,
):
    """_summary_

    Parameters
    ----------
    df : pd.DataFrame
        data frame containing the feature space and image name metadata
    feature_name : str
        column name of the feature to plot
    image_name_column : str
        column name of the column that contain the image name metadata
    row_name : _type_, optional
        name of the image to use for the density plot. If no defined the median image will be calculated, by default None
    show : bool, optional
        Whether or not the plot goes to device or not, by default False

    Returns
    -------
    sns.kdeplot return for plotting and saving
    """

    plt.subplots(figsize=(20, 2.5))
    plot = sns.kdeplot(
        df[feature_name],
        #    bins=bins,
        fill=True,
        color="r",
    )
    if row_name != None:
        plot.axvline(
            df[df[image_name_column] == row_name][feature_name].values[0],
            color="r",
            linestyle="--",
        )
    elif row_name is None:
        median, median_index = find_median(df, feature_name)
        plot.axvline(
            df.loc[median_index][feature_name],
            color="r",
            linestyle="--",
        )
    plot.set_title(feature_name)
    if show:
        plt.show()
    # return the plot
    return plot
