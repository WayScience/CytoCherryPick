
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def plot_dist(
    df: pd.DataFrame,
    feature_name: str = None,
    image_name: str = None,
    show: bool = False,
    save_path: str = None,
):
    """ "
    This function generates a density plot for a given image and the data of that column in a dataframe.
    Parameters
    ----------
    df : pd.DataFrame
        the dataframe that contains the data to be plotted
    image_name : str, optional
        the name of the image that is wanted to be plotted, by default None
    show : bool, optional
        the boolean that determines if the plot is shown to the device, by default False
    save_path : str, optional
        the path to save the plot to, by default None and plot will not be saved
    Returns
    -------
    None, unless show is set to True, then the plot is shown
    """

    # create a density plot for each column in the dataframe except the image name column
    # if given an image name show where in the distribution the image falls for each column in the dataframe

    # plots a density plot for each feature
    sns.kdeplot(
        df[feature_name], fill=True, label=feature_name, bw_adjust=0.5, clip=(-5, 5)
    )
    # plots a vertical line at the value of the feature for the given image name
    plt.axvline(
        df[df["image_name"] == image_name][feature_name].values[0],
        color="r",
        linestyle="--",
    )
    # set the title of the plot to the feature name for the given image name
    # this shows where in the distribution of a given featur the image falls for each feature
    plt.title(f"{image_name} location in the distribution of {feature_name}")
    if save_path is not None:
        plt.savefig(save_path)
    if show:
        plt.show()
    plt.close()
